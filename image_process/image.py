import cv2


__author__ = "Anh Do Nguyet"


class Image:

    def __init__(self):
        self.__file_path = None
        self.__blue_hist = None
        self.__green_hist = None
        self.__red_hist = None
        self.__category = '0'

    # đọc dữ liệu ảnh đầu vào, tính histogram, chuẩn hoá
    def read(self, file_path):
        self.__file_path = file_path
        img = cv2.imread(file_path, cv2.IMREAD_COLOR)

        # lấy histogram của ảnh
        self.__blue_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        self.__green_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
        self.__red_hist = cv2.calcHist([img], [2], None, [256], [0, 256])

        # chuẩn hoá histogram
        cv2.normalize(self.__blue_hist, self.__blue_hist, 0, 255, cv2.NORM_MINMAX)
        cv2.normalize(self.__green_hist, self.__green_hist, 0, 255, cv2.NORM_MINMAX)
        cv2.normalize(self.__red_hist, self.__red_hist, 0, 255, cv2.NORM_MINMAX)

    def get_file_path(self):
        return self.__file_path

    def get_category(self):
        return self.__category

    def set_category(self, cat):
        self.__category = cat

    def get_blue_histogram(self):
        return self.__blue_hist

    def get_green_histogram(self):
        return self.__green_hist

    def get_red_histogram(self):
        return self.__red_hist

    def calc_distance(self, image, method=cv2.HISTCMP_CHISQR):
        d = cv2.compareHist(self.__blue_hist, image.get_blue_histogram(), method)
        d += cv2.compareHist(self.__green_hist, image.get_green_histogram(), method)
        d += cv2.compareHist(self.__red_hist, image.get_red_histogram(), method)
        return d
