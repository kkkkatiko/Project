import sys
import sqlite3

#импортирую программу с графическим интерфейсом, сделанном в QtDesigner 
from PyQt5.QtWidgets import QApplication, QMainWindow
from statis import Ui_MainWindow



# Наследуется от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget3(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        con = sqlite3.connect("easy.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM easy""").fetchall()
        a = []
        a1 = 0
        for i in range(len(result)):
            if list(result[i])[0] != ' ':
                a.append(list(result[i])[0])
            else:
                a1 += 1
        a.sort()
        a = a[:3]
        for i in range(a1):
            a.append('')
        while len(a) < 3:
            a.append('')
        self.one_easy.setText(str(a[0]))
        self.two_easy.setText(str(a[1]))
        self.three_easy.setText(str(a[2]))


        con = sqlite3.connect("medium.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM easy""").fetchall()
        b = []
        b1 = 0
        for i in range(len(result)):
            if list(result[i])[0] != ' ':
                b.append(list(result[i])[0])
            else:
                b1 += 1
        b.sort()
        b = b[:3]
        for i in range(b1):
            b.append('')
        while len(b) < 3:
            b.append('')
        self.one_medium.setText(str(b[0]))
        self.two_medium.setText(str(b[1]))
        self.three_medium.setText(str(b[2]))


        con = sqlite3.connect("hard.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM easy""").fetchall()
        c = []
        c1 = 0
        for i in range(len(result)):
            if list(result[i])[0] != ' ':
                c.append(list(result[i])[0])
            else:
                c1 += 1
        c.sort()
        c = c[:3]
        for i in range(c1):
            c.append('')
        while len(c) < 3:
            c.append('')
        self.one_hard.setText(str(c[0]))
        self.two_hard.setText(str(c[1]))
        self.three_hard.setText(str(c[2]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget3()
    ex.show()
    sys.exit(app.exec_())
