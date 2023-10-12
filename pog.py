from pygame import *
from random import randint
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back =(200,255,255)
win_width = 700
win_height = 500
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
ball = Player('ball.png', 350, win_height - 550, 80, 80, 5)
racket1 = Player('tennis.png', 600, win_height - 400, 80, 80, 10)
racket2 = Player('tennis.png', 5, win_height - 100, 80, 80, 10)
game = True  
finish = False
clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.fill(back)
        ball.update()
        ball.reset()
        racket1.update_l()
        racket2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        racket1.reset()
        racket2.reset()
    
    display.update()
    clock.tick(FPS)
