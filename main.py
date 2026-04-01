# imports

import pygame
import time
import random

# game start

pygame.init()


# sounds

crash_noise = pygame.mixer.Sound('crash_sound.wav')


# game sizing
display_width = 800
display_height = 600

cX = 81
cY = 133

cEx = 80
cEy = 120


startbX = 24
startbY = 27

stopbX = 24
stopbY = 27

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
red_select = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green_select = (0, 255, 0)
green = (25, 145, 25)
blue_grey = (21, 27, 36)
crash_red = (194, 69, 45)
space = (8, 5, 10)

# game display stuff
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("A Bit Spacey")

clock = pygame.time.Clock()

# starting/stopping buttons
startImg = pygame.image.load('start_button.png')
startImg = pygame.transform.scale(startImg, (startbX, startbY))

stopImg = pygame.image.load('stop_button.png')
stopImg = pygame.transform.scale(stopImg, (stopbX, stopbY))

# car image stuff
carImg = pygame.image.load('spaceship.png')
carImg = pygame.transform.scale(carImg, (cX, cY))

bg = pygame.image.load('background.png')
bg = pygame.transform.scale(bg, (display_width, display_height))

crashbg = pygame.image.load('crash.png')
crashbg = pygame.transform.scale(crashbg, ((display_width/2), (display_height/2)))

ts = pygame.image.load('title_screen.png')
ts = pygame.transform.scale(ts, (800, 600))


carEnemy = ['pship.png', 'gship.png', 'rship.png', 'rocksm.png', 'rockmm.png']


pause = False


# Definitions of functions

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, white)
    gameDisplay.blit(text, (0, 0))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)

    game_loop()


def crashed():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load('crash_theme.wav')
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            print('event')
            if event.type == pygame.QUIT:
                quit()


        crashed = pygame.font.Font('freesansbold.ttf', 115)
        crashed_text = pygame.font.SysFont(None, 120)
        crashed_title = crashed_text.render("You Crashed!!", True, white)
        gameDisplay.blit(crashed_title, (150, 200))
        button("Try Again?", 160, 350, 200, 100, green_select, green, game_loop)
        button("...quit...", 440, 350, 200, 100, red_select, red, quitgame)
        pygame.display.update()
        clock.tick(15)




def button(msg, x, y, w, h, sc, dc, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    print(mouse)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, sc, (x, y, w, h))
        if click[False] == 1 and action != None:
            action()
            if action == "Play":
                game_loop()
            elif action == "Quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, dc, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 35)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    button_lable = pygame.font.SysFont(None, 50)
    button_title = button_lable.render(msg, True, black)
    gameDisplay.blit(button_title, textRect)


def quitgame():
    pygame.quit()
    quit()


def unpaused():
    global pause
    pause = False
    print("GAME IS LIVE")

def paused():
    while pause:
        for event in pygame.event.get():
            print('event')
            if event.type == pygame.QUIT:
                quit()
        paused = pygame.font.Font('freesansbold.ttf', 115)
        pause_text = pygame.font.SysFont(None, 120)
        pause_title = pause_text.render("Paused", True, white)
        gameDisplay.blit(pause_title, (260, 200))
        print("GAME IS PAUSED")

        button("Continue", 160, 350, 200, 100, green_select, green, unpaused)
        button("...quit...", 440, 350, 200, 100, red_select, red, quitgame)

     #   keyStates = pygame.key.get_pressed()

      #  if keyStates[pygame.K_SPACE]:
      #      unpaused()

        pygame.display.update()
        clock.tick(15)


def game_intro():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load('title_theme.wav')
    pygame.mixer.music.play(-1)
    intro = True
    while intro:
        gameDisplay.blit(ts,(0,0))
        for event in pygame.event.get():
            print('event')
            if event.type == pygame.QUIT:
                quit()

        intro = pygame.font.Font('freesansbold.ttf', 115)
        intro_text = pygame.font.SysFont(None, 110)
        intro_title = intro_text.render("A Bit Spacey", True, white)
        gameDisplay.blit(intro_title, (160, 250))

        button("LAUNCH!", 160, 350, 170, 80, green_select, green, game_loop)
        button("...quit...", 440, 350, 170, 80, red_select, red, quitgame)

        pygame.display.update()
        clock.tick(15)


# game play
def game_loop():
    global pause
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load('main_theme.wav')
    pygame.mixer.music.play(-1)

    x = (display_width * 0.48)
    y = (display_height * 0.7)

    xMove = 0
    yMove = 0

    carE_startx = random.randrange(0, display_width)
    carE_starty = -600
    carE_speed = 5
    carE_width = 100
    carE_height = 100
    carEdisplay = random.choice(carEnemy)
    print("RANDOM")

    dodged = 0

    gameExit = False

    while not gameExit:
        gameDisplay.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keyStates = pygame.key.get_pressed()
        if keyStates[pygame.K_LEFT] or keyStates[pygame.K_a]:
            xMove = -10
        elif keyStates[pygame.K_RIGHT] or keyStates[pygame.K_d]:
            xMove = 10
        else:
            xMove = 0


        x += xMove

        if keyStates[pygame.K_SPACE]:
         #   keyStates=pygame.K_a
            pause = True
            paused()



        carEsurface = pygame.transform.scale(pygame.image.load(carEdisplay), (cEx, cEy))
        gameDisplay.blit(carEsurface, (carE_startx, carE_starty))
        carE_starty += carE_speed
        car(x, y)
        things_dodged(dodged)

        if x > display_width - 81 or x < 0:
            crashed()

        if carE_starty > display_height:
            carEdisplay = random.choice(carEnemy)
            print("RANDOM")
            carE_starty = 0 - carE_height
            carE_startx = random.randrange(0, display_width)
            dodged += 1
            carE_speed += 0.20

        if y > carE_starty and y < carE_starty + carE_height:
            print('y crossover')

            if x > carE_startx and x < carE_startx + carE_width or x + cX > carE_startx and x + cX < carE_startx + carE_width:
                print('x crossover')
                gameDisplay.blit(crashbg, (carE_startx-carE_width, carE_starty))
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(crash_noise)
                crashed()

        pygame.display.update()
        clock.tick(60)


unpaused()
game_intro()
game_loop()
pygame.quit()
quit()
