
import os
import imghdr
from .image import Image
from .database import Database
from .precisionrecall import PrecisionRecall
from matplotlib import pyplot


class Manager:

    def __init__(self):
        self.__database = Database()
        self.__images = []
        self.__distances = []
        self.__query_result = []
        self.__result_index = 0
        self.__query_image = None
        self.__bin_number = 256
        self.__total_images_in_category = {}

    def load_image_folder(self, folder_path):
        self.__images = []
        for item in os.listdir(folder_path):
            file_path = os.path.join(folder_path, item)
            if imghdr.what(file_path) is not None:          # xác định xem file đầu vào có phải là file ảnh không
                image = Image()
                if len(item) < 7:
                    image.set_category('0')
                else:
                    image.set_category(item[0])
                image.read(file_path)
                self.__images.append(image)

    def set_database(self, path):
        self.__database.set_path(path)

    def save_database(self):
        self.__database.erase()
        self.__database.saves(self.__images)

    def load_database(self):
        self.__images = []
        self.__images = self.__database.loads()

    def query_image(self, file_path, bin_number=256, top_number=75):
        self.__bin_number = bin_number
        self.__query_result = []
        self.__result_index = 0

        if len(self.__images) == 0:
            return 'Data is empty!'

        if imghdr.what(file_path) is not None:          # xác định xem file đầu vào có phải là file ảnh không
            self.__query_image = Image()
            self.__query_image.read(file_path)
            self.__distances = []
            self.__total_images_in_category = {}

            for img in self.__images:
                d = self.__query_image.calc_distance(img, bin_number)
                cat = img.get_category()
                self.__total_images_in_category[cat] = self.__total_images_in_category.get(cat, 0) + 1
                print(img.get_file_path(), ' - distance: ', d)
                self.__distances.append(d)

            # sắp xếp kết quả
            # cùng lúc sắp xếp 2 list __distances và images theo __distances
            combined = zip(self.__distances, self.__images)
            z = sorted(combined)
            self.__distances, self.__images = zip(*z)

            top_number = min(top_number, len(self.__images))
            for i in range(0, top_number):
                self.__query_result.append(self.__images[i])

    def get_image(self):
        if len(self.__query_result) != 0:
            img = self.__query_result[self.__result_index]
            return img.get_file_path()

    def next_image(self):
        self.__result_index += 1
        if self.__result_index >= len(self.__query_result):
            self.__result_index = 0

    def back_image(self):
        self.__result_index -= 1
        if self.__result_index < 0:
            self.__result_index = len(self.__query_result)

    def draw_query_image_histogram(self, file_path, bin_number=256):
        if imghdr.what(file_path) is not None:
            self.__query_image = Image()
            self.__query_image.read(file_path)
            self.__query_image.draw_histogram(bin_number)

    def draw_result_image_histogram(self):
        if len(self.__query_result) != 0:
            img = self.__query_result[self.__result_index]
            img.draw_histogram(self.__bin_number)

    def get_pr_curve(self, file_path, bin_number=256, top_number=75):
        if len(self.__images) == 0:
            return 'Data is empty!'

        file_name = os.path.basename(file_path)

        if imghdr.what(file_path) is not None:  # xác định xem file đầu vào có phải là file ảnh không

            category_query = '0'
            if len(file_name) >= 7:
                category_query = file_name[0]

            self.query_image(file_path, bin_number, top_number)

            recalls = []
            precisions = []

            # tính với 1 kết quả, 2 kết quả ... đến len(query_result) kết quả
            for i in range(1, len(self.__query_result) + 1):
                pr = PrecisionRecall()
                total_images = self.__total_images_in_category.get(category_query, 0)
                pr.set_total_image_in_category(total_images)
                for j in range(0, i):
                    if category_query == self.__query_result[j].get_category():
                        pr.inc_true()
                    else:
                        pr.inc_false()
                recalls.append(pr.get_recall())
                precisions.append(pr.get_precision())

            pyplot.figure()
            pyplot.plot(recalls, precisions)
            pyplot.ylim([0.0, 1.05])
            pyplot.xlim([0.0, 1.05])
            pyplot.xlabel('Recall')
            pyplot.ylabel('Precision')
            pyplot.title('Precision-Recall')
            pyplot.show()
