from detectors.base import *

import numpy as np
import math
import cv2


class PSTNN(BaseDetector):
    '''
    Python implement of PSTNN method.

        Reference:
        Zhang, L.; Peng, Z. Infrared Small Target Detection Based on Partial Sum of the Tensor Nuclear Norm.
        Remote Sens. 2019, 11, 382.
    '''

    def __init__(self, patchSize=40, slideStep=40, lambdaL=0.7):
        super(PSTNN, self).__init__()
        self.patchSize = patchSize
        self.slideStep = slideStep
        self.lambdaL = lambdaL

    def process(self, img):
        img = img.astype(np.float64)

        tenD = self.gen_patch_ten(img, self.patchSize, self.slideStep)
        n1, n2, n3 = tenD.shape

        lambda1, lambda2 = self.structure_tensor_lambda(img, 3)
        corner_strength = (lambda1 * lambda2) / (lambda1 + lambda2
                                                 + np.finfo(np.float64).eps)  # avoid divide 0
        lambda_max = np.array((lambda1, lambda2))
        lambda_max = lambda_max.max(axis=0)

        prior_weight = lambda_max * corner_strength
        _range = np.amax(prior_weight) - np.amin(prior_weight)
        prior_weight = (prior_weight - np.amin(prior_weight)) / _range
        tenW = self.gen_patch_ten(prior_weight, self.patchSize, self.slideStep)

        _lambda = self.lambdaL / math.sqrt(max(n1, n2) * n3)
        tenB, tenT = self.trpca_pstnn(tenD, _lambda, tenW)

        tarImg = self.res_patch_ten_mean(tenT, img, self.patchSize, self.slideStep)
        backImg = self.res_patch_ten_mean(tenB, img, self.patchSize, self.slideStep)

        def normalization(data):
            _range = np.max(data) - np.min(data)
            return (data - np.min(data)) / _range

        maxv = img.max()
        E = np.around(normalization(tarImg) * maxv).astype(np.uint8)
        A = np.around(normalization(backImg) * maxv).astype(np.uint8)

        self._result['target'] = E

    def gen_patch_ten(self, img, patchSize, slideStep):
        """Construct patch tensor of original image"""
        imgHei, imgWid = img.shape[0], img.shape[1]

        rowPatchNum = math.ceil((imgHei - patchSize) / slideStep) + 1
        colPatchNum = math.ceil((imgWid - patchSize) / slideStep) + 1
        rowPosArr = np.arange(0, (rowPatchNum - 1) * slideStep, slideStep)
        rowPosArr = np.append(rowPosArr, [imgHei - patchSize])
        colPosArr = np.arange(0, (colPatchNum - 1) * slideStep, slideStep)
        colPosArr = np.append(colPosArr, [imgWid - patchSize])

        patchTenList = []
        for i in colPosArr:
            for j in rowPosArr:
                patchTenList.append(img[j: j + patchSize, i: i + patchSize])
        patchTen = np.stack(patchTenList, axis=2)
        return patchTen

    def res_patch_ten_mean(self, patchTen, img, patchSize, slideStep):
        imgHei, imgWid = img.shape
        rowPatchNum = math.ceil((imgHei - patchSize) / slideStep) + 1
        colPatchNum = math.ceil((imgWid - patchSize) / slideStep) + 1
        rowPosArr = np.arange(0, (rowPatchNum - 1) * slideStep, slideStep)
        rowPosArr = np.append(rowPosArr, [imgHei - patchSize])
        colPosArr = np.arange(0, (colPatchNum - 1) * slideStep, slideStep)
        colPosArr = np.append(colPosArr, [imgWid - patchSize])

        # for-loop version
        accImg = np.zeros([imgHei, imgWid]).astype(np.float64)
        weiImg = np.zeros([imgHei, imgWid]).astype(np.float64)
        onesMat = np.ones([patchSize, patchSize]).astype(np.float64)

        k = 0
        for col in colPosArr:
            for row in rowPosArr:
                tmpPatch = np.reshape(patchTen[:, :, k], (patchSize, patchSize))
                accImg[row: row + patchSize, col: col + patchSize] = tmpPatch
                weiImg[row: row + patchSize, col: col + patchSize] = onesMat
                k += 1

        recImg = accImg / weiImg

        return recImg

    def structure_tensor_lambda(self, img, sz):
        """This function is to get the maximum 2 eigenvalues of the image matrix"""
        std = 2
        u = cv2.GaussianBlur(img, (sz, sz), std, borderType=cv2.BORDER_REFLECT)
        Gy, Gx = np.gradient(u)

        std = 9
        J_11 = cv2.GaussianBlur(np.square(Gx), (sz, sz), std, borderType=cv2.BORDER_REFLECT)
        J_12 = cv2.GaussianBlur(Gx * Gy, (sz, sz), std, borderType=cv2.BORDER_REFLECT)
        J_22 = cv2.GaussianBlur(np.square(Gy), (sz, sz), std, borderType=cv2.BORDER_REFLECT)

        # Discriminant delat
        """
        | (I_x(p))^2,    I_x(p)I_y(p) |
        | I_x(p)I_y(p),  (I_y(p))^2   |

        lambda1 + lamda2 = (I_x(p))^2 + (I_y(p))^2 
        lambda1 * lamda2 = 0
        so, that is to solve x^2 + (lambda1 + lamda2)x = 0
        """
        sqrt_delta = np.sqrt(np.square(J_11 - J_22) + 4 * np.square(J_12))
        lambda_1 = 0.5 * (J_11 + J_22 + sqrt_delta)
        lambda_2 = 0.5 * (J_11 + J_22 - sqrt_delta)

        return lambda_1, lambda_2

    def Unfold(self, X, dim):
        X_out = np.reshape(X, (dim, -1), order="F")

        return X_out

    def prox_pstnn(self, Y, N, mu):
        """Algorithm2"""
        _, _, n3 = Y.shape
        X = np.zeros_like(Y).astype(np.complex128)
        Y = np.fft.fft(Y, axis=2)
        tau = 1. / mu

        # first frontal slice
        U, S, V = np.linalg.svd(Y[:, :, 0], full_matrices=0)
        U1, S1, V1 = U[:, 0:int(N + 1)], S[0:int(N + 1)], V[0:int(N + 1), :]
        U2, S2, V2 = U[:, int(N + 1):], S[int(N + 1):], V[int(N + 1):, :]
        threshS2 = np.maximum(S2 - tau, 0)
        X[:, :, 0] = U1 @ np.diag(S1) @ (V1) + U2 @ np.diag(threshS2) @ (V2)

        # i = 2, 3, ..., halfn3
        half_n3 = round(n3 / 2)
        for i in range(1, half_n3):
            U, S, V = np.linalg.svd(Y[:, :, i], full_matrices=0)
            U1, S1, V1 = U[:, 0:int(N + 1)], S[0:int(N + 1)], V[0:int(N + 1), :]
            U2, S2, V2 = U[:, int(N + 1):], S[int(N + 1):], V[int(N + 1):, :]
            threshS2 = np.maximum(S2 - tau, 0)
            X[:, :, i] = U1 @ np.diag(S1) @ (V1) + U2 @ np.diag(threshS2) @ (V2)
            X[:, :, n3 - i] = X[:, :, i].conjugate()

        # if n3 is even
        if n3 % 2 == 0:
            i = half_n3
            U, S, V = np.linalg.svd(Y[:, :, i], full_matrices=0)
            U1, S1, V1 = U[:, 0:int(N + 1)], S[0:int(N + 1)], V[0:int(N + 1), :]
            U2, S2, V2 = U[:, int(N + 1):], S[int(N + 1):], V[int(N + 1):, :]
            threshS2 = np.maximum(S2 - tau, 0)
            X[:, :, i] = U1 @ np.diag(S1) @ (V1) + U2 @ np.diag(threshS2) @ (V2)
            X[:, :, n3 - i] = X[:, :, i].conjugate()

        return np.real(np.fft.ifft(X, axis=2))

    def prox_l1(self, b, _lambda):
        # equation 26
        x = np.maximum(0, b - _lambda) + np.minimum(0, b + _lambda)
        return np.maximum(x, 0)

    def trpca_pstnn(self, _X, _lambda, tenW):
        def rankN(X, ratioN):
            """
            To get the preserved target rank
            """
            dim = X.shape
            D = self.Unfold(X, dim[2])
            # got the eigen value of D in descending sort
            _, S, _ = np.linalg.svd(D, full_matrices=0)
            ratioVec = S / S[0]
            idxArr = np.argwhere(ratioVec < ratioN)
            return idxArr[0] - 1

        tol = 1e-3
        max_iter = 500
        rho = 1.05
        mu = 2e-3
        max_mu = 1e10
        DEBUG = 0
        N = rankN(_X, 0.1)  # To get the preserved target rank
        constant_c = 1. + N

        dim = np.array(_X.shape, dtype=np.uint8)  # the shape of tenD
        _L = np.zeros(dim).astype(np.float64)  # B
        _S = np.zeros(dim).astype(np.float64)  # T
        _Y = np.zeros(dim).astype(np.float64)
        weighten = np.ones(dim)

        for i in range(max_iter):
            preT = np.sum(_S > 0)

            # update _L
            _R = _S * (-1) + _X - _Y / mu
            _L = self.prox_pstnn(_R, N, mu)

            # update S
            _T = _L * (-1) + _X - _Y / mu  # equation 26
            _S = self.prox_l1(_T, weighten * _lambda / mu)  # part of equation 23
            weighten = constant_c / (np.abs(_S) + 0.01) / (tenW + np.finfo(np.float64).eps)
            # equation(20), to compute W_{sw}.
            # W_{rec} is the reciprocal of W_{p}, which is tenW

            dY = _L + _S - _X
            err = np.linalg.norm(dY.flatten(), 2) / np.linalg.norm(_X.flatten(), 2)
            currT = np.sum(_S > 0)
            if DEBUG:  # Check convergence rate
                print('iter {}, mu = {}, err = {}, |T|0 norm = {}'.format(i + 1, mu, err, currT))
            if (err < tol) or ((preT > 0) and (currT > 0) and (preT == currT)): break
            _Y = _Y + dY * mu  # Equation 27
            mu = np.minimum(rho * mu, max_mu)

        return _L, _S
