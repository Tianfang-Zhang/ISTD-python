from detectors.base import *


class HBLCM(BaseDetector):
    def __init__(self, targetsize):
        super(HBLCM, self).__init__()

        self.kernelsize = targetsize

    def process(self, in_image):
        m, n = in_image.shape
        # Improved High Boost Filter
        h = np.array([[1, 1, 1], [1, 2, 1], [1, 1, 1]]) / 10
        Im = cv2.filter2D(in_image, -1, h)
        Ihp = in_image - Im
        Ihp[Ihp < 0] = 0
        Ihb = in_image * Ihp

        # High-Boost-Based Multiscale Local Contrast
        b = np.empty((0, m*n)) 
        for i in self.kernelsize:
            c = self.localdiff(Ihb, i)  # c保存当前目标尺寸下调用localdiff得到的local contrast
            b = np.vstack((b, c.ravel()))  #  把c展开成行向量，然后按行进行拼接
        bmax = b.max(axis=0)
        bmin = b.min(axis=0)
        cmax = bmax.reshape(m, n)
        cmin = bmin.reshape(m, n)
        contrast = (cmax - cmin) ** 2
        self._result = contrast

    def localdiff(self, I, s):
        k = s // 2
        f1 = np.ones((s, s)) / (s ** 2)
        mT = cv2.filter2D(I, -1, f1)
        f2 = np.ones((11, 11))
        f2[5 - k: 6 + k, 5 - k: 6 + k] = 0
        f2 = f2 / (11 ** 2 - s ** 2)
        mB = cv2.filter2D(I, -1, f2)
        return mT - mB
