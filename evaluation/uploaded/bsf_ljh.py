import numpy as np

from .base import *
class Bsf(BaseEvaluator):
    def __init__(self):
        super(Bsf, self).__init__()

    def update(self, preds, labels):
        self.preds = preds
        self.labels = labels

    def get(self):
        r=np.std(self.preds)/np.std(self.labels)
        return r