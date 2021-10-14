from detectors.base import *


class LCM(BaseDetector):
    '''
    Python implement of Local Contrast Method.

        Reference:
        ---------
        > Chen C L P, Li H, Wei Y, et al. A local contrast method for small infrared target detection[J].
        > IEEE transactions on geoscience and remote sensing, 2013, 52(1): 574-581.
    '''
    def __init__(self, radius=None):
        super(LCM, self).__init__()
        self.radius = [1, 2, 3, 4] if radius is None else radius

    def process(self, in_img):
        m, n = in_img.shape
        pad_radius = 3* np.max(self.radius) + 1
        pad_img = cv2.copyMakeBorder(in_img, pad_radius, pad_radius, pad_radius, pad_radius, cv2.BORDER_REPLICATE)

        masks_all = self.make_mask()
        C = np.zeros((len(self.radius)))
        rst = np.zeros((m, n))
        for i in range(m):
            for j in range(n):
                i_ind, j_ind = i + pad_radius, j + pad_radius

                for r_i in range(len(self.radius)):
                    r = self.radius[r_i]
                    R = 3 * r + 1
                    patch = pad_img[i_ind - R:i_ind + R + 1, j_ind - R:j_ind + R + 1]

                    masks = masks_all[r_i]
                    means = np.zeros((8))
                    for m in range(8):
                        means[m] = np.mean(patch[masks[:, :, m]])

                    L = np.max(patch[masks[:, :, -1]])

                    C[r_i] = np.min(L ** 2 / means)
                rst[i, j] = np.max(C)

        self._result = rst

    def make_mask(self):
        masks_all = []
        for r in self.radius:
            d = 2 * r + 1
            masks = np.zeros((3*d, 3*d, 9), dtype=np.bool)
            masks[0:d, 0:d, 0] = True
            masks[0:d, d:2*d, 1] = True
            masks[0:d, 2*d:3*d, 2] = True
            masks[d:2*d, 0:d, 3] = True
            masks[d:2*d, 2*d:3*d, 4] = True
            masks[2*d:3*d, 0:d, 5] = True
            masks[2*d:3*d, d:2*d, 6] = True
            masks[2*d:3*d, 2*d:3*d, 7] = True
            masks[d:2*d, d:2*d, 8] = True

            masks_all.append(masks)
        return masks_all





