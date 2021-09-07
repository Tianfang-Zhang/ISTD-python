from detectors.base import *


class LCM(BaseDetector):
    def __init__(self, targetsize):
        super(LCM, self).__init__()

        self.kernelsize = targetsize

    def process(self, in_image):
        m, n = in_image.shape
        b = np.empty((0, m * n))
        # Multiscale Local Contrast
        for i in self.kernelsize:
            c = self.localcontrast(in_image, i)  # c保存当前目标尺寸下调用localcontrast
            b = np.vstack((b, c.ravel()))  # 把c展开成行向量，然后按行进行拼接
        bmax = b.max(axis=0)
        cmax = bmax.reshape(m, n)
        self._result = cmax

    def localcontrast(self, I, s):
        p, q = I.shape
        f1 = np.ones((s, s)) / (s ** 2)
        m = cv2.filter2D(I, -1, f1)  # 计算每个cell的均值
        L = self.maxfilter(I, s, p, q)  # 计算中心cell的最大灰度值 最大值滤波：默认边界填充为0， 返回与I大小一样的Imax
        tempc = np.zeros((1, 8))  # 用来存放该尺度下八个方向上的局部对比度
        C = np.zeros((p, q))  # 用来存放该尺度下每个像素点局部对比度
        mb = cv2.copyMakeBorder(m, 1, 1, 1, 1, cv2.BORDER_REPLICATE)
        Lb = cv2.copyMakeBorder(L, 1, 1, 1, 1, cv2.BORDER_REPLICATE)  # 默认复制填充
        for a in range(1, p + 1):  # 因为边界填充所以下标改变
            for b in range(1, q + 1):
                tempc[0, 0] = Lb[a, b] ** 2 / mb[a - 1, b - 1]
                tempc[0, 1] = Lb[a, b] ** 2 / mb[a - 1, b]
                tempc[0, 2] = Lb[a, b] ** 2 / mb[a - 1, b + 1]
                tempc[0, 3] = Lb[a, b] ** 2 / mb[a, b - 1]
                tempc[0, 4] = Lb[a, b] ** 2 / mb[a, b + 1]
                tempc[0, 5] = Lb[a, b] ** 2 / mb[a + 1, b - 1]
                tempc[0, 6] = Lb[a, b] ** 2 / mb[a + 1, b]
                tempc[0, 7] = Lb[a, b] ** 2 / mb[a + 1, b + 1]
                C[a-1, b-1] = tempc.min()
        return C

    def maxfilter(self, I, s, p, q):
        k = s // 2
        Ib = cv2.copyMakeBorder(I, k, k, k, k, cv2.BORDER_CONSTANT)
        Imax = np.zeros((p, q))
        for m in range(k, p+k):
            for n in range(k, q+k):
                tempmax = Ib[m - k:m + k + 1, n - k:n + k + 1]
                Imax[m-k, n-k] = tempmax.max()
        return Imax
