from detectors.base import *


class FastSaliency(BaseDetector):
    '''
    Python implement of Fast Saliency method.

        Reference:
        ---------
        > Qi S, Xu G, Mou Z, et al. A fast-saliency method for real-time infrared small target detection[J].
        > Infrared Physics & Technology, 2016, 77: 440-450.
    '''
    def __init__(self):
        super(FastSaliency, self).__init__()

    def process(self, in_img):
        filter = np.array([[-4, -1, 0, -1, -4],
                           [-1, 2, 3, 2, -1],
                           [0, 3, 4, 3, 0],
                           [-1, 2, 3, 2, -1],
                           [-4, -1, 0, -1, -4]], dtype=np.int)
        rst = cv2.filter2D(in_img, ddepth=-1, kernel=filter, borderType=cv2.BORDER_DEFAULT)
        rst = rst ** 2

        rst = cv2.GaussianBlur(rst, [5, 5], 1.5)
        self._result = rst


