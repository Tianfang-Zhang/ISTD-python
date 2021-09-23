from detectors_upload.FastSaliency_lts import FastSaliency
from evaluation.uploaded.scrg_ljh import Scrg
from utils.datasets import *

if __name__ == '__main__':
    images = MDFA(base_dir="C:/image/MDFA/")
    # images = SIRST()
    detector = FastSaliency("facet")
    for i in range(len(images)):
        imgin, mask = images[i]
        detector.process(imgin)
        imgout = detector.result
        Evaluation1=Scrg()
        Evaluation1.update(imgin,mask)
        s1=Evaluation1.get()
        Evaluation2=Scrg()
        Evaluation2.update(imgout,mask)
        s2=Evaluation2.get()
        SCRG=s2/s1
        print("第%d张图的SCRG值为"%(i+1),SCRG)


