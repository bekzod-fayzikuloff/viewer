from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout,
                             QVBoxLayout, QLabel, QSlider, QFileDialog,)
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont
from PyQt5.QtCore import Qt, QUrl, QSize, QEvent
import keyboard
import time


# полный список используемых модулей(библиотек) для создания GUI интерфейса используется модуль PyQt5 и его классы и также модуль : sys, time, keyboard
#_____________________________#
start_time = time.time()
# также я добавил таймер для того чтобы знать сколько выполняется скрипт
# (если запустить код пару раз то время будет отображаться корректне)


class Window(QWidget):
    '''
       В этом классе описывается внешний вид, логика и функционал моего видеоплеера версии 0.01
       постораюсь по мере возможности улучшать свой проект добавляя функционал и
       удобства , это \'документация\', надеюсь моя программа тебе
       понравится
       P.S знаю что много плохого кода. сорри
    '''

    def __init__(self):
        '''Инициализируем Класс нашего главного окна и в нем прописывем основные характеристики нашего окна (размер , цвет , "тайтл" и вызывает методы
         в которых отслеживаются события(перемещение мыши) и прописан внешний вид интерфейса '''

        StyleSheet = '''TitleBar {
        background-color:#B34EE9;}
        '''
        super().__init__()

        self.setWindowTitle('v_|0.0.1|')
        self.setGeometry(350, 200, 1280, 666)
        self.setWindowIcon(QIcon(r'ico\gold.png'))

        pal = self.palette()
        pal.setColor(QPalette.Window, QColor('#F0F0F0'))
        self.setPalette(pal)
        self.setStyleSheet(StyleSheet)
        self.setMouseTracking(True)
        self.setCursor(Qt.PointingHandCursor)
        self.init_ui()


    def event(self, e):
        '''Метод обработчик который фиксирует взаимодействия с клавиатурой и мышью для манипуляцией
        над процессом показа виде (изменения громкости , перемотка и остановка'''
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
            if e.key() == Qt.Key_0:
                self.blef_win_on()
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

        # создание button(кнопки открыть)
        openBtn = QPushButton()
        openBtn.setStyleSheet(config)
        openBtn.setIcon(QIcon(r'ico\folders.png'))
        openBtn.setIconSize(QSize(20, 20))
        openBtn.clicked.connect(self.open_file)
        openBtn.setToolTip('Открытие папок для просмотра файлов')
        openBtn.setToolTipDuration(2500)

        # создание button (кнопки для запуска)
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setFlat(True)
        self.playBtn.setStyleSheet(config)
        self.playBtn.setIcon(QIcon(r'ico\play.png'))
        self.playBtn.setIconSize(QSize(40, 40))
        self.playBtn.clicked.connect(self.play_video)

        # создание button(кнопки для перемотки вперед)
        self.forwardBtn = QPushButton()
        self.forwardBtn.setEnabled(False)
        self.forwardBtn.setIcon(QIcon(r'ico\forward.png'))
        self.forwardBtn.setStyleSheet(config)
        self.forwardBtn.setIconSize(QSize(20, 20))
        self.forwardBtn.clicked.connect(self.forward)

        # создание button (для перемотки назад)
        self.backBtn = QPushButton()
        self.backBtn.setEnabled(False)
        self.backBtn.setIcon(QIcon(r'ico\backward .png'))
        self.backBtn.setStyleSheet(config)
        self.backBtn.setIconSize(QSize(20, 20))
        self.backBtn.clicked.connect(self.backward)

        # для volume(громкости)
        self.nextBtn = QPushButton()
        self.nextBtn.setObjectName('volume_btn')
        self.nextBtn.setIcon(QIcon(r'ico\volume1.png'))
        self.nextBtn.setStyleSheet(config)
        self.nextBtn.setIconSize(QSize(17, 17))
        self.nextBtn.clicked.connect(self.volume)

        # настройка button(кнопок)
        self.one_moreBtn = QPushButton()
        self.one_moreBtn.setObjectName('fullscreen')
        self.one_moreBtn.setStyleSheet(config)
        self.one_moreBtn.setIcon(QIcon(r'ico\fullscreen.png'))
        self.one_moreBtn.setIconSize(QSize(19, 19))
        self.one_moreBtn.clicked.connect(self.fullscreen)
        self.one_moreBtn.setToolTip('Переключить на полноэкранный размер')
        self.one_moreBtn.setToolTipDuration(2500)

# ----- кнопки для пустых мест ----- #
        self.btn1 = QPushButton()
        self.btn1.setEnabled(False)
        self.btn1.setStyleSheet(conf_for_blank)

        self.btn2 = QPushButton()
        self.btn2.setEnabled(False)
        self.btn2.setStyleSheet(conf_for_blank)
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
        # self.hslider.setStyleSheet(sliders_style)
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
        hboxLayout2.addWidget(self.nextBtn)
        hboxLayout2.addWidget(self.hslider)

        # добавления виджетов в hbox layout
        hboxLayout.addWidget(self.btn1)
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.backBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.forwardBtn)
        hboxLayout.addWidget(self.one_moreBtn)
        hboxLayout.addWidget(self.btn2)

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
        try:
            keyboard.add_hotkey('up', self.plus_volume)
            keyboard.add_hotkey('down', self.min_volume)
            keyboard.add_hotkey('left', self.go_back)
            keyboard.add_hotkey('right', self.go_forward)
        except:
            pass

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

    # Пустая функция для кнопки вперед
    def forward(self):
        self.go_forward_with_key()

    # Пустая функция для кнопки назад
    def backward(self):
        self.go_back_with_key()

    def blef_win(self):
        # Сокрытие вернего слоя Layout'a
        self.label1.hide()
        self.label2.hide()
        self.slider.hide()
        self.nextBtn.hide()
        self.hslider.hide()
        # Сокрытие нижнего слоя Layout'a
        openBtn.hide()
        self.btn1.hide()
        self.backBtn.hide()
        self.playBtn.hide()
        self.forwardBtn.hide()
        self.one_moreBtn.hide()
        self.btn2.hide()

    def blef_win_on(self):
        # 'Показать' верний слой Layout'a
        self.label1.setVisible(True)
        self.label2.setVisible(True)
        self.slider.setVisible(True)
        self.nextBtn.setVisible(True)
        self.hslider.setVisible(True)
        # 'Показать' нижний слой Layout'a
        openBtn.setVisible(True)
        self.btn1.setVisible(True)
        self.backBtn.setVisible(True)
        self.playBtn.setVisible(True)
        self.forwardBtn.setVisible(True)
        self.one_moreBtn.setVisible(True)
        self.btn2.setVisible(True)

    # Функия для полноэкранного режима
    def fullscreen(self):
        if self.one_moreBtn.objectName() == 'fullscreen':
            self.showMaximized()
            self.one_moreBtn.setObjectName('normal_screen')
            self.one_moreBtn.setToolTip('Возвращения окна стандартного режима')
            self.one_moreBtn.setIcon(QIcon(r'ico\norm_screen.png'))
        elif self.one_moreBtn.objectName() == 'normal_screen':
            self.one_moreBtn.setObjectName('fullscreen')
            self.one_moreBtn.setIcon(QIcon(r'ico\fullscreen.png'))
            self.one_moreBtn.setToolTip('Переключить на полноэкранный размер')
            self.showNormal()

    # Функия для кнопки громкости (проявляет слайдер)
    def volume(self):
        if self.nextBtn.objectName() == 'volume_btn':
            self.mediaPlayer.setMuted(True)
            self.nextBtn.setObjectName('btn')
            self.nextBtn.setIcon(QIcon(r'ico\vol_muted.png'))
        else:
            self.nextBtn.setObjectName('volume_btn')
            self.mediaPlayer.setMuted(False)
            self.nextBtn.setIcon(QIcon(r'ico\volume1.png'))


    # Проверка громкости
    def volume_check(self):
        if self.mediaPlayer.volume() == 0:
            self.nextBtn.setIcon(QIcon(r'ico\vol_muted.png'))
        if self.mediaPlayer.isMuted() == True:
            self.nextBtn.setIcon(QIcon(r'ico\vol_muted.png'))

    # Функция для снижения громкости
    def min_volume(self):
        vol = self.mediaPlayer.volume()
        vol = min(vol-5, 100)
        self.mediaPlayer.setVolume(vol)
        volume_state = self.hslider.sliderPosition()
        volume_state = min(volume_state - 5, self.hslider.sliderPosition())
        self.hslider.setSliderPosition(volume_state)
        if self.mediaPlayer.volume() == 0 or self.mediaPlayer.isMuted():
            self.nextBtn.setIcon(QIcon(r'ico\vol_muted.png'))
        else:
            self.nextBtn.setIcon(QIcon(r'ico\volume1.png'))

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
            self.playBtn.setIcon(QIcon(r'ico\pause.png'))
            self.playBtn.setIconSize(QSize(40, 40))
        else:
            self.playBtn.setIcon(QIcon(r'ico\play.png'))
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

    # Обработчик ощибки
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
            self.nextBtn.setIcon(QIcon(r'ico\vol_muted.png'))
        elif self.mediaPlayer.volume() != 0 or self.mediaPlayer.isMuted() == False:
            self.nextBtn.setIcon(QIcon(r'ico\volume1.png'))

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    print("--- %s seconds ---" % (time.time() - start_time))
    window.show()
    sys.exit(app.exec_())
# основное окно готово !!;)
