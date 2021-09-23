from evaluation.uploaded.base import *
import matplotlib.pyplot as plt


class ROC(BaseEvaluator):
    def __init__(self, step):
        super(ROC, self).__init__()
        self.step = step
        self.far = np.empty((0, int(1 / self.step)))
        self.tpr = np.empty((0, int(1 / self.step)))

    def update(self, preds, labels):
        maxpreds = preds.max()
        tempfar = np.array([])  # 用于存放该图像在不同的阈值下的FAR
        temptpr = np.array([])  # 用于存放该图像在不同的阈值下的TPR

        for i in np.arange(0, 1, self.step):
            bnpreds = np.where(preds > maxpreds * i, 1, 0)

            fari = np.mean(np.maximum(0, bnpreds - labels))
            tempfar = np.append(tempfar, fari)

            tpri = np.sum(bnpreds * labels) / np.maximum(np.sum(labels), 1)
            temptpr = np.append(temptpr, tpri)

        self.far = np.vstack((self.far, tempfar))
        self.tpr = np.vstack((self.tpr, temptpr))  # axis = 1不同阈值， axis = 0纵坐标不同图像

    def reset(self):
        self.far = np.array([])  # 此处遗留一点小问题：reset没有发挥用处
        self.tpr = np.array([])
        self.AUC = 0

    def get(self):
        self.avefar = np.mean(self.far, axis=0)
        self.avetpr = np.mean(self.tpr, axis=0)
        self.avefar = (self.avefar - self.avefar.min()) / (self.avefar.max() - self.avefar.min())
        self.avetpr = (self.avetpr - self.avetpr.min()) / (self.avetpr.max() - self.avetpr.min())

        plt.figure()
        plt.axis([0, 1, 0, 1])
        plt.xlabel("FAR")
        plt.ylabel("TPR")
        plt.title("ROC")
        plt.plot(self.avefar, self.avetpr)
        
    def get_AUC(self):
        for i in range(len(self.avetpr)-1):
            self.AUC = self.AUC + 0.5 * (self.avetpr[i+1] + self.avetpr[i]) * (self.avefar[i] - self.avefar[i+1])
        return self.AUC
