
__author__ = 'Cuong Nguyen Ngoc'


class PrecisionRecall:

    def __init__(self):
        self.__false = 0
        self.__true = 0
        self.__total_images_in_category = 0

    def inc_false(self):
        self.__false += 1

    def inc_true(self):
        self.__true += 1

    def set_total_image_in_category(self, total):
        self.__total_images_in_category = total

    def get_precision(self):
        mau = self.__true + self.__false
        if mau == 0:
            return 0
        return self.__true / mau

    def get_recall(self):
        if self.__total_images_in_category == 0:
            return 0
        return self.__true / self.__total_images_in_category
