from evaluation.uploaded.base import *


class BSF(BaseEvaluator):
    def __init__(self):
        super(BSF, self).__init__()

    def update(self, org, preds, labels):
        org[np.where(labels > 0)] = -1
        preds[np.where(labels > 0)] = -1
        Cin = org[org > 0].std()
        Cout = preds[preds > 0].std()
        bsfi = Cin/Cout
        self.bsfouts = np.append(self.bsfouts, bsfi)

    def reset(self):
        self.bsfouts = np.array([])

    def get(self):
        return self.bsfouts[-1]

    def get_all(self):
        return np.mean(self.bsfouts)

