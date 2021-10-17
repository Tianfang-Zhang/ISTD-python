from detectors.base import *


class MPCM(BaseDetector):
    '''
    Python implement of Multiscale Patch-based Contrast Measure.

        Reference:
        ---------
        > Wei Y, You X, Li H. Multiscale patch-based contrast measure for small infrared target detection[J].
        > Pattern Recognition, 2016, 58: 216-226.
    '''
    def __init__(self, radius=None):
        super(MPCM, self).__init__()
        if radius is None:
            radius = [1, 2, 3, 4]
        self.radius = radius

    def process(self, in_img):
        m, n = in_img.shape
        rst_imgs = []

        for i in range(len(self.radius)):
            r_in = self.radius[i]
            d_in = 2 * r_in + 1
            rst_filters = []

            # mean filtering
            mean_filter = np.ones((d_in, d_in)) / (d_in ** 2)
            mean_img = cv2.filter2D(in_img, ddepth=-1, kernel=mean_filter, borderType=cv2.BORDER_REPLICATE)

            # construct filters
            filters = self.construct_filters(r_in)
            for k in range(8):  # filtering
                f = filters[:, :, k]

                tmp = cv2.filter2D(mean_img, ddepth=-1, kernel=f, borderType=cv2.BORDER_REPLICATE)
                rst_filters.append(tmp)

            cs = np.zeros((m, n, 4))
            cs[:, :, 0] = rst_filters[0] * rst_filters[4]
            cs[:, :, 1] = rst_filters[1] * rst_filters[5]
            cs[:, :, 2] = rst_filters[2] * rst_filters[6]
            cs[:, :, 3] = rst_filters[3] * rst_filters[7]

            rst_imgs.append(np.min(cs, axis=2))

        rst_imgs = np.array(rst_imgs)
        rst = np.max(rst_imgs, axis=0)
        self._result = rst * (rst > 0)

    def construct_filters(self, r_in):
        d_in = 2 * r_in + 1
        d_ex = 3 * d_in
        filters = np.zeros((d_ex, d_ex, 8), dtype=np.float)
        filters[r_in + d_in, r_in + d_in, :] = 1

        filters[r_in, r_in, 0] = -1
        filters[r_in, r_in + d_in, 1] = -1
        filters[r_in, r_in + 2 * d_in, 2] = -1
        filters[r_in + d_in, r_in + 2 * d_in, 3] = -1
        filters[r_in + 2 * d_in, r_in + 2 * d_in, 4] = -1
        filters[r_in + 2 * d_in, r_in + d_in, 5] = -1
        filters[r_in + 2 * d_in, r_in, 6] = -1
        filters[r_in + d_in, r_in, 7] = -1
        return filters