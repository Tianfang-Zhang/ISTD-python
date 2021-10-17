from detectors.base import *


class Tophat(BaseDetector):
    '''
    Python implement of Tophat method.

        Reference:
        ---------
        > Tom V T, Peli T, Leung M, et al. Morphology-based algorithm for point target detection in infrared
        > backgrounds[C]//Signal and Data Processing of Small Targets 1993.
        > International Society for Optics and Photonics, 1993, 1954: 2-11.
    '''
    def __init__(self, element_radius=2, morph=cv2.MORPH_RECT):
        super(Tophat, self).__init__()
        self.radius = element_radius
        self.morph = morph

    def process(self, in_img):
        d = 2 * self.radius + 1
        kernel = cv2.getStructuringElement(self.morph, (d, d))
        tophat_img = cv2.morphologyEx(in_img, cv2.MORPH_TOPHAT, kernel)
        self._result = tophat_img