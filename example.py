from utils.images import *
from detectors.fast_saliency import FastSaliency
from detectors_upload.lcm_Ljh import lcm

if __name__ == '__main__':
    img = load_image('./data/1.bmp')

    detector = lcm(0, 0)
    detector.process(img)
    show_image(detector.result)

    plt.show()

