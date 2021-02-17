import sys
import unittest

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from first.elements import second_window, slider

app = QApplication(sys.argv)


class SecondWindowElementTest(unittest.TestCase):
    test_second_window = second_window.WindowForImage()

    def test_second_window_title_name(self):
        self.assertEqual(SecondWindowElementTest.test_second_window.windowTitle(), 'Image Area')

    def test_second_window_size(self):
        self.assertEqual(SecondWindowElementTest.test_second_window.size(), QtCore.QSize(720, 480))

    def test_second_window_stylesheet_background_color(self):
        start = str(SecondWindowElementTest.test_second_window.styleSheet()).find('background')
        end = str(SecondWindowElementTest.test_second_window.styleSheet()).find(';') + 1

        self.assertEqual(
            str(SecondWindowElementTest.test_second_window.styleSheet())[start:end],
            'background: #7F7F7F;'
        )

    def test_second_window_can_drop(self):
        self.assertTrue(SecondWindowElementTest.test_second_window.acceptDrops())

    def test_second_window_label_class(self):
        test_label_obj = second_window.ImageLabel()
        self.assertEqual(SecondWindowElementTest.test_second_window.photoViewer.__class__, test_label_obj.__class__)


class SliderElementTest(unittest.TestCase):
    test_slider_object = slider.MySlider(orient=QtCore.Qt.Horizontal)

    def test_slider_maximum_height(self):
        self.assertEqual(SliderElementTest.test_slider_object.maximumHeight(), 7)

    def test_slider_orientation(self):
        self.assertEqual(SliderElementTest.test_slider_object.orientation(), QtCore.Qt.Horizontal)




