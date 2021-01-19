import sys
import pygame
import PG_file

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from rules import Ui_MainWindow1
from PyQt5.QtCore import QTimer


class MyWidget2(QMainWindow, Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget2()
    ex.show()
    sys.exit(app.exec_())
