# from detectors.fast_saliency import FastSaliency
# from detectors_upload.LCM_lts import LCM
from detectors_upload.HBLCM_lts import HBLCM
from utils.datasets import *
from evaluation.uploaded.BSF_lts import *
from evaluation.uploaded.ROC_lts import *

if __name__ == '__main__':
    images = MDFA(base_dir="D:/ISTD-python-main/data/MDFA/")
    # images = SIRST(base_dir="D:/ISTD-python-main/data/sirst/")
    # detector = FastSaliency("facet")
    # detector = lcm(0, 0)
    detector = HBLCM([3, 5, 7, 9])

    evaluator = BSF()
    # evaluator = SCRG()
    # evaluator = ROC(0.01)

    for i in range(len(images)):
        imgorg, mask = images[i]
        detector.process(imgorg)
        imgpre = detector.result
        # evaluator.update(imgpre, mask) #ROC
        evaluator.update(imgorg, imgpre, mask)  # BSF/SCRG
        # print(evaluator.get())

    print(evaluator.get_all())  # BSF/SCRG
    # evaluator.get()  # ROC
    plt.show()
