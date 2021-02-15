import sys
import unittest

from first import main

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
test_window = main.FirstWindow()


class ApplicationsTest(unittest.TestCase):

    def test_window_title(self):
        self.assertEqual(test_window.windowTitle(), 'v_|0.0.1|')

    def test_window_geometry(self):
        self.assertEqual(test_window.geometry(), QtCore.QRect(350, 200, 1280, 666))

    def test_window_background(self):
        self.assertEqual(test_window.hasMouseTracking(), True)

    def test_window_drops_accept(self):
        self.assertEqual(test_window.acceptDrops(), True)

    def test_window_buttons_is_enabled(self):
        self.assertEqual(
            all([
                test_window.playBtn.isEnabled(),
                test_window.forwardBtn.isEnabled(),
                test_window.backBtn.isEnabled(),
                test_window.blankBtn.isEnabled(),
                 ]), False)


if __name__ == '__main__':
    unittest.main()