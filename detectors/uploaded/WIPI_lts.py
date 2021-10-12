from detectors.base import *


class WIPI(BaseDetector):
    def __init__(self):
        super(WIPI, self).__init__()
        self.options = {'dw': 50, 'dh': 50, 'x_step': 10, 'y_step': 10}

    def mat2gray(self, image):
        return (image - np.min(image)) / np.ptp(image)

    def process(self, image):
        m, n = image.shape

        """
        Compute steering matrices PARAMETERS
        zx, zy : image gradients along x and y directions
        size: the size of local patch
        mu1, mu2 : regularization parameter
        """
        mu1 = 1
        mu2 = 1

        # 构造块图像
        D = []
        Lambda = []
        for i in range(0, m - self.options['dh'] + 1, self.options['y_step']):
            for j in range(0, n - self.options['dw'] + 1, self.options['x_step']):
                tempD = image[i:i + self.options['dh'], j:j + self.options['dw']]
                gx, gy = self.derivative7(tempD)  # 1st derivative in x and y
                Lambdai = self.steering(gx, gy, self.options['dh'] * self.options['dw'], mu1, mu2)
                Lambda.append(Lambdai)
                D.append(tempD.flatten('F'))  # 'F'按列展开
        D_array = np.array(D).T
        Lambda_array = np.array(Lambda)
        D_normalized = self.mat2gray(D_array)  # 块图像归一化

        # 用ADM算法从D中分解出目标图像E1和背景图像A1
        A1, E1 = self.ADM_IR(D_normalized, Lambda_array)

        # 块图像重构目标图像E_hat
        # AA = np.zeros((m, n, 100))
        EE = np.zeros((m, n, 100))

        index = 0
        C = np.zeros(image.shape)
        # A_hat = np.zeros(image.shape)
        E_hat = np.zeros(image.shape)

        for i in range(0, m - self.options['dh'] + 1, self.options['y_step']):
            for j in range(0, n - self.options['dw'] + 1, self.options['x_step']):
                # temp = A1[:, index].reshape((self.options['dw'], self.options['dh'])).T
                temp1 = E1[:, index].reshape((self.options['dw'], self.options['dh'])).T
                C[i:i + self.options['dh'], j:j + self.options['dw']] += 1  # 记录每个像素点重叠的次数（被滑动窗口遍历的次数）
                index += 1
                for ii in range(i, i + self.options['dh']):
                    for jj in range(j, j + self.options['dw']):
                        # AA[ii, jj, int(C[ii, jj]) - 1] = temp[ii - i, jj - j]
                        EE[ii, jj, int(C[ii, jj]) - 1] = temp1[ii - i, jj - j]

        for i in range(m):
            for j in range(n):
                if C[i, j] > 0:
                    # A_hat[i, j] = np.median(AA[i, j, :int(C[i, j])])
                    E_hat[i, j] = np.median(EE[i, j, :int(C[i, j])])

        self._result = E_hat

    def ADM_IR(self, D, Lambda):
        m, n = D.shape

        tol = 1e-7
        maxIter = 100

        # initialize
        Y = D
        uY, sY, vY = np.linalg.svd(np.dot(Y, Y.T))
        norm_two = np.sqrt(max(sY))
        Q = Y.flatten('F')
        norm_inf = np.linalg.norm(Q, ord=np.inf, axis=0) * np.sqrt(min(m, n))
        dual_norm = max(norm_two, norm_inf)
        Y = Y / dual_norm

        hatA = np.zeros((m, n))
        hatE = np.zeros((m, n))
        mu = 1.25 / norm_two  # this one can be tuned
        muBar = mu * 1e7
        rho = 1.5  # this one can be tuned
        normD = np.linalg.norm(D)

        iter = 0
        converged = 0

        while not converged:
            iter = iter + 1

            # Target component T
            tempT = D - hatA + (1 / mu) * Y
            for i in range(n):
                tempQ = tempT[:, i] - Lambda[i] / mu
                for j in range(m):
                    if tempQ[j] > 0:
                        hatE[j, i] = tempQ[j]

            # Background component B
            U, S, V = np.linalg.svd(D - hatE + (1 / mu) * Y, full_matrices=False)
            S = S - 1 / mu
            S[np.where(S < 0)] = 0
            hatA = np.dot(np.dot(U, np.diag(S)), V.T)

            # Lagrange multiplier
            Z = D - hatA - hatE
            Y = Y + mu * Z
            mu = min(mu * rho, muBar)

            # stop Criterion
            stopC = np.linalg.norm(Z) / normD
            if stopC < tol or iter == maxIter:
                converged = 1

        return hatA, hatE

    def derivative7(self, im):
        """
        This function computes 1st and 2nd derivatives of an image using the 7-tap
        coefficients given by Farid and Simoncelli.The results are significantly
        more accurate than MATLAB's GRADIENT function on edges that are at angles
        other than vertical or horizontal. This in turn improves gradient orientation
        estimation enormously.
        """
        # 7 - tap interpolant and 1st and 2nd derivative coefficients
        p = [0.004711, 0.069321, 0.245410, 0.361117, 0.245410, 0.069321, 0.004711]
        d1 = [0.018708, 0.125376, 0.193091, 0.000000, -0.193091, -0.125376, -0.018708]
        d2 = [0.055336, 0.137778, -0.056554, - 0.273118, - 0.056554, 0.137778, 0.055336]

        gx = self.myconv2(p, d1, im, 'same')
        gy = self.myconv2(d1, p, im, 'same')

        return gx, gy

    def myconv2(self, v1, v2, m, mode='same'):
        """
        Two-dimensional convolution of matrix m by vectors v1 and v2

        First convolves each column of 'm' with the vector 'v1'
        and then it convolves each row of the result with the vector 'v2'.

        """
        tmp = np.apply_along_axis(np.convolve, 0, m, v1, mode)
        return np.apply_along_axis(np.convolve, 1, tmp, v2, mode)

    def steering(self, zx, zy, size, mu1, mu2):
        """
        Compute steering matrices PARAMETERS
        zx, zy : image gradients along x and y directions
        size: the size of local patch
        mu1, mu2 : regularization parameter
        """
        G = []
        G.append(zx.flatten('F'))
        G.append(zy.flatten('F'))
        G_array = np.array(G).T

        U, s, V = np.linalg.svd(G_array, full_matrices=False)
        sigma = (s[0] + mu1) / (s[1] + mu1)
        gamma = np.sqrt((s[0] * s[1] + mu2) / size)

        Lambdai = sigma * gamma
        return Lambdai
