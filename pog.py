from pygame import *
from random import randint
from time import time as timer

back =(200,255,255)
win_width = 700
win_height = 500
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
window.fill(back)

game = True
clock = time.Clock()
FPS = 60

while game :
    for e in event.get():
        if e.type == QUIT:
            run = False