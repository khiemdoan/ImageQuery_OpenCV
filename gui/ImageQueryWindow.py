from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from gui.ImageQueryUi import Ui_ImageQuery
from PyQt5.QtWidgets import QFileDialog, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtGui import QImageReader, QPixmap
from image_process import Manager

__author__ = 'Khiem Doan Hoa'


class ImageQueryWindow(QMainWindow, Ui_ImageQuery):

    def __init__(self):
        super(ImageQueryWindow, self).__init__()
        self.setupUi(self)
        self._setup_event()
        self._manager = Manager()

    def _setup_event(self):
        self.lineEdit_database.textEdited.connect(self._changed_database_line_edit)
        self.lineEdit_image.textEdited.connect(self._changed_image_line_edit)

        self.button_browse_image_data.clicked.connect(self._clicked_browse_image_data)
        self.button_browse_database.clicked.connect(self._clicked_browse_database)
        self.button_browse_image.clicked.connect(self._clicked_browse_image)

        self.button_load_image_data.clicked.connect(self._clicked_load_image_data)
        self.button_save_database.clicked.connect(self._clicked_save_database)
        self.button_load_database.clicked.connect(self._clicked_load_database)
        self.button_query_image.clicked.connect(self._clicked_query_image)

        self.button_next.clicked.connect(self._clicked_next)
        self.button_back.clicked.connect(self._clicked_back)

    def _changed_database_line_edit(self):
        path = self.lineEdit_database.text()
        self._manager.set_database(path)

    def _changed_image_line_edit(self):
        file_path = self.lineEdit_image.text()
        image_reader = QImageReader(file_path)
        if image_reader.canRead() is True:
            widget_height = self.queryView.height()
            widget_width = self.queryView.width()
            image = image_reader.read().scaled(widget_width, widget_height, QtCore.Qt.KeepAspectRatio)
            item = QGraphicsPixmapItem(QPixmap.fromImage(image))
            scene = QGraphicsScene()
            scene.addItem(item)
            self.queryView.setScene(scene)
        else:
            scene = QGraphicsScene()
            self.queryView.setScene(scene)

    def _clicked_browse_image_data(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(options=QFileDialog.Options())
        self.lineEdit_image_data.setText(folder_path)

    def _clicked_browse_database(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(options=QFileDialog.Options())
        self.lineEdit_database.setText(folder_path)
        self._changed_database_line_edit()

    def _clicked_browse_image(self):
        dialog = QFileDialog()
        file_path = dialog.getOpenFileName(options=QFileDialog.Options())
        self.lineEdit_image.setText(file_path[0])
        self._changed_image_line_edit()

    def _clicked_load_image_data(self):
        folder_path = self.lineEdit_image_data.text()
        self._manager.load_image_folder(folder_path)

    def _clicked_load_database(self):
        self._manager.load_database()

    def _clicked_save_database(self):
        self._manager.save_database()

    def _clicked_query_image(self):
        file_path = self.lineEdit_image.text()
        self._manager.query_image(file_path)

    def _clicked_next(self):
        self._manager.next_image()

    def _clicked_back(self):
        self._manager.back_image()
