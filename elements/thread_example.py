import time

from PyQt5.QtCore import QThread


class MyThread(QThread):

    def __init__(self, func):
        super().__init__()
        self.func = func

    def run(self) -> None:
        self.func()

