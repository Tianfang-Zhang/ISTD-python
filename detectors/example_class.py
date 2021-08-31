from .base import *


class example_class(BaseDetector):
    def __init__(self, arg1, arg2):
        super(example_class, self).__init__()

        self.arg1 = arg1
        self.arg2 = arg2

    def process(self, in_img):
        filter = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
        self._result = cv2.filter2D(in_img, -1, kernel=filter)


