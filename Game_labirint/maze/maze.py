from pygame import *#импорт библиотеки

class GameSprite(sprite.Sprite):#класс
    def __init__(self, image_sprite, img_x, img_y, speed):#ввод значений 
        super().__init__()##указывает на себя всё из класса родителя
        self.image = transform.scale(image.load(image_sprite), (65,65))#указывает на себя картинку
        self.speed = speed#указывает на себя скорость
        self.rect = self.image.get_rect()#указывает на себя
        self.rect.x = img_x#указывает на себя х
        self.rect.y = img_y#указывает на себя у

    def show_s(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x>5:
            self.rect.x -=self.speed
        if keys[K_d] and self.rect.x<win_width-80:
            self.rect.x +=self.speed
        if keys[K_w] and self.rect.y>5:
            self.rect.y -=self.speed
        if keys[K_s] and self.rect.y<win_hight-80:
            self.rect.y +=self.speed

class Enemy(GameSprite):
    napraw = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.napraw='right'
        if self.rect.x >= win_width-85:
            self.napraw = 'left'
        if self.napraw == 'left':
            self.rect.x-=self.speed
        else:
            self.rect.x+=self.speed
        
class Wall(sprite.Sprite):
    def __init__(self, col_r, col_g, col_b, wall_x, wall_y, wall_hight, wall_width):
        super().__init__()
        self.col_r=col_r
        self.col_g=col_g
        self.col_b=col_b
        self.wall_x=wall_x
        self.wall_y=wall_y
        self.wall_hight=wall_hight
        self.wall_width=wall_width

        self.image = Surface((self.wall_width, self.wall_hight))
        self.image.fill((self.col_r,self.col_g,self.col_b))

        self.rect=self.image.get_rect()
        self.rect.x=wall_x
        self.rect.y=wall_y

    def show_w(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

w1=Wall(123,234,213, 100,30, 350,30)
w2=Wall(123,234,213, 215,100, 450,30)
w3=Wall(123,234,213, 100 ,0, 30,262)
w4=Wall(123,234,213, 330,30, 350,30)
w5=Wall(123,234,213, 445,100, 450,30)
w6=Wall(123,234,213, 560,365, 30,500)

win_width = 700
win_hight = 500

window = display.set_mode((win_width, win_hight))
display.set_caption("Лабиринт")

background = transform.scale(image.load("background.jpg"), (win_width,win_hight))

player = Player('hero.png',5, win_hight-70, 4)
monster = Enemy('cyborg.png', win_width-80, 280, 2)
finish_s = GameSprite('treasure.png', win_width-120, win_hight -80, 0)

game = True
finish = False

clock = time.Clock()

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

while game:
    for i in event.get():
        if i.type==QUIT:
            game=False

    if finish!=True:
        window.blit(background,(0,0))
        player.show_s()
        monster.show_s()
        finish_s.show_s()
        w1.show_w()
        w2.show_w()
        w3.show_w()
        w4.show_w()
        w5.show_w()
        w6.show_w()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5)or sprite.collide_rect(player, w6):
            finish=True
            window.blit(lose,(200,200))

        if sprite.collide_rect(player, finish_s):
            game=False
            window.blit(win,(200,200))

        player.update()
        monster.update()

    display.update()
    clock.tick(60)