import sys

from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedWidth(400)
        self.pressing = False
        self.element = MyFrame()

        self.ver = QVBoxLayout()
        self.ver.addWidget(self.element)
        self.setLayout(self.ver)


class MyFrame(QWidget):

    def __init__(self):
        super().__init__()

        self.title = QLabel("My Own Bar")
        self.setFixedHeight(10)
        self.setContentsMargins(0, 0, 0, 0)
        self.hide_bth = QPushButton('_')
        self.hide_bth.setFixedSize(10, 10)

        self.full_screen_btn = QPushButton('f')
        self.full_screen_btn.setFixedSize(10, 10)

        self.close_btn = QPushButton('x')
        self.close_btn.setFixedSize(10, 10)

        self.title.setAlignment(Qt.AlignCenter)
        self.vertical = QHBoxLayout()
        self.vertical.setContentsMargins(0, 0, 0, 0)
        self.vertical.addWidget(self.title)
        self.vertical.addWidget(self.hide_bth)
        self.vertical.addWidget(self.full_screen_btn)
        self.vertical.addWidget(self.close_btn)
        self.setLayout(self.vertical)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    frame = MyWidget()
    frame.show()
    sys.exit(app.exec_())
