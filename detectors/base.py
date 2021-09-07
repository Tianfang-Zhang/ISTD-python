from abc import ABCMeta, abstractmethod

import numpy as np
import matplotlib.pyplot as plt
import cv2


class BaseDetector(object):
    '''
    Basic class of infrared small target detectors
    '''

    def __init__(self):
        self._result = np.array([])

    @property
    def result(self):
        '''
        return the detection result

            Examples
            --------
            >> x.result
        '''
        return self._result

    @abstractmethod
    def process(self, in_img):
        '''
        specific process of the detector.

            Notes
            ------
            1. you have to rewrite this function and save the result to 'self._result'.
            2. there is no return value in this version.

            Examples
            --------
            >> x = Detector(args)
            >> x.process(in_img)
            >> x.result
        '''
        pass

