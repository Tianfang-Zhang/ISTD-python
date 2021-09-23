import cv2
import matplotlib.pyplot as plt
import numpy as np

from .base import *
class Roc(BaseEvaluator):
    def __init__(self):
        super(Roc, self).__init__()


    def update(self, preds, labels):
        self.preds = preds
        self.labels = labels

    def get_all(self):
        FPR=np.zeros(100)
        TPR=np.zeros(100)
        for i in range(100):
            t=0.01*i*np.max(self.preds)
            ret, mask = cv2.threshold(self.preds, t, 1, cv2.THRESH_BINARY)
            FPR[i]=np.mean(np.maximum(0,mask-self.labels))
            TPR[i]=np.sum(mask*self.labels)/np.maximum(np.sum(self.labels),1)
        # axF=np.empty((0,100))
        # axT = np.empty((0, 100))
        # axF=np.vstack((axF,FPR))
        # axT=np.vstack((axT,TPR))
        # FPR = (np.mean(axF, axis=0) - np.mean(axF, axis=0).min()) / (np.mean(axF, axis=0).max() - np.mean(axF, axis=0).min())
        # TPR = (np.mean(axT, axis=0) - np.mean(axT, axis=0).min()) / (np.mean(axT, axis=0).max() - np.mean(axT, axis=0).min())
        # plt.figure()
        # plt.plot(FPR,TPR)
        auc=0
        for i in range(99):
            auc=auc+(FPR[i]-FPR[i+1])*(TPR[i]*TPR[i+1])

        return FPR,TPR,auc