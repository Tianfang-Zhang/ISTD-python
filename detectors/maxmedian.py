from detectors.base import *


class MaxMedian(BaseDetector):
    def __init__(self, radius=7):
        super(MaxMedian, self).__init__()
        self.radius = radius

    def process(self, in_img):
        m, n = in_img.shape
        r = self.radius
        pad_radius = self.radius

        pad_img = cv2.copyMakeBorder(in_img, pad_radius, pad_radius, pad_radius, pad_radius, cv2.BORDER_REPLICATE)
        med_img = np.zeros((m, n))
        z = np.zeros((4))

        for i in range(m):
            for j in range(n):
                i_ind, j_ind = i + pad_radius, j + pad_radius
                patch = pad_img[i_ind-r: i_ind+r+1, j_ind-r: j_ind+r+1]
                z[0] = np.median(patch[:, r])
                z[1] = np.median(patch[r, :])
                z[2] = np.median(np.diag(patch))
                z[2] = np.median(np.diag(np.rot90(patch)))

                med_img[i, j] = np.max(z)

        rst = in_img - med_img
        self._result = rst * (rst > 0)

