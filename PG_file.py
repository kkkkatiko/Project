import random
import pygame
import pygame.freetype
import sys
import time
import sqlite3



class goodgame:
    def __init__(self, n = 3):
        self.n = n
        self.table = [[int(((i * n + i / n + j) % (n * n) // 1 + 1)) for j in range(n * n)] for i in range(n * n)]

    def show(self):
        for i in range(self.n **  2):
            print(self.table[i])

    def peremena(self):
        self.table = list(map(list, zip(*self.table)))

    def swap_str(self):
        area = random.randrange(0, self.n)
        line1 = random.randrange(0, self.n)
        number1 = area * self.n + line1
        line2 = random.randrange(0, self.n)
        while (line1 == line2):
            line2 = random.randrange(0, self.n)
        number2 = area * self.n + line2
        self.table[number1], self.table[number2] = self.table[number2], self.table[number1]

    def transport(self):
        area1 = random.randrange(0, self.n)
        area2 = random.randrange(0, self.n)
        while (area1 == area2):
            area2 = random.randrange(0, self.n)
        for i in range(0, self.n):
            number11, number22 = area1 * self.n + i, area2 * self.n + i
            self.table[number11], self.table[number22] = self.table[number22], self.table[number11]

    def swap_col(self):
        goodgame.peremena(self)
        goodgame.swap_str(self)
        goodgame.peremena(self)

    def swap_row(self):
        goodgame.peremena(self)
        goodgame.transport(self)
        goodgame.peremena(self)


    def mix(self):
        mixen = ['self.peremena()', 'self.swap_row()', 'self.swap_col()','self.transport()', 'self.swap_str()']
        for i in range(1, 120):
            s = random.randrange(0, len(mixen))
            eval(mixen[s])
        for g in self.table:
            print(g)

    def easytab(self):
        for i in range(8):
            while self.table[i].count(0) < 5:
                s = random.randrange(0, 9)
                if self.table[i][s] != 0:
                    self.table[i][s] = 0
        for o in range(5):
            f = random.randrange(0, 9)
            self.table[8][f] = 0
        for g in self.table:
            print(g)
        return self.table

    def midtab(self):
        for i in range(9):
            while self.table[i].count(0) < 6:
                s = random.randrange(0, 9)
                if self.table[i][s] != 0:
                    self.table[i][s] = 0
        for g in self.table:
            print(g)
        return self.table

    def hardtab(self):
        for i in range(7):
            while self.table[i].count(0) < 6:
                s = random.randrange(0, 9)
                if self.table[i][s] != 0:
                    self.table[i][s] = 0
        while self.table[7].count(0) < 7:
            f = random.randrange(0, 9)
            if self.table[7][f] != 0:
                self.table[7][f] = 0
        while self.table[8].count(0) < 7:
            f = random.randrange(0, 9)
            if self.table[8][f] != 0:
                self.table[8][f] = 0
        for g in self.table:
            print(g)
        return self.table


class Board:
    def __init__(self, width, height, a):
        self.width = width
        self.height = height
        self.board = a
        self.left = 10
        self.top = 10
        self.cell_size = 50
        self.a = 0
        self.b = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        x, y = 0, 0
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255), (self.left + x + 50, self.top + y + 50, 
                            self.cell_size, self.cell_size))
                pygame.draw.rect(screen, (0, 0, 0), (self.left + x + 50, self.top + y + 50, 
                            self.cell_size, self.cell_size), 1)
                self.images_list = []
                if self.board[i][j] == 1:
                    self.im1 = pygame.image.load('2021-01-07_22-49-28.png')
                    t = self.im1.get_rect(bottomright=(self.left + x + 46 + self.cell_size, self.top + y + 47 + self.cell_size))
                    screen.blit(self.im1, t)
                    self.images_list.append(self.im1)
                elif self.board[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (self.left + x + 52, self.top + y + 52, 
                            44, 44))
                elif self.board[i][j] == 2:
                    self.im2 = pygame.image.load('2021-01-07_22-55-08.png')
                    t = self.im2.get_rect(bottomright=(self.left + x + 45 + self.cell_size, self.top + y + 47 + self.cell_size))
                    screen.blit(self.im2, t)
                    self.images_list.append(self.im2)
                elif self.board[i][j] == 3:
                    self.im3 = pygame.image.load('2021-01-07_22-57-33.png')
                    t = self.im3.get_rect(bottomright=(self.left + x + 45 + self.cell_size, self.top + y + 46 + self.cell_size))
                    screen.blit(self.im3, t)
                    self.images_list.append(self.im3)
                elif self.board[i][j] == 4:
                    self.im4 = pygame.image.load('2021-01-07_22-57-57.png')
                    t = self.im4.get_rect(bottomright=(self.left + x + 45 + self.cell_size, self.top + y + 47 + self.cell_size))
                    screen.blit(self.im4, t)
                    self.images_list.append(self.im4)
                elif self.board[i][j] == 5:
                    self.im5 = pygame.image.load('2021-01-07_22-58-32.png')
                    t = self.im5.get_rect(bottomright=(self.left + x + 48 + self.cell_size, self.top + y + 47 + self.cell_size))
                    screen.blit(self.im5, t)
                    self.images_list.append(self.im5)
                elif self.board[i][j] == 6:
                    self.im6 = pygame.image.load('2021-01-07_22-59-02.png')
                    t = self.im6.get_rect(bottomright=(self.left + x + 44 + self.cell_size, self.top + y + 47 + self.cell_size))
                    screen.blit(self.im6, t)
                    self.images_list.append(self.im6)
                elif self.board[i][j] == 7:
                    self.im7 = pygame.image.load('2021-01-07_22-59-24.png')
                    t = self.im7.get_rect(bottomright=(self.left + x + 47 + self.cell_size, self.top + y + 47 + self.cell_size))
                    screen.blit(self.im7, t)
                    self.images_list.append(self.im7)
                elif self.board[i][j] == 8:
                    self.im8 = pygame.image.load('2021-01-08_00-13-11.png')
                    t = self.im8.get_rect(bottomright=(self.left + x + 42 + self.cell_size, self.top + y + 42 + self.cell_size))
                    screen.blit(self.im8, t)
                    self.images_list.append(self.im8)
                elif self.board[i][j] == 9:
                    self.im9 = pygame.image.load('2021-01-07_22-59-53.png')
                    t = self.im9.get_rect(bottomright=(self.left + x + 49 + self.cell_size, self.top + y + 47 + self.cell_size))
                    screen.blit(self.im9, t)
                    self.images_list.append(self.im9)
                elif self.board[i][j] >= 10 and self.board[i][j] <= 20:
                    pygame.draw.rect(screen, (255, 240, 170), (self.left + x + 51, self.top + y + 51, 48, 48))
                    if self.board[i][j] == 11:
                        self.im11 = pygame.image.load('2021-01-08_18-05-34.png')
                        t = self.im11.get_rect(bottomright=(self.left + x + 46 + self.cell_size, self.top + y + 45 + self.cell_size))
                        screen.blit(self.im11, t)
                        self.images_list.append(self.im11)
                    elif self.board[i][j] == 12:
                        self.im12 = pygame.image.load('2021-01-08_18-07-16.png')
                        t = self.im12.get_rect(bottomright=(self.left + x + 43 + self.cell_size, self.top + y + 48 + self.cell_size))
                        screen.blit(self.im12, t)
                        self.images_list.append(self.im12)
                    elif self.board[i][j] == 13:
                        self.im13 = pygame.image.load('2021-01-08_18-08-07.png')
                        t = self.im13.get_rect(bottomright=(self.left + x + 44 + self.cell_size, self.top + y + 44 + self.cell_size))
                        screen.blit(self.im13, t)
                        self.images_list.append(self.im13)
                    elif self.board[i][j] == 14:
                        self.im14 = pygame.image.load('2021-01-08_18-08-52.png')
                        t = self.im14.get_rect(bottomright=(self.left + x + 43 + self.cell_size, self.top + y + 46 + self.cell_size))
                        screen.blit(self.im14, t)
                        self.images_list.append(self.im14)
                    elif self.board[i][j] == 15:
                        self.im15 = pygame.image.load('2021-01-08_18-09-20.png')
                        t = self.im15.get_rect(bottomright=(self.left + x + 48 + self.cell_size, self.top + y + 48 + self.cell_size))
                        screen.blit(self.im15, t)
                        self.images_list.append(self.im15)
                    elif self.board[i][j] == 16:
                        self.im16 = pygame.image.load('2021-01-08_18-09-52.png')
                        t = self.im16.get_rect(bottomright=(self.left + x + 43 + self.cell_size, self.top + y + 45 + self.cell_size))
                        screen.blit(self.im16, t)
                        self.images_list.append(self.im16)
                    elif self.board[i][j] == 17:
                        self.im17 = pygame.image.load('2021-01-08_18-10-19.png')
                        t = self.im17.get_rect(bottomright=(self.left + x + 45 + self.cell_size, self.top + y + 47 + self.cell_size))
                        screen.blit(self.im17, t)
                        self.images_list.append(self.im17)
                    elif self.board[i][j] == 18:
                        self.im18 = pygame.image.load('2021-01-08_18-10-41.png')
                        t = self.im18.get_rect(bottomright=(self.left + x + 47 + self.cell_size, self.top + y + 43 + self.cell_size))
                        screen.blit(self.im18, t)
                        self.images_list.append(self.im18)
                    elif self.board[i][j] == 19:
                        self.im19 = pygame.image.load('2021-01-08_18-11-06.png')
                        t = self.im19.get_rect(bottomright=(self.left + x + 45 + self.cell_size, self.top + y + 48 + self.cell_size))
                        screen.blit(self.im19, t)
                        self.images_list.append(self.im19)
                elif self.board[i][j] >= 30:
                    pygame.draw.rect(screen, (202, 231, 173), (self.left + x + 51, self.top + y + 51, 48, 48))
                    if self.board[i][j] == 33:
                        f = pygame.image.load('в.png')
                        t = f.get_rect(bottomright=(self.left + x + 45 + self.cell_size, self.top + y + 48 + self.cell_size))
                        screen.blit(f, t)
                    elif self.board[i][j] == 44:
                        f = pygame.image.load('е.png')
                        t = f.get_rect(bottomright=(self.left + x + 45 + self.cell_size, self.top + y + 48 + self.cell_size))
                        screen.blit(f, t)
                    elif self.board[i][j] == 55:
                        f = pygame.image.load('р.png')
                        t = f.get_rect(bottomright=(self.left + x + 45 + self.cell_size, self.top + y + 48 + self.cell_size))
                        screen.blit(f, t)
                    elif self.board[i][j] == 66:
                        f = pygame.image.load('н.png')
                        t = f.get_rect(bottomright=(self.left + x + 45 + self.cell_size, self.top + y + 48 + self.cell_size))
                        screen.blit(f, t)
                    elif self.board[i][j] == 77:
                        f = pygame.image.load('о.png')
                        t = f.get_rect(bottomright=(self.left + x + 45 + self.cell_size, self.top + y + 48 + self.cell_size))
                        screen.blit(f, t)
                x += self.cell_size  
            x = 0
            y += self.cell_size

                
    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - 1) // self.cell_size
        cell_y = (mouse_pos[-1] - 1) // self.cell_size
        if cell_y <= 9 and cell_y >= 1:
            if cell_x <= 9 and cell_x >= 1:
                return cell_x, cell_y
        else:
            return None
            
    def on_click(self, cell_coords):
        if self.a != cell_coords[0] or self.b != cell_coords[-1]:
            for i in range(self.height):
                for j in range(self.width):
                    if self.a - 1 == i and self.b - 1 == j:
                        if self.board[j][i] == 10:
                            self.board[j][i] = 0          
            self.a = cell_coords[0]
            self.b = cell_coords[-1]
        for i in range(self.height):
            for j in range(self.width):
                if self.a - 1 == i and self.b - 1 == j:
                    if self.board[j][i] == 0:
                        self.board[j][i] = 10
                    elif self.board[j][i] >= 11:
                        self.board[j][i] = 0
                        

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell != None:
            self.on_click(cell)

    def klava(self, num):
        self.num = num
        if self.num == 0:
            for i in range(self.height):
                for j in range(self.width):
                    if i == 2 and j == 4:
                        self.board[j][i] = 33 #v
                    elif i == 3 and j == 4:
                        self.board[j][i] = 44 #e
                    elif i == 4 and j == 4:
                        self.board[j][i] = 55 #r
                    elif i == 5 and j == 4:
                        self.board[j][i] = 66 #n
                    elif i == 6 and j == 4:
                        self.board[j][i] = 77 #o
                    else:
                        self.board[j][i] = 0
        else:
            for i in range(self.height):
                for j in range(self.width):
                    if self.board[j][i] == 10:
                        self.board[j][i] += int(num)
                    elif self.board[j][i] >= 10 and self.board[j][i] <= 10:
                        self.board[j][i] -= 10

    def proof(self, screen):
        x = self.board
        '''
        for row in range(len(x)):
            for col in range(len(x)):
                x[row][col] = x[row][col] % 10 '''
        for row in range(len(x)):
            for col in range(len(x)):
                if x[row][col] % 10 < 1 or type(x[row][col]) is not type(1):
                    print('F')
                    return False
                elif x[row][col] % 10 > len(x):
                    print('F')
                    return False
        for row in x:
            if sorted(list(set(row))) != sorted(row):
                print('F')
                return False
        cols = []
        for col in range(len(x)):
            for row in x:
                cols += [row[col] % 10]
            if sorted(list(set(cols))) != sorted(cols):
                print('F')
                return False
            cols = []
        print('T')
        return True

    def re(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board[j][i] = 10
            
def drawgame():
    example = goodgame()
    example.mix()
    pygame.init()
    pygame.display.set_caption('Судоку')
    size = width, height = 570, 570
    e = pygame.Rect(410, 18, 122, 28)
    screen = pygame.display.set_mode(size)
    pygame.mixer.init()  #музыка
    pygame.mixer.music.load('zvuk-prirodyi-reka-ptitsyi-ryadom-les-16486.ogg')
    pygame.mixer.music.play(-1, 0.0)
    board = Board(9, 9, example.easytab())   #загрузка уровней
    running = True
    x = 0
    image = pygame.image.load("0.png").convert()
    while running:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if e.collidepoint(mouse_pos):
                    if board.proof(screen) == True:
                        board.klava(0)
                        #time.sleep(3)
                        #running = False
                    else:
                        image = pygame.image.load("2021-01-18_18-24-28.png").convert()
                        image = pygame.transform.scale(image, (122, 28))

                
                board.get_click(event.pos)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            numbersss = 1
            board.klava(numbersss)
        elif keys[pygame.K_2]:
            numbersss = 2
            board.klava(numbersss)
        elif keys[pygame.K_3]:
            numbersss = 3
            board.klava(numbersss)
        elif keys[pygame.K_4]:
            numbersss = 4
            board.klava(numbersss)
        elif keys[pygame.K_5]:
            numbersss = 5
            board.klava(numbersss)
        elif keys[pygame.K_6]:
            numbersss = 6
            board.klava(numbersss)
        elif keys[pygame.K_7]:
            numbersss = 7
            board.klava(numbersss)
        elif keys[pygame.K_8]:
            numbersss = 8
            board.klava(numbersss)
        elif keys[pygame.K_9]:
            numbersss = 9
            board.klava(numbersss)
        
        background_position = [0, 0]
        background_image = pygame.image.load("fotooboi.jpg").convert()
        background_image = pygame.transform.scale(background_image, (570, 570))
        screen.blit(background_image, background_position)
        board.render(screen)
        con = sqlite3.connect("easy.sqlite")
        cur = con.cursor()
        n = [410, 18]
        screen.blit(image, n)
        board.render(screen)

        font = pygame.freetype.SysFont(None, 34)
        font.origin = True
        clock = pygame.time.Clock()
        ticks = pygame.time.get_ticks()
        ho = int(ticks / 3600000 % 60)
        seconds = int(ticks / 1000 % 60)
        minutes = int(ticks / 60000 % 24)
        out = '{ho}:{minutes:02d}:{seconds:02d}'.format(minutes = minutes, ho = ho, seconds = seconds)
        font.render_to(screen, (220, 40), out, pygame.Color(255, 255, 255))
        clock.tick(60)
        pygame.display.flip()
    x = pygame.time.get_ticks() / 1000
    cur.execute("""INSERT INTO easy VALUES(?)""", (x,))
    con.commit() 
    pygame.quit()

def drawgame1():
    example = goodgame()
    example.mix()
    pygame.init()
    pygame.display.set_caption('Судоку')
    size = width, height = 570, 570
    e = pygame.Rect(410, 18, 122, 28)
    screen = pygame.display.set_mode(size)
    pygame.mixer.init()  #музыка
    pygame.mixer.music.load('zvuk-prirodyi-reka-ptitsyi-ryadom-les-16486.ogg')
    pygame.mixer.music.play(-1, 0.0)
    board = Board(9, 9, example.midtab())   #загрузка уровней
    running = True
    x = 0
    image = pygame.image.load("0.png").convert()
    while running:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if e.collidepoint(mouse_pos):
                    if board.proof(screen) == True:
                        board.klava(0)
                        #time.sleep(3)
                        #running = False
                    else:
                        image = pygame.image.load("2021-01-18_18-24-28.png").convert()
                        image = pygame.transform.scale(image, (122, 28))

                
                board.get_click(event.pos)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            numbersss = 1
            board.klava(numbersss)
        elif keys[pygame.K_2]:
            numbersss = 2
            board.klava(numbersss)
        elif keys[pygame.K_3]:
            numbersss = 3
            board.klava(numbersss)
        elif keys[pygame.K_4]:
            numbersss = 4
            board.klava(numbersss)
        elif keys[pygame.K_5]:
            numbersss = 5
            board.klava(numbersss)
        elif keys[pygame.K_6]:
            numbersss = 6
            board.klava(numbersss)
        elif keys[pygame.K_7]:
            numbersss = 7
            board.klava(numbersss)
        elif keys[pygame.K_8]:
            numbersss = 8
            board.klava(numbersss)
        elif keys[pygame.K_9]:
            numbersss = 9
            board.klava(numbersss)
        
        background_position = [0, 0]
        background_image = pygame.image.load("fotooboi.jpg").convert()
        background_image = pygame.transform.scale(background_image, (570, 570))
        screen.blit(background_image, background_position)
        board.render(screen)

        n = [410, 18]
        screen.blit(image, n)
        board.render(screen)
        con = sqlite3.connect("medium.sqlite")
        cur = con.cursor()
        font = pygame.freetype.SysFont(None, 34)
        font.origin = True
        clock = pygame.time.Clock()
        ticks = pygame.time.get_ticks()
        ho = int(ticks / 3600000 % 60)
        seconds = int(ticks / 1000 % 60)
        minutes = int(ticks / 60000 % 24)
        out = '{ho}:{minutes:02d}:{seconds:02d}'.format(minutes = minutes, ho = ho, seconds = seconds)
        font.render_to(screen, (220, 40), out, pygame.Color(255, 255, 255))
        clock.tick(60)
        pygame.display.flip()
    x = pygame.time.get_ticks() / 1000
    cur.execute("""INSERT INTO easy VALUES(?)""", (x,))
    con.commit() 
    pygame.quit()


def drawgame2():
    example = goodgame()
    example.mix()
    pygame.init()
    pygame.display.set_caption('Судоку')
    size = width, height = 570, 570
    e = pygame.Rect(410, 18, 122, 28)
    screen = pygame.display.set_mode(size)
    pygame.mixer.init()  #музыка
    pygame.mixer.music.load('zvuk-prirodyi-reka-ptitsyi-ryadom-les-16486.ogg')
    pygame.mixer.music.play(-1, 0.0)
    board = Board(9, 9, example.hardtab())   #загрузка уровней
    running = True
    x = 0
    image = pygame.image.load("0.png").convert()
    while running:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if e.collidepoint(mouse_pos):
                    if board.proof(screen) == True:
                        board.klava(0)
                        #time.sleep(3)
                        #running = False
                    else:
                        image = pygame.image.load("2021-01-18_18-24-28.png").convert()
                        image = pygame.transform.scale(image, (122, 28))

                
                board.get_click(event.pos)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            numbersss = 1
            board.klava(numbersss)
        elif keys[pygame.K_2]:
            numbersss = 2
            board.klava(numbersss)
        elif keys[pygame.K_3]:
            numbersss = 3
            board.klava(numbersss)
        elif keys[pygame.K_4]:
            numbersss = 4
            board.klava(numbersss)
        elif keys[pygame.K_5]:
            numbersss = 5
            board.klava(numbersss)
        elif keys[pygame.K_6]:
            numbersss = 6
            board.klava(numbersss)
        elif keys[pygame.K_7]:
            numbersss = 7
            board.klava(numbersss)
        elif keys[pygame.K_8]:
            numbersss = 8
            board.klava(numbersss)
        elif keys[pygame.K_9]:
            numbersss = 9
            board.klava(numbersss)
        
        background_position = [0, 0]
        background_image = pygame.image.load("fotooboi.jpg").convert()
        background_image = pygame.transform.scale(background_image, (570, 570))
        screen.blit(background_image, background_position)
        board.render(screen)

        n = [410, 18]
        screen.blit(image, n)
        board.render(screen)
        con = sqlite3.connect("hard.sqlite")
        cur = con.cursor()
        font = pygame.freetype.SysFont(None, 34)
        font.origin = True
        clock = pygame.time.Clock()
        ticks = pygame.time.get_ticks()
        ho = int(ticks / 3600000 % 60)
        seconds = int(ticks / 1000 % 60)
        minutes = int(ticks / 60000 % 24)
        out = '{ho}:{minutes:02d}:{seconds:02d}'.format(minutes = minutes, ho = ho, seconds = seconds)
        font.render_to(screen, (220, 40), out, pygame.Color(255, 255, 255))
        clock.tick(60)
        pygame.display.flip()
    x = pygame.time.get_ticks() / 1000
    cur.execute("""INSERT INTO easy VALUES(?)""", (x,))
    con.commit()
    pygame.quit()
