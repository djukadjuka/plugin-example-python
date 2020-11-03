import os

from PyQt5.QtCore import QResource
from PyQt5.QtWidgets import QApplication, QWidget

from epp.view.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()

    app.exec_()
