import sys

from PyQt6.QtWidgets import QApplication

from gui import Gui


if __name__ == '__main__':
    app = QApplication([])
    gui = Gui()
    gui.show()

    sys.exit(app.exec())
