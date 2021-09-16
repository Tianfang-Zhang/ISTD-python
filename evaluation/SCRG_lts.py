from evaluation.base import *


class SCRG(BaseEvaluator):
    def __init__(self):
        super(SCRG, self).__init__()

    def update(self, org, preds, labels):
        temorg = org.copy()
        tempreds = preds.copy()

        temorg[np.where(labels == 0)] = -1
        tempreds[np.where(labels == 0)] = -1  # 用于把目标区域提取出来
        org[np.where(labels == 1)] = -1
        preds[np.where(labels == 1)] = -1  # 用于把背景区域提取出来

        Cin = org[org > 0].std()  # 背景杂波：背景标准差
        Sin = temorg[temorg > 0].mean() - org[org > 0].mean()  # 信号幅值:输入图像的目标均值减去背景均值
        Cout = preds[preds > 0].std()
        Sout = tempreds[tempreds > 0].mean() - preds[preds > 0].mean()  # 输出图像的目标均值减去背景均值

        scrg = (Sout/Cout)/(Sin/Cin)
        self.scrgouts = np.append(self.scrgouts, scrg)

    def reset(self):
        self.scrgouts = np.array([])

    def get(self):
        return self.scrgouts[-1]

    def get_all(self):
        return self.scrgouts
