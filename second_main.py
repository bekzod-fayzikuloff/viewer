import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
import pillow_file


def resource_path(relative):

    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)


class ImageLabel(QLabel):
    '''Класс унаследованный от класса QLabel  в нем мы прописываем описание параметров экземпляра этого класса'''
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont('SansSerif', 11, QFont.StyleItalic))
        self.setText("<font color='#384ED6'>Перетените сюда изображение</font>")
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa;
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)


class AppDemo(QWidget):
    stylesheet = """
        QWidget {
            background: #7F7F7F;
        }
    """
    def __init__(self):
        super().__init__()
        self.setFixedSize(720, 480)
        self.setWindowTitle('Image Area')
        self.setWindowIcon(QIcon(resource_path(r'ico/L.ico')))
        self.setStyleSheet(self.stylesheet)
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()

        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)

        self.setLayout(mainLayout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(pillow_file.image_size_fix(file_path))

            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))
