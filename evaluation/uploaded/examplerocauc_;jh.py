import numpy as np
from matplotlib import pyplot as plt

from detectors_upload.FastSaliency_lts import FastSaliency
from evaluation.uploaded.rocauc_ljh import Roc
from utils.datasets import *

if __name__ == '__main__':
    images = MDFA(base_dir="C:/image/MDFA/")
    # images = SIRST()
    detector = FastSaliency("facet")


    tp=np.zeros(len(images))
    fp=np.zeros(len(images))
    for i in range(2):
        imgin, mask = images[i]
        detector.process(imgin)
        imgout = detector.result
        Evalution=Roc()
        Evalution.update(imgout,mask)
        X,Y,auc=Evalution.get_all()
        # print(fp[i],tp[i])
        plt.axis([0, 1, 0, 1])
        plt.xlabel("FAR")
        plt.ylabel("TPR")
        plt.title("ROC")
        plt.plot(X, Y)
        print("第%d张图的AUC值为"%(i+1),auc)
        plt.legend()
        plt.show()


    # plt.plot(np.sort(fp), np.sort(tp), marker='o', mec='r', mfc='w', label=u'roc')
    # plt.legend()
    # plt.show()

