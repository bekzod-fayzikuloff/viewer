import sys
import unittest

from PyQt5.QtMultimedia import QMediaPlayer

import main

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
        self.assertFalse(
            all([
                test_window.playBtn.isEnabled(),
                test_window.forwardBtn.isEnabled(),
                test_window.backBtn.isEnabled(),
                test_window.blankBtn.isEnabled(),
                 ])
        )

    def test_window_tool_tip(self):
        self.assertEqual(test_window.screenBtn.toolTip(), 'Переключить на полноэкранный размер'),
        self.assertEqual(
            test_window.imageBtn.toolTip(), 'Открывает второе окно которое позволяет взимодействовать с изображениями'
        )
        self.assertEqual(test_window.themeBtn.toolTip(), 'Изменить задний фон'),
        self.assertEqual(test_window.label1.toolTip(), 'Прошло времени'),
        self.assertEqual(test_window.label2.toolTip(), 'Общая продолжительность')

    def test_labels_text(self):
        self.assertEqual(test_window.label1.text(), '0:00 /')
        self.assertEqual(test_window.label2.text(), '0:00')

    def test_window_size_change(self):
        self.assertEqual(test_window.screenBtn.objectName(), 'fullscreen')
        test_window.full_screen()
        self.assertEqual(test_window.screenBtn.objectName(), 'normal_screen')
        self.assertTrue(test_window.isMaximized())

    def test_window_volume_function(self):
        self.assertEqual(test_window.volumeBtn.objectName(), 'volume_btn')
        self.assertFalse(test_window.mediaPlayer.isMuted())
        test_window.volume()
        self.assertEqual(test_window.volumeBtn.objectName(), 'btn')
        self.assertTrue(test_window.mediaPlayer.isMuted())

    def test_window_positions_changing(self):
        self.assertEqual(test_window.mediaPlayer.position(), 0)
        test_window.go_forward()
        self.assertEqual(test_window.mediaPlayer.position(), 10000)
        test_window.go_back()
        self.assertEqual(test_window.mediaPlayer.position(), 0)

    def test_window_media_player_class(self):
        test_class_ = QMediaPlayer()
        self.assertEqual(type(test_class_), type(test_window.mediaPlayer))

    def test_window_color(self):
        self.assertEqual(test_window.styleSheet(), 'background-color: #F0F0F0;')
        test_window.change_to_dark_theme()
        self.assertEqual(test_window.styleSheet(), 'background-color: #3C3F41;')

    def test_window_second_window(self):
        test_window.imageBtn.click()
        self.assertTrue(test_window.second_window.isEnabled())


if __name__ == '__main__':
    unittest.main()
