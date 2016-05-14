
import cv2
from matplotlib import pyplot as plt


class Image:

    def __init__(self):
        self._file_path = None
        self._blue_hist = None
        self._green_hist = None
        self._red_hist = None

    def read(self, file_path):
        self._file_path = file_path
        img = cv2.imread(file_path, cv2.IMREAD_COLOR)
        self._blue_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        self._green_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
        self._red_hist = cv2.calcHist([img], [2], None, [256], [0, 256])

    def get_file_path(self):
        return self._file_path

