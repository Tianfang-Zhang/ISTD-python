from detectors.base import *


class IPI(BaseDetector):
    '''
    Python implement of Infrared Patch Image method.

        Reference:
        ---------
        > Gao C, Meng D, Yang Y, et al. Infrared patch-image model for small target detection in a single image[J].
        > IEEE transactions on image processing, 2013, 22(12): 4996-5009.
    '''
    def __init__(self, length=30, step=10):
        super(IPI, self).__init__()
        self.length = length
        self.step = step

    def process(self, in_img):
        m, n = in_img.shape
        patch_img = self.image2patch(in_img, self.length, self.step)

        lambda_ = 1 / np.sqrt(np.maximum(m, n))
        B, T, loss = self.optimization_admm(patch_img, lambda_)

        # rstB = self.patch2image(B, self.length, self.step, (m, n))
        rstT = self.patch2image(T, self.length, self.step, (m, n))
        self._result = rstT * (rstT > 0)

    def image2patch(self, in_img, length, step):
        m, n = in_img.shape
        index_i = np.arange(0, m-length+1, step)
        index_j = np.arange(0, n-length+1, step)
        patch_img = np.zeros((length*length, len(index_i)*len(index_j)))
        counter = 0
        for i in index_i:
            for j in index_j:
                patch = in_img[i:i+length, j:j+length]
                patch_img[:, counter] = patch.reshape((-1))
                counter += 1
        return patch_img

    def patch2image(self, patch_img, length, step, image_shape):
        m, n = image_shape

        recons = np.zeros((m, n, 100))
        count_mat = np.zeros((m, n), dtype=np.int)
        index = 0

        for i in np.arange(0, m-length+1, step):
            for j in np.arange(0, n-length+1, step):
                # Count the time each pixel used and record the value
                repatch = patch_img[:, index].reshape((length, length))
                count_mat[i: i+length, j: j+length] = count_mat[i: i+length, j: j+length] + 1

                # Record the value of each pixel
                for ii in np.arange(i, i+length):
                    for jj in np.arange(j, j+length):
                        recons[ii, jj, count_mat[ii, jj]] = repatch[ii-i, jj-j]

                index += 1

        image = np.zeros((m, n))
        for i in range(m):
            for j in range(n):
                if count_mat[i, j] > 0:
                    vec = recons[i, j, 0:count_mat[i, j]]
                    image[i, j] = np.mean(vec)
        return image

    def SoftThresholding(self, img, epsilon):
        return np.sign(img) * np.maximum(np.abs(img) - epsilon, 0)

    def SingularValueShrinkage(self, img, epsilon):
        U, S, Vt = np.linalg.svd(img, full_matrices=False)
        diag_S = np.zeros((len(S), len(S)), dtype=np.float64)
        for i in range(S.shape[0]):
            diag_S[i,i] = S[i]
        return np.linalg.multi_dot([U, self.SoftThresholding(diag_S, epsilon), Vt])

    def optimization_admm(self, D, lambda_):
        # Parameters setting
        B_k, B_kp1 = D, D
        T_k, T_kp1 = np.zeros(D.shape), np.zeros(D.shape)
        Y_k, Y_kp1 = np.zeros(D.shape), np.zeros(D.shape)
        rho_k = 1 / (5 * np.std(D))

        iter_num = 0
        norm_D = np.linalg.norm(D, 'fro')
        CONVERGED = False
        loss = []

        # Iteration step
        while not CONVERGED:
            # Update B
            B_kp1 = self.SingularValueShrinkage(D + Y_k/rho_k - T_k, 1/rho_k)

            # Update T
            tmp = D + Y_k/rho_k - B_kp1
            T_kp1 = self.SoftThresholding(tmp * (tmp > 0), lambda_/rho_k)

            # Update Y
            Y_kp1 = Y_k + rho_k*(D - B_kp1 - T_kp1)

            rho_kp1 = rho_k * 1.5

            # Judge converged
            iter_num += 1
            Criterion = np.linalg.norm(D - B_kp1 - T_kp1, 'fro') / norm_D
            loss.append(Criterion)

            nonzero_num_k = np.sum(T_k != 0)
            nonzero_num_kp1 = np.sum(T_kp1 != 0)

            if Criterion < 1e-7 or nonzero_num_k == nonzero_num_kp1:
                CONVERGED = True

            # Disp the status
            # print('Iteration Number: %d, loss: %f' % (iter_num, Criterion))
            # print('Nonzero Number K: %d, Kp1: %d' % (nonzero_num_k, nonzero_num_kp1))
            # print('')

            # Assignment to continue
            B_k, T_k = B_kp1, T_kp1
            Y_k, rho_k = Y_kp1, rho_kp1

        return B_k, T_k, loss







