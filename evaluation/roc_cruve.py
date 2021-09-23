import numpy as np
import cv2


class ROCMetric(object):
    def __init__(self, bins=100):
        self.bins = bins
        self.reset()

    def update(self, pred, label):
        pred = pred / np.max(pred) # normalize output to 0-1

        # analysis target number
        num_labels, labels, _, centroids = cv2.connectedComponentsWithStats(label.astype(np.uint8))
        assert num_labels > 1

        # get masks and update important parameters
        back_mask = labels == 0
        self.background_area += sum(back_mask)
        self.target_nums += (num_labels - 1)

        for ibin in range(self.bins + 1):
            thre = ibin / self.bins
            pred_binary = pred >= thre

            for t in range(1, num_labels):
                target_mask = labels == t
                self.true_detect[ibin] += sum(target_mask == pred_binary) > 0
                self.false_detect[ibin] += sum(back_mask == pred_binary)

    def get(self):
        fpr = self.false_detect / self.background_area  # X axis
        tpr = self.true_detect / self.target_nums       # Y axis
        return fpr, tpr

    def get_all(self):
        return self.false_detect, self.background_area, self.true_detect, self.target_nums

    def reset(self):
        self.false_detect = np.zeros(self.bins+1)
        self.true_detect = np.zeros(self.bins+1)
        self.background_area = 0
        self.target_nums = 0