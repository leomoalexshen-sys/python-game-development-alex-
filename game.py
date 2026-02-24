import pgzrun
from random import randint

TITLE = "Shoot the Alien"
WIDTH = 500
HEIGHT = 500

message = "Click the Alien!"
score = 0

alien = Actor('alien')

def draw():
    # global score
    screen.clear()
    screen.fill((128, 0, 0))
    alien.draw()
    screen.draw.text(message, center=(250, 30), fontsize=40, color="white")
    screen.draw.text("Score:"+str(score), center=(250, 470), fontsize=35, color="yellow")

def place_alien():
    alien.x = randint(50, WIDTH - 50)
    alien.y = randint(50, HEIGHT - 50)

def on_mouse_down(pos):
    global message, score
    if alien.collidepoint(pos):
        message = "Good Shot!"
        score = score +1
        place_alien()
    else:
        message = "You Missed"

place_alien()
pgzrun.go()