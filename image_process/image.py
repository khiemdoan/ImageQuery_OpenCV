
import cv2


class Image:

    def __init__(self):
        self._file_path = None
        self._hist = None

    def read(self, file_path):
        self._file_path = file_path
        mat = cv2.imread(file_path, cv2.IMREAD_COLOR)

    def get_file_path(self):
        return self._file_path

