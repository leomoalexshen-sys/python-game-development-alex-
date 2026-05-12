import pgzrun
import random

r = random.randint(1, 255)
g = random.randint(1, 255)
b = random.randint(1, 255)

health=20

WIDTH = 626
HEIGHT = 352
game_over = False

player = Actor("actor")
player.pos = 50, 50

debug_timer=60

thing1 = Actor("lava")
thing1.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
thing1_speed = 5

thing2 = Actor("lava")
thing2.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
thing2_speed = 3

thing3 = Actor("lava")
thing3.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
thing3_speed = 1

thing4 = Actor("lava")
thing4.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
thing4_speed = 2

thing5 = Actor("lava")
thing5.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
thing5_speed=4

finishing=Actor("finish")
finishing.pos=615, 345

def update():
    global thing1_speed, thing2_speed, thing3_speed, thing4_speed, thing5_speed, debug_timer, health, hit_lava1, hit_lava2, hit_lava3, hit_lava4, hit_lava5

    hit_lava1 = player.colliderect(thing1)
    hit_lava2 = player.colliderect(thing2)
    hit_lava3 = player.colliderect(thing3)
    hit_lava4 = player.colliderect(thing4)
    hit_lava5 = player.colliderect(thing5)

    if keyboard.left:
        player.x-=2
    elif keyboard.right:
        player.x+=2
    elif keyboard.down:
        player.y+=2
    elif keyboard.up:
        player.y-=2

    thing1.y += thing1_speed

    if thing1.y >= HEIGHT:
        thing1.y = HEIGHT
        thing1_speed = -thing1_speed

    if thing1.y <= 0:
        thing1.y = 0
        thing1_speed = -thing1_speed

    thing2.y += thing2_speed

    if thing2.y >= HEIGHT:
        thing2.y = HEIGHT
        thing2_speed = -thing2_speed

    if thing2.y <= 0:
        thing2.y = 0
        thing2_speed = -thing2_speed

    thing3.y += thing3_speed

    if thing3.y >= HEIGHT:
        thing3.y = HEIGHT
        thing3_speed = -thing3_speed

    if thing3.y <= 0:
        thing3.y = 0
        thing3_speed = -thing3_speed

    thing4.y += thing4_speed

    if thing4.y >= HEIGHT:
        thing4.y = HEIGHT
        thing4_speed = -thing4_speed

    if thing4.y <= 0:
        thing4.y = 0
        thing4_speed = -thing4_speed


    thing5.y += thing5_speed

    if thing5.y >= HEIGHT:
        thing5.y = HEIGHT
        thing5_speed = -thing5_speed

    if thing5.y <= 0:
        thing5.y = 0
        thing5_speed = -thing5_speed

    if debug_timer > 0:
        debug_timer-=1
    if health == 0:
        debug_timer = 60
    if debug_timer == 0:
        if hit_lava1 or hit_lava2 or hit_lava3 or hit_lava4 or hit_lava5:
            health-=1
            player.pos=50, 50
            debug_timer=60

def draw():
    global game_over, r, g, b, health

    hit_lava1 = player.colliderect(thing1)
    hit_lava2 = player.colliderect(thing2)
    hit_lava3 = player.colliderect(thing3)
    hit_lava4 = player.colliderect(thing4)
    hit_lava5 = player.colliderect(thing5)

    screen.blit("background", (0, 0))
    player.draw()
    thing1.draw()
    thing2.draw()
    thing3.draw()
    thing4.draw()
    thing5.draw()
    finishing.draw()

    screen.draw.text("Your Health is " + str(health) + " right now", fontsize = 20, color = "black", bottomleft=(10, 342))

    finished=player.colliderect(finishing)

    if finished:
        game_over = True

    if game_over:
        screen.fill((r, g, b))
        screen.draw.text("CONGRATULATIONS!!!", fontsize=30, color="black", midtop = (WIDTH/2, 10))

    if health == 0:
        screen.fill("black")
        screen.draw.text("YOU DIED", fontsize=30, color="red", midtop = (WIDTH/2, 10))
        health=0

    if player.y == 0:
        player.pos = player.x, 0
    elif player.y == 352:
        player.pos = player.x, 352
    elif player.x == 626:
        player.pos = 626, player.y
    elif player.x == 0:
        player.pos = 0, player.y

pgzrun.go()
