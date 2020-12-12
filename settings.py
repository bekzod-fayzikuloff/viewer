from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout,
                             QVBoxLayout, QLabel, QSlider, QFileDialog, QDialog)
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont
from PyQt5.QtCore import Qt, QUrl, QSize, QEvent
import os


def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)


class SettingsWindow(QWidget):
    stylesheet = '''
        QWidget {
            background: #F0F0F0;
        }
    '''

    def __init__(self):
        super().__init__()
        self.setFixedSize(720, 480)
        self.setWindowTitle('Settings')
        self.setWindowIcon(QIcon(resource_path(r'ico/setting.png')))
        self.setStyleSheet(self.stylesheet)
        self.ui()

    def ui(self):
        self.darkBtn = QPushButton('do dark')
        self.darkBtn.clicked.connect(self.change_to_dark)

        self.whiteBnt = QPushButton('do white')
        self.whiteBnt.clicked.connect(self.change_to_white)

        hbox = QHBoxLayout()

        hbox.addWidget(self.darkBtn)
        hbox.addWidget(self.whiteBnt)

        self.setLayout(hbox)

    def change_to_dark(self):
        dark_theme ='#3C3F41'
        self.setStyleSheet('QWidget {background: %s;}' % dark_theme)

    def change_to_white(self):
        white_theme = '#EDEDED'
        self.setStyleSheet('QWidget {background: %s;}' % white_theme)