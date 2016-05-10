from PyQt5.QtWidgets import QMainWindow
from gui.ImageQueryUi import Ui_ImageQuery
from PyQt5.QtWidgets import QFileDialog

__author__ = 'Khiem Doan Hoa'


class ImageQueryWindow(QMainWindow, Ui_ImageQuery):

    def __init__(self):
        super(ImageQueryWindow, self).__init__()
        self.setupUi(self)
        self._setup_event()

    def _setup_event(self):
        self.button_browse_image_data.clicked.connect(self._clicked_browse_image_data)
        self.button_browse_database.clicked.connect(self._clicked_browse_database)
        self.button_browse_image.clicked.connect(self._clicked_browse_image)

        self.button_load_image_data.clicked.connect(self._clicked_load_image_data)
        self.button_save_database.clicked.connect(self._clicked_save_database)
        self.button_load_database.clicked.connect(self._clicked_load_database)
        self.button_query_image.clicked.connect(self._clicked_query_image)

        self.button_next.clicked.connect(self._clicked_next)
        self.button_back.clicked.connect(self._clicked_back)

    def _clicked_browse_image_data(self):
        folder_path = QFileDialog.getExistingDirectory(self)
        self.lineEdit_image_data.setText(folder_path)

    def _clicked_browse_database(self):
        folder_path = QFileDialog.getExistingDirectory(self)
        self.lineEdit_database.setText(folder_path)

    def _clicked_browse_image(self):
        file_path = QFileDialog.getOpenFileName(self)
        self.lineEdit_image.setText(file_path[0])

    def _clicked_load_image_data(self):
        folder_path = self.lineEdit_image_data.text()
        print(folder_path)

    def _clicked_load_database(self):
        folder_path = self.lineEdit_database.text()
        print(folder_path)

    def _clicked_save_database(self):
        print('save')

    def _clicked_query_image(self):
        file_path = self.lineEdit_image.text()
        print(file_path)

    def _clicked_next(self):
        print('next')

    def _clicked_back(self):
        print('back')
