import pgzrun
from random import randint
TITLE="Good Shot"
WIDTH=500
HEIGHT = 500
message = ""
alien = Actor('alien')

def draw():
   screen.clear()
   screen.fill (color = (128, 0, 0))
   alien.draw()
   screen.draw.text(message, center = (400, 0), fontsize= 30)

def place_alien():
   alien.x = randint (50, WIDTH-50)
   alien.y = randint (50, WIDTH-50)

def on_mouse_down (pos):
    global message
    if alien.collidepoint (pos):
        message = "Good Shot"
        place_alien ()
    else:
        message = "You missed"

place_alien ()
pgzrun.go ()
