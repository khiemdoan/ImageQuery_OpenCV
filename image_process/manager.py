
from .image import Image


class Manager:

    def __init__(self):
        pass

    def load_image_folder(self, folder_path):
        print('load image folder: ', folder_path)

    def set_database(self, path):
        print('set database: ', path)

    def save_database(self):
        print('save database')

    def load_database(self):
        print('load database')

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
