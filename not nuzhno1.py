import sys
import pygame
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from play import Ui_MainWindow1
from PyQt5.QtCore import QTimer
 
class Game():
    def __init__(self):
        pygame.init()
        self.game_init()
 
    def game_init(self):
        size = width, height = 600, 400
        self.screen = pygame.display.set_mode(size)
        self.x_pos = 15
        self.v = 10
        self.x = 1
        self.clock = pygame.time.Clock()
 
    def loop(self, window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.x = event.pos
                self.x_pos = 0
        self.screen.fill([0, 0, 255])
        if self.x != 1:
            pygame.draw.circle(self.screen, (255, 255, 0), self.x, self.x_pos)
            self.x_pos += self.v * self.clock.tick()/1000
        pygame.display.update()
        return False
 
class MyWidget2(QMainWindow, Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        self.dialog = MyWidget2()
 
    def init_ui(self):
        self.easy_btn.clicked.connect(self.openGame)
        self.show()
 
    def init_pygame(self):
        self.game = Game()
        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(10)
 
    def pygame_loop(self):
        if self.game.loop(self):
            self.timer.stop()
            self.timer.disconnect()
            pygame.quit()
 
    def openGame(self):
        self.init_pygame()
        self.dialog.close()
 
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget2()
    result = app.exec_()
    sys.exit(result)
