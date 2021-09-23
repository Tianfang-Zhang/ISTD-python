from detectors_upload.FastSaliency_lts import FastSaliency
from evaluation.uploaded.bsf_ljh import Bsf
from utils.datasets import *

if __name__ == '__main__':
    images = MDFA(base_dir="C:/image/MDFA/")
    # images = SIRST()
    detector = FastSaliency("facet")
    for i in range(len(images)):
        imgin, mask = images[i]
        detector.process(imgin)
        imgout = detector.result
        Evaluation1=Bsf()
        Evaluation1.update(imgin,imgout)
        BSF=Evaluation1.get()
        print("第%d张图的BSF值为"%(i+1),BSF)

