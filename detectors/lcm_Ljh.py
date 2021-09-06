from .base import *

class lcm(BaseDetector):
    def __init__(self, arg1, arg2):
        super(lcm, self).__init__()

        self.arg1 = arg1
        self.arg2 = arg2

    def process(self, in_img):
        N = [3, 5, 7, 9]
        [row, col] = in_img.shape
        # print(row)
        # print(col)
        h = np.size(N)
        # print(h)
        M = np.ones([np.size(N), row, col])
        # print(np.shape(M))
        for i in range(0, np.size(N) - 1, 1):
            mask = np.ones([N[i], N[i]])
            img = cv2.dilate(in_img, mask)
            img = img * img
            m1 = np.zeros([3 * N[i], 3 * N[i]])
            m2 = np.zeros([3 * N[i], 3 * N[i]])
            m3 = np.zeros([3 * N[i], 3 * N[i]])
            m4 = np.zeros([3 * N[i], 3 * N[i]])
            m5 = np.zeros([3 * N[i], 3 * N[i]])
            m6 = np.zeros([3 * N[i], 3 * N[i]])
            m7 = np.zeros([3 * N[i], 3 * N[i]])
            m8 = np.zeros([3 * N[i], 3 * N[i]])

            m1[0: N[i], 0: N[i]] = 1
            m2[0: N[i], N[i]: 2 * N[i]] = 1
            m3[0: N[i], 2 * N[i]: 3 * N[i]] = 1
            m4[N[i]: 2 * N[i], 2 * N[i]: 3 * N[i]] = 1
            m5[2 * N[i]: 3 * N[i], 2 * N[i]: 3 * N[i]] = 1
            m6[2 * N[i]: 3 * N[i], N[i]: 2 * N[i]] = 1
            m7[2 * N[i]: 3 * N[i], 0: N[i]] = 1
            m8[N[i]: 2 * N[i], 0: N[i]] = 1
            # print(m8)
            LCM = np.zeros([8, row, col])
            # print(np.shape(LCM))
            LCM[0] = cv2.filter2D(img, -1, kernel=m1 / np.sum(m1))
            LCM[1] = cv2.filter2D(img, -1, kernel=m1 / np.sum(m1))
            LCM[2] = cv2.filter2D(img, -1, kernel=m1 / np.sum(m1))
            LCM[3] = cv2.filter2D(img, -1, kernel=m1 / np.sum(m1))
            LCM[4] = cv2.filter2D(img, -1, kernel=m1 / np.sum(m1))
            LCM[5] = cv2.filter2D(img, -1, kernel=m1 / np.sum(m1))
            LCM[6] = cv2.filter2D(img, -1, kernel=m1 / np.sum(m1))
            LCM[7] = cv2.filter2D(img, -1, kernel=m1 / np.sum(m1))
            # print(np.shape(LCM))
            result = LCM.max(0)
            M[i] = img / result
        out = M.max(0)
        t = 0.5 * out.max()
        r, self._result = cv2.threshold(out, t, 255, cv2.THRESH_BINARY)


