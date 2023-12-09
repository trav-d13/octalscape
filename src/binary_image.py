import cv2
from matplotlib import pyplot as plt
import numpy as np


def read_image(path: str):
    img = cv2.imread(path)
    return img


def resize_image(height: int, width: int, image: np.matrix):
    resized = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
    return resized


def prepare_image_for_edge_detection(image: np.matrix):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    return img_blur


def detect_edges(image: np.matrix):
    prep_image = prepare_image_for_edge_detection(image)
    block_size = 9
    c = 7
    edges = cv2.adaptiveThreshold(prep_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c)
    return edges


def prepare_output_matrix(edges: np.matrix):
    # invert_image = 255 - edges  # Invert image so black lines become 255 values
    inverted_scale = edges / 255  # Scale 255 values to zero
    return inverted_scale


def save_output_matrix(template_matrix: np.matrix, file_name: str):
    save_path = '../images/matrix_templates/' + file_name
    np.savetxt(save_path, template_matrix, fmt='%d', delimiter='')

def display_image(image: np.array, name: str):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

