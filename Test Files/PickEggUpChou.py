"""This file is specifically for experimenting with egg images, and
having the claw pick the egg up and go back to default position
"""
import pygame
import random

# Initialize the Pygame
pygame.init()

# Create the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Clock
clock = pygame.time.Clock()

# Background
background = pygame.image.load("../images/GudetamaBackground.jpg")
background = pygame.transform.scale(background, (800, 600))

# Caption
pygame.display.set_caption("Gudetama Claw Machine Game")

# Claw Machine
clawMachineIcon = pygame.image.load("../images/ClawMachineIcon.png")
clawMachineIcon = pygame.transform.scale(clawMachineIcon, (100, 150))
clawMachineIconBlue = pygame.image.load("../images/ClawWithBlueEgg.png")
clawMachineIconBlue = pygame.transform.scale(clawMachineIconBlue, (100, 150))
clawMachineIconGold = pygame.image.load("../images/ClawWithGoldEgg.png")
clawMachineIconGold = pygame.transform.scale(clawMachineIconGold, (100, 150))
clawMachineIconRed = pygame.image.load("../images/ClawWithRedEgg.png")
clawMachineIconRed = pygame.transform.scale(clawMachineIconRed, (100, 150))
clawMachineIconYellow = pygame.image.load("../images/ClawWithYellowEgg.png")
clawMachineIconYellow = pygame.transform.scale(clawMachineIconYellow, (100, 150))


# Joystick
joystickDefaultIcon = pygame.image.load("../images/joystick_default.png")
joystickDefaultIcon = pygame.transform.scale(joystickDefaultIcon, (250, 250))
joystickLeft = pygame.image.load("../images/joystick_left.png")
joystickLeft = pygame.transform.scale(joystickLeft, (250, 250))
joystickRight = pygame.image.load("../images/joystick_right.png")
joystickRight = pygame.transform.scale(joystickRight, (250, 250))

# Other Variables
joystick_sprites = dict()
joy_z = 0
left_click = 1
gaming = True
GAME_COMPLETE = False

# Start Button
startButton_x, startButton_y, startButton_width, startButton_height = 350, 550, 50, 25
startButton = pygame.Rect(startButton_x, startButton_y, startButton_width, startButton_height)
onStartButton, START_GAME = False, False

# Drop Claw Button
dropButton_x, dropButton_y, dropButton_width, dropButton_height = 650, 550, 50, 25
dropButton = pygame.Rect(dropButton_x, dropButton_y, dropButton_width, dropButton_height)
onDropButton, START_DROP = False, False
isDropping = True

# Claw Variables
claw_x, claw_y = 0, 0
claw_xChange, claw_yChange = 0, 0


# Functions
def joystickDefault(x, y, z):
    joystickImageNames = [joystickDefaultIcon, joystickLeft, joystickRight]
    if z == 0:
        screen.blit(joystickImageNames[z], (x, y))
    elif z == 1:
        screen.blit(joystickImageNames[z], (x, y))
    elif z == 2:
        screen.blit(joystickImageNames[z], (x, y))

 #need to update this for when egg is caught!
def claw(x, y, initialNum):
    #This is only for TESTING reasons for experimenting with claw images!
    if isDropping and y<325:
        screen.blit(clawMachineIcon, (x, y))
    else:
        if isDropping == False and initialNum == 0:
            screen.blit(clawMachineIconBlue, (x, y))
        elif isDropping == False and initialNum == 1:
            screen.blit(clawMachineIconGold, (x, y))
        elif isDropping == False and initialNum == 2:
            screen.blit(clawMachineIconRed, (x, y))
        elif isDropping == False and initialNum == 3:
            screen.blit(clawMachineIconYellow, (x, y))


def button_clicked_on(button, on_button):   # Works for start & drop buttons -> take <button> parameter to specify
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == left_click \
            and button.collidepoint(position[0], position[1]):
        on_button = True
    return on_button


def button_clicked_off(button, start_function, on_button):
    if event.type == pygame.MOUSEBUTTONUP and event.button == left_click \
            and button.collidepoint(position[0], position[1]):
        start_function = True
    elif event.type == pygame.MOUSEBUTTONUP and event.button == left_click \
            and not button.collidepoint(position[0], position[1]):
        on_button = False
    return start_function, on_button


def move_claw(x):
    if keys[pygame.K_LEFT] and x > 0:
        change = -5
        z = 1
    elif keys[pygame.K_RIGHT] and x < screen_width - 100:
        change = 5
        z = 2
    else:
        change = 0
        z = 0
    return change, z


def drop_claw(is_dropping, x, y):
    x_change, y_change, drop_complete = 0, 0, False
    if y > 325:   #Where claw goes back up
        is_dropping = False
    if is_dropping:
        y_change = 5
    elif not is_dropping and y != 0:
        y_change = -5
    elif y == 0 and x > 0:
        x_change = -5
    if not is_dropping and y == 0 and x == 0:
        drop_complete = True
    if x_change == 0:
        pygame.draw.rect(screen, (0, 0, 0), (x + 47, 0, 7, y))
    return is_dropping, x_change, y_change, drop_complete


def game_reset():
    start_game = False
    start_drop = False
    dropping = True
    game_complete = False
    return start_game, start_drop, dropping, game_complete

num = random.Random().randrange(0, 4) #Deciding which image to do
# Gameplay
while gaming:
    event = pygame.event.poll()
    position = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    screen.blit(background, (0, 0))
    if event.type == pygame.QUIT:
        gaming = False
    joystickDefault(-50, 450, joy_z)
    claw(claw_x, claw_y, num)
    pygame.draw.rect(screen, (255, 255, 255), startButton)
    pygame.draw.rect(screen, (255, 0, 0), dropButton)

    if not START_GAME:
        onStartButton = button_clicked_on(startButton, onStartButton)
        if onStartButton:
            START_GAME, onStartButton = button_clicked_off(startButton, START_GAME, onStartButton)

    if START_GAME:
        if not START_DROP:
            onDropButton = button_clicked_on(dropButton, onDropButton)
            if onDropButton:
                START_DROP, onDropButton = button_clicked_off(dropButton, START_DROP, onDropButton)
            claw_xChange, joy_z = move_claw(claw_x)
            claw_x += claw_xChange
            joystickDefault(-50, 450, joy_z)
            claw(claw_x, claw_y, num)

        if START_DROP:
            isDropping, claw_xChange, claw_yChange, GAME_COMPLETE = drop_claw(isDropping, claw_x, claw_y)
            claw_x += claw_xChange
            claw_y += claw_yChange
            claw(claw_x, claw_y, num)

        if GAME_COMPLETE:
            START_GAME, START_DROP, isDropping, GAME_COMPLETE = game_reset()
    pygame.display.update()
    clock.tick(60)
