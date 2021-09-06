from .base import *


class fast_saliency(BaseDetector):
    def __init__(self, arg1, arg2):
        super(fast_saliency, self).__init__()

        self.arg1 = arg1
        self.arg2 = arg2

    def process(self, in_img):
        # filter = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])#高通滤波模板1：拉普拉斯
        filter = np.array([[-4, -1, 0, -1, -4],
                           [-1, 2, 3, 2, -1],
                           [0, 3, 4, 3, 0],
                           [-1, 2, 3, 2, -1],
                           [-4, -1, 0, -1, -4]])  # 高通滤波模板2：论文给的
        self._result = cv2.filter2D(in_img, -1, kernel=filter)  # 高通滤波
        self._result = self._result * self._result  # 增强
        sigma = 1.5
        self._result = cv2.GaussianBlur(self._result, (3, 3), sigma)  # 高斯滤波
        t = 0.35 * self._result.max()  # 取阈值
        r, self._result = cv2.threshold(self._result, t, 255, cv2.THRESH_BINARY)
