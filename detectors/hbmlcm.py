from detectors.base import *


class HBMLCM(BaseDetector):
    '''
    Python implement of High-Boost-Based Multiscale Local Contrast Measure.

        Reference:
        ---------
        > Shi Y, Wei Y, Yao H, et al. High-boost-based multiscale local contrast measure for infrared small target
        > detection[J]. IEEE Geoscience and Remote Sensing Letters, 2017, 15(1): 33-37.
    '''
    def __init__(self, radius=None, ex_radius=7, high_boost_d = 5):
        super(HBMLCM, self).__init__()

        if radius is None:
            self.radius = [1, 2, 3, 4]
        self.ex_radius = ex_radius
        self.high_boost_d = high_boost_d

    def process(self, in_img):
        m, n = in_img.shape
        ex_r = self.ex_radius

        ihbf_img = self.high_boost(in_img)

        pad_radius = np.maximum(np.max(self.radius), self.ex_radius)
        pad_ihbfimg = cv2.copyMakeBorder(ihbf_img, pad_radius, pad_radius, pad_radius, pad_radius, cv2.BORDER_REPLICATE)
        rst = np.zeros((m, n))
        for i in range(m):
            for j in range(n):
                i_ind, j_ind = i + pad_radius, j + pad_radius

                patch_ex = pad_ihbfimg[i_ind-ex_r: i_ind+ex_r+1, j_ind-ex_r: j_ind+ex_r+1]
                dst = np.zeros((len(self.radius)))
                for ri in range(len(self.radius)):
                    r = self.radius[ri]
                    patch_in = pad_ihbfimg[i_ind-r: i_ind+r+1, j_ind-r: j_ind+r+1]
                    mt = np.mean(patch_in)
                    mb = (np.sum(patch_ex) - np.sum(patch_in)) / ((2*ex_r+1) ** 2 - (2*r+1) ** 2)
                    dst[ri] = np.abs(mt-mb)
                rst[i, j] = (np.max(dst) - np.min(dst)) ** 2
        self._result = rst

    def high_boost(self, in_img):
        d = self.high_boost_d
        filter = np.ones((d, d), dtype=np.float) / (d * d)

        mean_img = cv2.filter2D(in_img, ddepth=-1, kernel=filter, borderType=cv2.BORDER_REPLICATE)
        hp_img = in_img - mean_img
        hp_img = (hp_img > 0) * hp_img
        out_img = in_img * hp_img
        return out_img


