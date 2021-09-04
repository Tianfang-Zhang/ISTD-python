from .base import *


class FastSaliency(BaseDetector):
    def __init__(self, kerneltype):
        super(FastSaliency, self).__init__()

        self.hpkernel = kerneltype

    def process(self, in_img):
        # Gradient operation for highpass filtering
        if self.hpkernel == "laplacian":
            hpfilter = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
        elif self.hpkernel == "facet":
            hpfilter = np.array(
                [[-4, -1, 0, -1, -4], [-1, 2, 3, 2, -1], [0, 3, 4, 3, 0], [-1, 2, 3, 2, -1], [-4, -1, 0, -1, -4]])

        r = cv2.filter2D(in_img, -1, hpfilter)

        # Square computation for target enhancement.
        e = r ** 2

        # Gaussian smoothing for noise suppression.
        Gaussfilter = self.gaussian_kernel_2d(3, 1.5)

        self._result = cv2.filter2D(e, -1, Gaussfilter)

    def gaussian_kernel_2d(self, kernelsize, sigma):
        kx = cv2.getGaussianKernel(kernelsize, sigma)
        ky = cv2.getGaussianKernel(kernelsize, sigma)
        return np.multiply(kx, np.transpose(ky))


