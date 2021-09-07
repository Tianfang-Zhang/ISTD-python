from detectors.base import *


class HB_MLCM(BaseDetector):
    def __init__(self, arg1, arg2):
        super(HB_MLCM, self).__init__()

        self.arg1 = arg1
        self.arg2 = arg2

    def process(self, in_img):
        h = np.ones([9, 9]) / 81
        # print(h)
        i_smooth = cv2.filter2D(in_img, -1, kernel=h)
        i_hp = in_img - i_smooth
        i_hp[i_hp < 0] = 0
        img = in_img * i_hp
        # cv2.imshow("IHBF",i)
        # cv2.waitKey(0) #等待按键

        k = 4
        [row, col] = in_img.shape
        d = np.zeros((k, row, col))
        # print(np.size(d))
        for i in range(1, k):
            t = np.ones([2 * i + 1, 2 * i + 1]) / ((2 * i + 1) * (2 * i + 1))
            r = np.floor((2 * i + 1) / 2)
            b = np.ones([15, 15])
            b[int(8 - r):int(8 + r), int(8 - r):int(8 + r)] = 0
            b = b / np.sum(b)
            # print(b)
            mt = cv2.filter2D(img, -1, t)
            mb = cv2.filter2D(img, -1, b)
            # print(np.shape(mt-mb))
            d[i - 1, :, :] = mt - mb
        # print(d[1])
        # print(np.shape(d[1]))
        d = np.abs(d)
        d_min = np.min(d, 0)
        d_max = np.max(d, 0)
        out = (d_max - d_min) * (d_max - d_min)
        print(np.shape(out))
        t = 0.5 * out.max()
        r, self._result = cv2.threshold(out, t, 255, cv2.THRESH_BINARY)