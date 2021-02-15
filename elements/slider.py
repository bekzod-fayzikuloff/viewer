from PyQt5.QtWidgets import QSlider


class MySlider(QSlider):
    config = '''
    QSlider::groove:horizontal {
        border-radius: 1px;       
        height: 6px;              
        margin: -1px 0;           
    }
    QSlider::handle:horizontal {
        background-color: #98A798;
        border: 2px solid silver;
        height: 16px;     
        width: 10px;
        margin: -4px 0;     
        border-radius: 7px  ;
        padding: -4px 0px;  
    }
    QSlider::add-page:horizontal {
        background: #A6A6A6;
    }
    QSlider::sub-page:horizontal {
        background: #272A32;
    }
    '''

    def __init__(self, orient):
        super().__init__()
        self.setOrientation(orient)
        self.setRange(0, 0)
        self.setMaximumHeight(7)
        self.setStyleSheet(MySlider.config)
