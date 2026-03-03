import pyzrun
from random import randint

width=600
height=500
score=0
game_over=False

bee=Actor('bumble_bee')
bee.pos=200, 200
flower=Actor("flower")
flower.pos=100, 100

def update()
    

def draw()
    screen.blit('background', (0,0))
    flower.draw()
    bumble_bee.draw()
    screen.draw.text('SCORE: '+str(score), color="black", midtop=(width/2, 10), fontsize=30)
    if game_over:
        screen.fill('black')
        screen.draw.text('TIME IS UP! YOUR FINAL SCORE IS: '+str(score), midtop=(width/2, 10), fontsize=50, color='red')

def place_flower():
    flower.x=randint(width-50, height-50)
    flower.y=randint(width-50, height-50)