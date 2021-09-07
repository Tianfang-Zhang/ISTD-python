from .base import *


class LCM(BaseDetector):
    def __init__(self, radius=None):
        super(LCM, self).__init__()
        self.radius = [1, 2, 3, 4] if radius is None else radius

    def process(self, in_img):
        pass



