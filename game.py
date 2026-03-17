import pgzrun
from random import randint

width=600
height=500
score=0
game_over=False

bee=Actor('bee')
bee.pos=200, 200
flower=Actor("flower")
flower.pos=100, 100

def update():
    global score

    if keyboard.left:
        bee.x=bee.x-1

    elif keyboard.right:
        bee.x=bee.x+1

    elif keyboard.up:
        bee.y=bee.y-1

    elif keyboard.down:
        bee.y=bee.y+1

    flower_collected=bee.colliderect(flower)
    if flower_collected:
        score=score+1
        place_flower()

def place_flower():
    flower.x=randint(70, height-50)
    flower.y=randint(70, height-50)

def time_up():
    global game_over
    game_over = True

timer=0

def draw():
    global timer
    screen.blit('background', (0,0))
    flower.draw()
    bee.draw()
    screen.draw.text('SCORE: '+str(score), color="black", midtop=(width/2, 10), fontsize=30)
    screen.draw.text('time left: '+str(timer), color='black', midtop=(width/2, 50), fontsize=20)

    if game_over:
        screen.fill('black')
        screen.draw.text('TIME IS UP! YOUR FINAL SCORE IS: '+str(score), midtop=(width/2, 10), fontsize=50, color='red')
    timer=timer+0.016666

clock.schedule(time_up, 60.0)

pgzrun.go()
