from abc import ABCMeta, abstractmethod

import numpy as np
import matplotlib.pyplot as plt
import cv2


class BaseDetector(object):
    '''
    Basic class of infrared small target detectors
    '''

    def __init__(self):
        '''
        Init function.

            Notes
            ------
            1. self._result is Python dict, which key 'rst' is required.
            2. dict value of each key must be Numpy Array.
            3. you can customize your unique output, such as other coefficient matrix.
            ------
        '''
        self._result = {'target': np.array([]),
                        'background': np.array([]),
                        'coefficient': np.array([])}

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

