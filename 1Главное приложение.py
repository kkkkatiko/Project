import sys

#импорт программы с графическим интерфейсом, сделанном в QtDesigner 
from PyQt5.QtWidgets import QApplication, QMainWindow
from main import Ui_MainWindow

from program_for_rules import MyWidget2
from program_for_play import MyWidget1
from program_for_statis import MyWidget3


# Наследуется от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.dialog1 = MyWidget1()
        self.dialog2 = MyWidget2()
        self.dialog3 = MyWidget3()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow, 
        # остальное без изменений
        self.setupUi(self)
        #проверка нажатий кнопок
        self.play_btn.clicked.connect(self.showDialog1)
        self.pushButton_4.clicked.connect(self.showDialog2)
        self.time_btn.clicked.connect(self.showDialog3)

    def showDialog1(self):
        self.dialog1.show()

    def showDialog2(self):
        self.dialog2.show()

    def showDialog3(self):
        self.dialog3.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
