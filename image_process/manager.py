
import os
import imghdr
from .image import Image
from .database import Database


class Manager:

    def __init__(self):
        self.__database = Database()
        self.__images = []

    def load_image_folder(self, folder_path):
        self.__images = []
        for item in os.listdir(folder_path):
            file_path = os.path.join(folder_path, item)
            if imghdr.what(file_path) is not None:          # xác định xem file đầu vào có phải là file ảnh không
                image = Image()
                image.read(file_path)
                self.__images.append(image)
        return True

    def set_database(self, path):
        self.__database.set_path(path)

    def save_database(self):
        self.__database.erase()
        self.__database.saves(self.__images)

    def load_database(self):
        self.__images = []
        self.__images = self.__database.loads()

    def query_image(self, file_path):
        image = Image()
        image.read(file_path)
        print('query image: ', file_path)

    def get_image(self):
        print('get image: ')

    def next_image(self):
        print('next image')

    def back_image(self):
        print('back image')
