from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout,
                             QVBoxLayout, QLabel, QSlider, QFileDialog, QShortcut)
import sys
from second_main import AppDemo
from for_example import Switch
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QFont, QKeySequence
from PyQt5.QtCore import Qt, QUrl, QSize, QEvent
import time
import os


# полный список используемых модулей(библиотек) для создания GUI интерфейса используется модуль PyQt5
# и его классы и также модуль : sys, time, keyboard
# _____________________________#
start_time = time.time()
# также я добавил таймер для того чтобы знать сколько выполняется скрипт
# (если запустить код пару раз то время будет отображаться корректне)


def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)


class FirstWindow(QWidget):
    '''
       В этом классе описывается внешний вид, логика и функционал моего видеоплеера версии 0.01
       постораюсь по мере возможности улучшать свой проект добавляя функционал и
       удобства , это \'документация\', надеюсь моя программа тебе
       понравится
       P.S знаю что много плохого кода. сорри
    '''

    def __init__(self):
        ''' Инициализируем Класс нашего главного окна и в нем прописывем основные характеристики нашего окна (размер , цвет , "тайтл" и вызывает методы
         в которых отслеживаются события(перемещение мыши) и прописан внешний вид интерфейса '''

        super().__init__()
        self.setWindowTitle('v_|0.0.1|')
        self.setGeometry(350, 200, 1280, 666)
        self.setWindowIcon(QIcon(resource_path(r'ico\L.ico')))
        self.setStyleSheet("background-color: #F0F0F0;")

        self.setMouseTracking(True)
        self.setCursor(Qt.PointingHandCursor)
        self.init_ui()

    def event(self, e):
        ''' Метод обработчик который фиксирует взаимодействия с клавиатурой и мышью для манипуляцией
        над процессом показа виде (изменения громкости , перемотка и остановка '''
        if e.type() == QEvent.MouseButtonDblClick:
            self.fullscreen()
        elif e.type() == QEvent.Wheel:
            pass
        elif e.type() == QEvent.KeyPress:
            if e.key() == Qt.Key_Space:
                self.play_video()
            if e.key() == Qt.Key_VolumeUp:
                self.plus_volume()
            if e.key() == Qt.Key_VolumeDown:
                self.min_volume()

        elif e.type() == QEvent.MouseButtonPress:
            if e.buttons() & Qt.LeftButton:
                self.play_video()
        return QWidget.event(self, e)

    def mouseMoveEvent(self, event):
        '''Здесь я пытался реализовать обработчик , который показался мне интересным ,
         во время воспроизведения видео если курсор мыши находится внутри "видеовиджета"
         то ползунок громкости , продолжительности видео и кнопки громкости скроются '''
        if self.isMaximized():
            if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
                slider_y = (self.slider.pos().y() - 3)
                if event.pos().y() > slider_y:
                    self.blef_win_on()
                elif event.pos().y() < slider_y:
                    self.blef_win()
            if self.mediaPlayer.state() == QMediaPlayer.PausedState:
                self.blef_win_on()
        else:
            self.blef_win_on()
            if self.hslider.isVisible():
                self.blef_win_on()

    def init_ui(self):
        conf_for_blank = '''QPushButton{
        border: none;
        margin: 0px;
        padding: 0px;
        background-color:#F0F0F0;
        }
        '''
        config = '''QPushButton{
        border: none;
        margin: 0px;
        padding: 0px;
        background-color:#F0F0F0;
        }
        QPushButton:hover{
        background-color: #B4B4B4;
        border-radius:7px;
        width: 30px;
        }
        '''

        global hboxLayout
        global hboxLayout2
        global vboxLayout
        global videowidget
        global openBtn

        # создание экземпляра(объекта) класса QMediaPlayer() и передача аргуметов
        # QMediaPlayer.VideoSurface указывает что он 'служит' для воспроизведения видео
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # создание экземпляра(объекта) класса QVideoWidget()
        videowidget = QVideoWidget()
        videowidget.setStyleSheet('background-color: #B4B4B4;')

        # создание button(кнопки открыть)
        openBtn = QPushButton()
        openBtn.setStyleSheet(config)
        openBtn.setIcon(QIcon(resource_path(r'ico\folders.png')))
        openBtn.setIconSize(QSize(20, 20))
        openBtn.clicked.connect(self.open_file)
        openBtn.setToolTip('Открытие папок для просмотра файлов')
        openBtn.setToolTipDuration(2500)

        # создание button (кнопки для запуска)
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setFlat(True)
        self.playBtn.setStyleSheet(config)
        self.playBtn.setIcon(QIcon(resource_path(r'ico\play.png')))
        self.playBtn.setIconSize(QSize(40, 40))
        self.playBtn.clicked.connect(self.play_video)

        # создание button(кнопки для перемотки вперед)
        self.forwardBtn = QPushButton()
        self.forwardBtn.setEnabled(False)
        self.forwardBtn.setIcon(QIcon(resource_path(r'ico\forward.png')))
        self.forwardBtn.setStyleSheet(config)
        self.forwardBtn.setIconSize(QSize(20, 20))
        self.forwardBtn.clicked.connect(self.go_forward)

        # создание button (для перемотки назад)
        self.backBtn = QPushButton()
        self.backBtn.setEnabled(False)
        self.backBtn.setIcon(QIcon(resource_path(r'ico\backward .png')))
        self.backBtn.setStyleSheet(config)
        self.backBtn.setIconSize(QSize(20, 20))
        self.backBtn.clicked.connect(self.go_back)

        # для volume(громкости)
        self.volumeBtn = QPushButton()
        self.volumeBtn.setObjectName('volume_btn')
        self.volumeBtn.setIcon(QIcon(resource_path(r'ico\volume1.png')))
        self.volumeBtn.setStyleSheet(config)
        self.volumeBtn.setIconSize(QSize(17, 17))
        self.volumeBtn.clicked.connect(self.volume)

        # настройка button(кнопок)
        self.screenBtn = QPushButton()
        self.screenBtn.setObjectName('fullscreen')
        self.screenBtn.setStyleSheet(config)
        self.screenBtn.setIcon(QIcon(resource_path(r'ico\fullscreen.png')))
        self.screenBtn.setIconSize(QSize(19, 19))
        self.screenBtn.clicked.connect(self.fullscreen)
        self.screenBtn.setToolTip('Переключить на полноэкранный размер')
        self.screenBtn.setToolTipDuration(2500)

# ----- кнопки для пустых мест ----- #

        # создание button (для окна настроек)
        self.imageBtn = QPushButton()
        self.imageBtn.setIcon(QIcon(resource_path(r'ico\photo.png')))
        self.imageBtn.setToolTip('Открывает второе окно которое позволяет взимодействовать с изображениями')
        self.imageBtn.setIconSize((QSize(18, 18)))
        self.imageBtn.setEnabled(True)
        self.imageBtn.setStyleSheet(config)
        self.imageBtn.clicked.connect(self.buttonHandler)

        self.themeBtn = Switch(thumb_radius=11, track_radius=8)
        self.themeBtn.setObjectName('default')
        self.themeBtn.setToolTip('Изменить задний фон')
        self.themeBtn.clicked.connect(self.change_to_dark_theme)

        self.blankBtn = QPushButton()
        self.blankBtn.setEnabled(False)
        self.blankBtn.setStyleSheet(conf_for_blank)

# --------------------------------------- #

        # создание slider'а
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.setMaximumHeight(7)
        self.slider.sliderMoved.connect(self.set_position)

        # создания slider для volume
        self.hslider = QSlider(Qt.Horizontal)
        self.hslider.setRange(0, 100)
        self.hslider.setMaximumHeight(7)
        self.hslider.sliderMoved.connect(self.set_volume_position)
        self.hslider.setMaximumWidth(80)
        self.hslider.setSliderPosition(100)

        # создания label'а
        self.label1 = QLabel('0:00 /')
        self.label1.setToolTip('Прошло времени')
        self.label1.setFont(QFont('SansSerif', 8, QFont.Bold))
        self.label2 = QLabel('0:00')
        self.label2.setToolTip('Общая продолжительность')
        self.label2.setFont(QFont('SansSerif', 8, QFont.Bold))

        # создание hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0, 0, 0, 0)

        # создание hbox2 layout
        hboxLayout2 = QHBoxLayout()
        hboxLayout.setContentsMargins(0, 0, 0, 0)

        # добавления виджетов в hbox2 layout
        hboxLayout2.addWidget(self.label1)
        hboxLayout2.addWidget(self.label2)
        hboxLayout2.addWidget(self.slider)
        hboxLayout2.addWidget(self.volumeBtn)
        hboxLayout2.addWidget(self.hslider)

        # добавления виджетов в hbox layout
        hboxLayout.addWidget(self.themeBtn)
        hboxLayout.addWidget(self.blankBtn)
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.backBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.forwardBtn)
        hboxLayout.addWidget(self.imageBtn)
        hboxLayout.addWidget(self.screenBtn)

        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout2)
        vboxLayout.addLayout(hboxLayout)

        self.setLayout(vboxLayout)
        self.mediaPlayer.setVideoOutput(videowidget)

        # обработчики медиа сигналов
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

        self.mediaPlayer.volumeChanged.connect(self.set_volume_position)
        self.mediaPlayer.durationChanged.connect(self.duration_volume)

        # Несколько функций которые вызываются во время взаимодействия с клавишами для удобства
        self.volumeMinSc = QShortcut(QKeySequence('Down'), self)
        self.volumeMinSc.activated.connect(self.min_volume)

        self.volumePlusSc = QShortcut(QKeySequence('Up'), self)
        self.volumePlusSc.activated.connect(self.plus_volume)

        self.forwardSc = QShortcut(QKeySequence('Right'), self)
        self.forwardSc.activated.connect(self.go_forward_with_key)

        self.backSc = QShortcut(QKeySequence('Left'), self)
        self.backSc.activated.connect(self.go_back_with_key)

    # Функция открытия файла
    def open_file(self):
        global filename
        filename, _ = QFileDialog.getOpenFileName(self)
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
            self.backBtn.setEnabled(True)
            self.forwardBtn.setEnabled(True)

    # Функция запуска и паузы видеоплеера
    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def go_back_with_key(self):
        pos = self.mediaPlayer.position()
        pos = min(pos - 1000, pos)
        self.mediaPlayer.setPosition(pos)

    def go_forward_with_key(self):
        pos = self.mediaPlayer.position()
        pos = max(pos + 1000, pos)
        self.mediaPlayer.setPosition(pos)


    def blef_win(self):
        # Сокрытие вернего слоя Layout'a
        self.label1.hide()
        self.label2.hide()
        self.slider.hide()
        self.volumeBtn.hide()
        self.hslider.hide()
        # Сокрытие нижнего слоя Layout'a
        openBtn.hide()
        self.imageBtn.hide()
        self.backBtn.hide()
        self.playBtn.hide()
        self.forwardBtn.hide()
        self.screenBtn.hide()
        self.themeBtn.hide()

    def blef_win_on(self):
        # 'Показать' верний слой Layout'a
        self.label1.setVisible(True)
        self.label2.setVisible(True)
        self.slider.setVisible(True)
        self.volumeBtn.setVisible(True)
        self.hslider.setVisible(True)
        # 'Показать' нижний слой Layout'a
        openBtn.setVisible(True)
        self.imageBtn.setVisible(True)
        self.backBtn.setVisible(True)
        self.playBtn.setVisible(True)
        self.forwardBtn.setVisible(True)
        self.screenBtn.setVisible(True)
        self.themeBtn.setVisible(True)

    def change_to_dark_theme(self):
        new_dark_gardient = '''
        QWidget{
            background: #3E52BD;
            background: -webkit-linear-gradient(top left, #3E52BD, #A35C35);
            background: -moz-linear-gradient(top left, #3E52BD, #A35C35);
            background: linear-gradient(to bottom right, #3E52BD, #A35C35);
        }
        '''
        dark = '#0D1117'
        new_dark_config = '''
        QPushButton{
            border: none;
            margin: 0px;
            padding: 0px;
            background-color: %s;
        }
        QPushButton:hover{
            background-color: #B4B4B4 ;
            border-radius:7px;
            width: 30px;
        }
        ''' % dark

        config = '''QPushButton{
        border: none;
        margin: 0px;
        padding: 0px;
        background-color:#F0F0F0;
        }
        QPushButton:hover{
        background-color: #B4B4B4;
        border-radius:7px;
        width: 30px;
        }
        '''

        if self.themeBtn.objectName() == 'default':
            self.setStyleSheet(f"background-color: {dark};")
            self.imageBtn.setStyleSheet(new_dark_config)
            self.themeBtn.setStyleSheet(new_dark_config)
            self.themeBtn.setIcon(QIcon(resource_path(r'ico/default.png')))
            self.themeBtn.setIconSize((QSize(18, 18)))
            self.screenBtn.setStyleSheet(new_dark_config)
            self.playBtn.setStyleSheet(new_dark_config)
            self.backBtn.setStyleSheet(new_dark_config)
            self.forwardBtn.setStyleSheet(new_dark_config)
            self.volumeBtn.setStyleSheet(new_dark_config)
            self.blankBtn.setStyleSheet(new_dark_config)
            openBtn.setStyleSheet(new_dark_config)
            self.themeBtn.setObjectName('dark')
        else:
            self.setStyleSheet(f"background-color: #F0F0F0;")
            self.imageBtn.setStyleSheet(config)
            self.themeBtn.setStyleSheet(config)
            self.themeBtn.setIcon(QIcon(resource_path(r'ico/dark_mode.png')))
            self.themeBtn.setIconSize((QSize(18, 18)))
            self.screenBtn.setStyleSheet(config)
            self.playBtn.setStyleSheet(config)
            self.backBtn.setStyleSheet(config)
            self.forwardBtn.setStyleSheet(config)
            self.volumeBtn.setStyleSheet(config)
            self.blankBtn.setStyleSheet(config)
            openBtn.setStyleSheet(config)
            self.themeBtn.setObjectName('default')

    # Функия для полноэкранного режима
    def fullscreen(self):
        if self.screenBtn.objectName() == 'fullscreen':
            self.showMaximized()
            self.screenBtn.setObjectName('normal_screen')
            self.screenBtn.setToolTip('Возвращения окна стандартного режима')
            self.screenBtn.setIcon(QIcon(resource_path(r'ico\norm_screen.png')))
        # elif self.one_moreBtn.objectName() == 'normal_screen':
        else:
            self.screenBtn.setObjectName('fullscreen')
            self.screenBtn.setIcon(QIcon(resource_path(r'ico\fullscreen.png')))
            self.screenBtn.setToolTip('Переключить на полноэкранный размер')
            self.showNormal()

    # Функия для кнопки громкости (проявляет слайдер)
    def volume(self):
        if self.volumeBtn.objectName() == 'volume_btn':
            self.mediaPlayer.setMuted(True)
            self.volumeBtn.setObjectName('btn')
            self.volumeBtn.setIcon(QIcon(resource_path(r'ico\vol_muted.png')))
        else:
            self.volumeBtn.setObjectName('volume_btn')
            self.mediaPlayer.setMuted(False)
            self.volumeBtn.setIcon(QIcon(resource_path(r'ico\volume1.png')))

    # Проверка громкости
    def volume_check(self):
        if self.mediaPlayer.volume() == 0:
            self.volumeBtn.setIcon(QIcon(resource_path(r'ico\vol_muted.png')))
        if self.mediaPlayer.isMuted():
            self.volumeBtn.setIcon(QIcon(resource_path(r'ico\vol_muted.png')))

    # Функция для снижения громкости
    def min_volume(self):
        vol = self.mediaPlayer.volume()
        vol = min(vol-5, 100)
        self.mediaPlayer.setVolume(vol)
        volume_state = self.hslider.sliderPosition()
        volume_state = min(volume_state - 5, self.hslider.sliderPosition())
        self.hslider.setSliderPosition(volume_state)
        if self.mediaPlayer.volume() == 0 or self.mediaPlayer.isMuted():
            self.volumeBtn.setIcon(QIcon(resource_path(r'ico\vol_muted.png')))
        else:
            self.volumeBtn.setIcon(QIcon(resource_path(r'ico\volume1.png')))

    # Функция для увелечения громкости
    def plus_volume(self):
        vol = self.mediaPlayer.volume()
        vol = max(vol + 5, 0)
        self.mediaPlayer.setVolume(vol)
        volume_state = self.hslider.sliderPosition()
        volume_state = max(volume_state + 5, self.hslider.sliderPosition())
        self.hslider.setSliderPosition(volume_state)

    # Функция которая меняет состояние кнопок
    def mediastate_changed(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(QIcon(resource_path(r'ico\pause.png')))
            self.playBtn.setIconSize(QSize(40, 40))
        else:
            self.playBtn.setIcon(QIcon(resource_path(r'ico\play.png')))
            self.playBtn.setIconSize(QSize(40, 40))

    # Функция которая отвечает за перемотку с помощью слайдера и которая выводит прошедшее время с начала записи
    def position_changed(self, position):
        self.slider.setValue(position)
        self.label1.setText('%d:%02d /' % (int(position / 60000), int((position / 1000) % 60)))

    # Функция отвечающая за нахождения общей продолжительности записи и ввывод ее в надпись
    def duration_changed(self, duration):
        self.slider.setRange(0, duration)
        durations = self.mediaPlayer.duration()
        self.label2.setText('%d:%02d' % (int(durations / 60000), int((durations / 1000) % 60)))

    # передает значение позиции в медиаплеер
    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    # Обработчик ошибки
    def handle_errors(self):
        self.playBtn.setEnabled(False)

    # Функция управляющая за передачу в слайдер громкости
    def position_volume(self, position):
        self.hslider.setValue(position)

    # Функция задающаю общую грумкость
    def duration_volume(self):
        self.hslider.setRange(0, 100)

    # Функция для регулирования громкости
    def set_volume_position(self, position):
        self.mediaPlayer.setVolume(position)
        if self.mediaPlayer.volume() == 0 or self.mediaPlayer.isMuted():
            self.volumeBtn.setIcon(QIcon(resource_path(r'ico\vol_muted.png')))
        elif self.mediaPlayer.volume() != 0 or self.mediaPlayer.isMuted():
            self.volumeBtn.setIcon(QIcon(resource_path(r'ico\volume1.png')))

    # перемотка назад на 10сек
    def go_back(self):
        pos = self.mediaPlayer.position()
        pos = min(pos - 10000, pos)
        self.mediaPlayer.setPosition(pos)

    # перемотка вперед на 10сек
    def go_forward(self):
        pos = self.mediaPlayer.position()
        pos = max(pos + 10000, pos)
        self.mediaPlayer.setPosition(pos)

    def buttonHandler(self):
        grab = self.grab()
        filename = f"img-{time.strftime('%Y-%m-%d-%H-%M-%S')}"
        grab.save(resource_path(f'screens/{filename}.png'), 'png')
        #os.startfile(resource_path(f'screens/{filename}.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FirstWindow()
    print("--- {} секунд ---".format(time.time() - start_time))
    window.show()
    sys.exit(app.exec_())
    # основное окно готово !!;)
