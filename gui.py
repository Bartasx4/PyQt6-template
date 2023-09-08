from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QMainWindow,
)


class Gui(QMainWindow):
    track = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Last Heard')
        self.resize(1200, 700)
        # self.setGeometry(100, 100, 1200, 800)
