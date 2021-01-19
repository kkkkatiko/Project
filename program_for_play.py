import sys
import pygame
import PG_file

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from play import Ui_MainWindow1
from PyQt5.QtCore import QTimer


class MyWidget1(QMainWindow, Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.easy_btn.clicked.connect(self.openEasyGame)
        self.medium_btn.clicked.connect(self.openMediumGame)
        self.play_btn_3.clicked.connect(self.openHardGame)
    

    def openEasyGame(self):
        PG_file.drawgame()

    def openMediumGame(self):
        PG_file.drawgame1()

    def openHardGame(self):
        PG_file.drawgame2()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex1 = MyWidget1()
    ex1.show()
    sys.exit(app.exec_())
