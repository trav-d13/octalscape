import cv2
from matplotlib import pyplot as plt
import numpy as np


def read_image(path: str):
    img = cv2.imread(path)
    return img


def display_image(image: np.array, name: str):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

