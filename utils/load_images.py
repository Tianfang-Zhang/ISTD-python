import numpy as np
import matplotlib.pyplot as plt
import cv2


def load_image(srcpath):
    img = cv2.imread(srcpath)
    if img.ndim == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img / 255
    return img
