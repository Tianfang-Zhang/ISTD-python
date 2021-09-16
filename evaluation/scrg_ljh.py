from .base import *
class Scrg(BaseEvaluator):
    def __init__(self):
        super(Scrg, self).__init__()

    def update(self, preds, labels):
        # t=preds*labels
        # b=preds*(1-labels)
        self.preds=preds
        self.labels=labels

    def get(self):
        t = self.preds * self.labels#目标
        b=self.preds*(1-self.labels)#背景
        r=np.abs(((np.sum(t)/np.sum(self.labels))-(np.sum(b)/np.sum(1-self.labels)))/np.std(b))

        return r



