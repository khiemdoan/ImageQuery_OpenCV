from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from gui.ImageQueryUi import Ui_ImageQuery
from PyQt5.QtWidgets import QFileDialog, QGraphicsPixmapItem, QGraphicsScene, QMessageBox
from PyQt5.QtGui import QImageReader, QPixmap
from image_process import Manager

__author__ = 'Khiem Doan Hoa'


class ImageQueryWindow(QMainWindow, Ui_ImageQuery):

    def __init__(self):
        super(ImageQueryWindow, self).__init__()
        self.setupUi(self)
        self.__setup_ui()
        self.__setup_event()
        self.__manager = Manager()

    def __setup_ui(self):
        i = 256
        while i >= 2:
            self.comboBox_bin_number.addItem(str(int(i)))
            self.comboBox_bin_number_pr.addItem(str(int(i)))
            i /= 2

    def __setup_event(self):
        self.lineEdit_database.textEdited.connect(self.__changed_database_line_edit)
        self.lineEdit_image.textEdited.connect(self.__changed_image_line_edit)

        self.button_browse_image_data.clicked.connect(self.__clicked_browse_image_data)
        self.button_browse_database.clicked.connect(self.__clicked_browse_database)
        self.button_browse_image.clicked.connect(self.__clicked_browse_image)

        self.button_load_image_data.clicked.connect(self.__clicked_load_image_data)
        self.button_save_database.clicked.connect(self.__clicked_save_database)
        self.button_load_database.clicked.connect(self.__clicked_load_database)
        self.button_query_image.clicked.connect(self.__clicked_query_image)

        self.button_next.clicked.connect(self.__clicked_next)
        self.button_back.clicked.connect(self.__clicked_back)

        self.button_query_histogram.clicked.connect(self.__clicked_show_query_histogram)
        self.button_result_histogram.clicked.connect(self.__clicked_show_result_histogram)

        self.slider_select_top.valueChanged.connect(self.__changed_slider_select_top)

        self.slider_select_top_pr.valueChanged.connect(self.__changed_slider_select_top_pr)
        self.button_browse_image_pr.clicked.connect(self.__clicked_browse_image_pr)
        self.button_draw_pr.clicked.connect(self.__draw_pr)

    def __changed_database_line_edit(self):
        path = self.lineEdit_database.text()
        self.__manager.set_database(path)

    def __changed_image_line_edit(self):
        file_path = self.lineEdit_image.text()
        image_reader = QImageReader(file_path)
        if image_reader.canRead() is True:
            widget_height = self.queryView.height()
            widget_width = self.queryView.width()
            image = image_reader.read().scaled(widget_width, widget_height, Qt.KeepAspectRatio)
            item = QGraphicsPixmapItem(QPixmap.fromImage(image))
            scene = QGraphicsScene()
            scene.addItem(item)
            self.queryView.setScene(scene)
        else:
            scene = QGraphicsScene()
            self.queryView.setScene(scene)

    def __changed_slider_select_top(self):
        value = self.slider_select_top.value()
        self.label_select_top_value.setText(str(value))

    def __changed_slider_select_top_pr(self):
        value = self.slider_select_top_pr.value()
        self.label_select_top_value_pr.setText(str(value))

    def __clicked_browse_image_data(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(options=QFileDialog.Options())
        self.lineEdit_image_data.setText(folder_path)

    def __clicked_browse_database(self):
        dialog = QFileDialog()
        file_path = dialog.getOpenFileName(options=QFileDialog.Options())
        self.lineEdit_database.setText(file_path[0])
        self.__changed_database_line_edit()

    def __clicked_browse_image(self):
        dialog = QFileDialog()
        file_path = dialog.getOpenFileName(options=QFileDialog.Options())
        self.lineEdit_image.setText(file_path[0])
        self.__changed_image_line_edit()

    def __clicked_load_image_data(self):
        folder_path = self.lineEdit_image_data.text()
        self.__manager.load_image_folder(folder_path)
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Information')
        msg_box.setText('Loading data is successful!')
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec()

    def __clicked_load_database(self):
        self.__manager.load_database()
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Information')
        msg_box.setText('Loading data is successful!')
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec()

    def __clicked_save_database(self):
        self.__manager.save_database()
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Information')
        msg_box.setText('Saving data is successful!')
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec()

    def __clicked_query_image(self):
        file_path = self.lineEdit_image.text()
        bin_number = self.comboBox_bin_number.currentText()
        bin_number = int(bin_number)
        top_number = self.slider_select_top.value()
        ret = self.__manager.query_image(file_path, bin_number, top_number)
        if ret is None:
            file_path = self.__manager.get_image()
            self.__display_result_image(file_path)
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Information')
            msg_box.setText(ret)
            msg_box.setIcon(QMessageBox.Information)
            msg_box.exec()

    def __clicked_next(self):
        self.__manager.next_image()
        file_path = self.__manager.get_image()
        self.__display_result_image(file_path)

    def __clicked_back(self):
        self.__manager.back_image()
        file_path = self.__manager.get_image()
        self.__display_result_image(file_path)

    def __display_result_image(self, file_path):
        image_reader = QImageReader(file_path)
        if image_reader.canRead() is True:
            widget_height = self.resultView.height()
            widget_width = self.resultView.width()
            image = image_reader.read().scaled(widget_width, widget_height, Qt.KeepAspectRatio)
            item = QGraphicsPixmapItem(QPixmap.fromImage(image))
            scene = QGraphicsScene()
            scene.addItem(item)
            self.resultView.setScene(scene)
        else:
            scene = QGraphicsScene()
            self.resultView.setScene(scene)

    def __clicked_show_query_histogram(self):
        file_path = self.lineEdit_image.text()
        bin_number = self.comboBox_bin_number.currentText()
        bin_number = int(bin_number)
        self.__manager.draw_query_image_histogram(file_path, bin_number)

    def __clicked_show_result_histogram(self):
        self.__manager.draw_result_image_histogram()

    def __clicked_browse_image_pr(self):
        dialog = QFileDialog()
        file_path = dialog.getOpenFileName(options=QFileDialog.Options())
        self.lineEdit_image_pr.setText(file_path[0])

    def __draw_pr(self):
        file_path = self.lineEdit_image_pr.text()
        bin_number = self.comboBox_bin_number_pr.currentText()
        bin_number = int(bin_number)
        top_number = self.slider_select_top_pr.value()
        ret = self.__manager.draw_pr(file_path, bin_number, top_number)
        if ret is not None:
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Information')
            msg_box.setText(ret)
            msg_box.setIcon(QMessageBox.Information)
            msg_box.exec()
