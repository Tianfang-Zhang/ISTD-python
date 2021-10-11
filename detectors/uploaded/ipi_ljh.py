from detectors.base import *


class IPI1(BaseDetector):
    def __init__(self):
        super(IPI1, self).__init__()
        self.dw=50
        self.dh=50
        self.xstep=10
        self.ystep=10

    def mat2gray(self, image):
        return (image - np.min(image)) / np.ptp(image)

    def process(self, image):
        [m, n] = image.shape
        D = []
        for i in range(0, m - self.dh + 1, self.ystep):
            for j in range(0, n - self.dw + 1, self.xstep):
                D.append(image[i:i + self.dh, j:j + self.dw].flatten('F')) 
        D_array = np.array(D).T
        D_normalized = self.mat2gray(D_array)  

        
        Lambda = 1 / np.sqrt(max(m, n))
        A1, E1 = self.APG_IR(D_normalized, Lambda)

       
        AA = np.zeros((m, n, 100))
        EE = np.zeros((m, n, 100))

        index = 0
        C = np.zeros(image.shape)
        A_hat = np.zeros(image.shape)
        E_hat = np.zeros(image.shape)

        for i in range(0, m - self.dh + 1, self.ystep):
            for j in range(0, n - self.dw + 1, self.xstep):
                temp1 = E1[:, index].reshape((self.dw, self.dh)).T
                C[i:i + self.dh, j:j + self.dw] += 1  
                index += 1
                for ii in range(i, i + self.dh):
                    for jj in range(j, j + self.dw):
                        AA[ii, jj, int(C[ii, jj]) - 1] = temp1[ii - i, jj - j]
                        EE[ii, jj, int(C[ii, jj]) - 1] = temp1[ii - i, jj - j]

        for i in range(m):
            for j in range(n):
                if C[i, j] > 0:
                    A_hat[i, j] = np.median(AA[i, j, :int(C[i, j])])
                    E_hat[i, j] = np.median(EE[i, j, :int(C[i, j])])

        self._result = E_hat

    def APG_IR(self, D, Lambda):
        maxIter = 1e4
        tol = 1e-7
        lineSearchFlag = 0
        continuationFlag = 1
        eta = .9
        mu = 1e-3


        DISPLAY_EVERY = 20
        DISPLAY = 0

        m, n = D.shape
        t_k = 1
        t_km1 = 1
        tau_0 = 2  # square of Lipschitz constant for the RPCA problem

        X_km1_A = np.zeros(D.shape)
        X_km1_E = np.zeros(D.shape)  # X^{k-1} = (A^{k-1},E^{k-1})
        X_k_A = np.zeros(D.shape)
        X_k_E = np.zeros(D.shape)  # X^{k} = (A^{k},E^{k})

        U, s, V = np.linalg.svd(D, full_matrices=False)
        mu_k = s[1]
        mu_bar = .005 * s[3]
        tau_k = tau_0
        converged = 0
        numIter = 0
        NOChange_counter = 0
        pre_rank = 0
        pre_cardE = 0

        while not converged:
            Y_k_A = X_k_A + ((t_km1 - 1) / t_k) * (X_k_A - X_km1_A)
            Y_k_E = X_k_E + ((t_km1 - 1) / t_k) * (X_k_E - X_km1_E)
            G_k_A = Y_k_A - (1. / tau_k) * (Y_k_A + Y_k_E - D)
            G_k_E = Y_k_E - (1. / tau_k) * (Y_k_A + Y_k_E - D)

            U, s, V = np.linalg.svd(G_k_A, full_matrices=False)
            X_kp1_A = np.dot(np.dot(U, np.diag(self.pos(s - mu_k / tau_k))), V)
            X_kp1_E = np.sign(G_k_E) * self.pos(np.abs(G_k_E) - Lambda * mu_k / tau_k)

            rankA = np.sum(s > mu_k / tau_k)
            cardE = np.sum(np.sum((np.abs(X_kp1_E) > 0).astype(np.float32)))

            t_kp1 = 0.5 * (1 + np.sqrt(1 + 4 * t_k * t_k))
            temp = X_kp1_A + X_kp1_E - Y_k_A - Y_k_E
            S_kp1_A = tau_k * (Y_k_A - X_kp1_A) + temp
            S_kp1_E = tau_k * (Y_k_E - X_kp1_E) + temp

            norm_S = np.linalg.norm(
                np.concatenate((S_kp1_A, S_kp1_E), axis=1), ord='fro')
            norm_X = np.linalg.norm(
                np.concatenate((X_kp1_A, X_kp1_E), axis=1), ord='fro')
            stoppingCriterion = norm_S / (tau_k * max(1., norm_X))
            if stoppingCriterion <= tol:
                converged = 1
            if continuationFlag:
                mu_k = max(0.9 * mu_k, mu_bar)

            t_km1 = t_k
            t_k = t_kp1
            X_km1_A = X_k_A
            X_km1_E = X_k_E
            X_k_A = X_kp1_A
            X_k_E = X_kp1_E
            numIter += 1

           
            if pre_rank == rankA:
                NOChange_counter += 1
                if NOChange_counter > 10 and np.abs(cardE - pre_cardE) < 20:
                    converged = 1
            else:
                NOChange_counter = 0
                pre_cardE = cardE
            pre_rank = rankA
           
            if rankA > 0.3 * min(m, n):
                converged = 1
           
            if DISPLAY and numIter % DISPLAY_EVERY == 0:
                print('Iteration ', numIter, '  rank(A) ', rankA, ' ||E||_0 ', cardE)

            if numIter >= maxIter:
                print('Maximum iterations reached')
                converged = 1
        return X_k_A, X_k_E

    def pos(self, A):
        return A * (A > 0).astype(np.float32)
