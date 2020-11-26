from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont
from PyQt5.QtCore import Qt, QUrl, QSize, QEvent
import sys


class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Settings')
        self.setWindowIcon(QIcon(r'ico\L.png'))
        self.setFixedSize(QSize(720, 480))
        pall = self.palette()
        pall.setColor(QPalette.Window, QColor('#45484A'))
        self.setPalette(pall)

        self.init_ui()

    def init_ui(self):
        pass


    def change_color(self):
        return QColor('#45484A')
