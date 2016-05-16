import cv2

__author__ = "Anh Do Nguyet"


class Image:

    def __init__(self):
        self.__file_path = None
        self.__blue_hist = None
        self.__green_hist = None
        self.__red_hist = None

    def read(self, file_path):
        self.__file_path = file_path
        img = cv2.imread(file_path, cv2.IMREAD_COLOR)
        self.__blue_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        self.__green_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
        self.__red_hist = cv2.calcHist([img], [2], None, [256], [0, 256])

    def get_file_path(self):
        return self.__file_path
