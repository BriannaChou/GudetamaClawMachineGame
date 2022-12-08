"""Kayla and Brianna - We need to get buttons working on main page
    Player cannot move claw until start button is pressed
    Makes rules / how to play page
    Eggs to appear
    Egg work with claw
    Have claw grab egg
    Have egg open
    Have egg added to Gudex
    Have state of main page not change (like the eggs) until all eggs are caught,
        and then reset
    Having a total number of Gudetama eggs caught out of the total in the game
   Logan - Linking the Gudex and Rules/How to Play page to the main page
"""

import random
import webbrowser
import pygame
import os
from tkinter import messagebox

# Initialize the Pygame
pygame.init()

# Create lists for Gudex
global Gudemon_List
global Gudemon_Caught

Gudemon_Caught = []
Gudemon_List = ["ramenGudetama", "curryGudetama", "eggGudetama", "toyGudetama", "hamburgerGudetama", "lifePerserverGudetama", "goldenTrophyGudetama"]

# Create the screen
screen_width, screen_height = 800, 600
window_width, window_height = 900, 600
screen = pygame.display.set_mode((window_width, window_height))

# Clock
clock = pygame.time.Clock()

# Background
background = pygame.image.load("images/GudetamaBackground.jpg")
background = pygame.transform.scale(background, (800, 600))

# Caption
pygame.display.set_caption("Gudetama Claw Machine Game")

# Claw Machine
clawMachineIcon = pygame.image.load("images/ClawMachineIcon.png")
clawMachineIcon = pygame.transform.scale(clawMachineIcon, (100, 150))
clawMachineIconBlue = pygame.image.load("images/ClawWithBlueEgg.png")
clawMachineIconBlue = pygame.transform.scale(clawMachineIconBlue, (100, 150))
clawMachineIconGold = pygame.image.load("images/ClawWithGoldEgg.png")
clawMachineIconGold = pygame.transform.scale(clawMachineIconGold, (100, 150))
clawMachineIconRed = pygame.image.load("images/ClawWithRedEgg.png")
clawMachineIconRed = pygame.transform.scale(clawMachineIconRed, (100, 150))
clawMachineIconYellow = pygame.image.load("images/ClawWithYellowEgg.png")
clawMachineIconYellow = pygame.transform.scale(clawMachineIconYellow, (100, 150))

# Joystick
joystickDefaultIcon = pygame.image.load("images/joystick_default.png")
joystickDefaultIcon = pygame.transform.scale(joystickDefaultIcon, (100, 100))
joystickLeft = pygame.image.load("images/joystick_left.png")
joystickLeft = pygame.transform.scale(joystickLeft, (100, 100))
joystickRight = pygame.image.load("images/joystick_right.png")
joystickRight = pygame.transform.scale(joystickRight, (100, 100))

# Start Button
startButton_x, startButton_y, startButton_width, startButton_height = 350, 550, 100, 40
start_rect = pygame.Rect(startButton_x, startButton_y, startButton_width, startButton_height)
startButton = pygame.image.load("images/StartButton.png")
startButton = pygame.transform.scale(startButton, (startButton_width, startButton_height))
onStartButton, START_GAME = False, False

# Drop Claw Button
dropButton_x, dropButton_y, dropButton_width, dropButton_height = 600, 550, 100, 40
drop_rect = pygame.Rect(dropButton_x, dropButton_y, dropButton_width, dropButton_height)
dropButton = pygame.image.load("images/DropButton.png")
dropButton = pygame.transform.scale(dropButton, (dropButton_width, dropButton_height))
onDropButton, START_DROP = False, False
isDropping = True

# Rules and Gudex Icons
icon_width, icon_height = 80, 90
rules_x, rules_y = 810, 20
gudex_x, gudex_y = 810, 150
rules = pygame.image.load("images/RulesAndHowToPlayIcon.png")
rules = pygame.transform.scale(rules, (icon_width, icon_height))
rules_rect = pygame.Rect(rules_x, rules_y, icon_width, icon_height)
gudex = pygame.image.load("images/GudexIcon.png")
gudex = pygame.transform.scale(gudex, (icon_width, icon_height))
gudex_rect = pygame.Rect(gudex_x, gudex_y, icon_width, icon_height)
onRules = False
onGudex = False

# Other Variables
joystick_sprites = dict()
joy_z = 0
left_click = 1
gaming = True
GAME_COMPLETE = False
font = pygame.font.SysFont(None, 40) #For text popup
text = font.render("You Caught a Gudetama!", True, (0, 255, 0))

# Claw Variables
claw_x, claw_y = 0, 0
claw_xChange, claw_yChange = 0, 0

# Eggs
egg_width = 47
egg_height = 60
eggDimensions = (egg_width, egg_height)
blue = pygame.image.load("images/blueEgg.png")
blue = pygame.transform.scale(blue, eggDimensions)
red = pygame.image.load("images/redEgg.png")
red = pygame.transform.scale(red, eggDimensions)
yellow = pygame.image.load("images/yellowEgg.png")
yellow = pygame.transform.scale(yellow, eggDimensions)
gold = pygame.image.load("images/goldenEgg_special.png")
gold = pygame.transform.scale(gold, eggDimensions)

# Other Egg Variables
eggGroup = pygame.sprite.Group()
numEggs = 20 #WILL be set at 20!!!!
eggBounds = []
eggColors = []
FILLED = False
NO_EGG_GRABBED = True #Need this for popup window
CAUGHT_EGG = None
CAUGHT_EGG_COLOR = None


# Egg Sprite Class
class Egg(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        self.image = image

        self.rect = self.image.get_rect()


# Functions
def joystickDefault(x, y, z):
    joystickImageNames = [joystickDefaultIcon, joystickLeft, joystickRight]
    if z == 0:
        screen.blit(joystickImageNames[z], (x, y))
    elif z == 1:
        screen.blit(joystickImageNames[z], (x, y))
    elif z == 2:
        screen.blit(joystickImageNames[z], (x, y))


def claw(x, y):
    if isDropping and y < 325:
        screen.blit(clawMachineIcon, (x, y))
    else:
        if CAUGHT_EGG_COLOR == 0:
            screen.blit(clawMachineIconBlue, (x, y))
        elif CAUGHT_EGG_COLOR == 1:
            screen.blit(clawMachineIconRed, (x, y))
        elif CAUGHT_EGG_COLOR == 2:
            screen.blit(clawMachineIconYellow, (x, y))
        elif CAUGHT_EGG_COLOR == 3:
            screen.blit(clawMachineIconGold, (x, y))
        else:
            screen.blit(clawMachineIcon, (x, y))


def add_sprites():
    global FILLED
    global eggBounds
    global eggColors
    color = None
    eggValue = None
    current = 0
    collision_bounds = []
    failures = 0
    max_failures = 50

    while current < numEggs:
        overlap = False
        rand = random.randint(1, 20)
        if rand < 11:
            color = blue
            eggValue = 0
        elif rand < 17:
            color = red
            eggValue = 1
        elif rand < 20:
            color = yellow
            eggValue = 2
        else:
            color = gold
            eggValue = 3

        egg = Egg(color)
        egg.rect.x = random.randint(17, screen_width - egg_width - 13)
        egg.rect.y = random.randint(350, 500 - egg_height)
        egg_rect = pygame.Rect(egg.rect.x, egg.rect.y, egg_width, egg_height)

        for rectangle in collision_bounds:
            if rectangle.colliderect(egg_rect):
                overlap = True

        if not overlap:
            eggGroup.add(egg)
            collision_bounds.append(egg_rect)
            eggBounds.append(pygame.Rect(egg.rect.x + egg_width // 4, egg.rect.y + egg_height - 1, egg_width // 2, egg_height))
            eggColors.append(eggValue)
            current += 1
            failures = 0
        else:
            failures += 1

        if failures == max_failures:
            current = 0
            collision_bounds = []
            eggGroup.empty()
            eggBounds = []
            eggColors = []

    FILLED = True


def button_clicked_on(button, on_button):
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


def drop_claw(is_dropping, x, y, width, height):
    global NO_EGG_GRABBED
    global CAUGHT_EGG_COLOR
    x_change, y_change, drop_complete = 0, 0, False
    if y > 350 or not NO_EGG_GRABBED:
        is_dropping = False
    if is_dropping:
        y_change = 5

        clawMidpoint = (x + width // 2, y + height)
        if NO_EGG_GRABBED:
            index = 0
            for egg in eggBounds:
                if egg.collidepoint(clawMidpoint):
                    CAUGHT_EGG = eggGroup.sprites()[index]
                    eggGroup.remove(CAUGHT_EGG)
                    eggBounds.pop(index)
                    CAUGHT_EGG_COLOR = eggColors[index]
                    eggColors.pop(index)
                    add_Gudemon(CAUGHT_EGG_COLOR)
                    NO_EGG_GRABBED = False
                    break
                index += 1

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
    if NO_EGG_GRABBED:
        messagebox.showinfo('Nice Try!', 'You missed the egg! Try again!')
    else:
        messagebox.showinfo('Congradulations!', 'You caught a Gudetama. Check out the Gudex to see it!')
    start_game = False
    start_drop = False
    dropping = True
    game_complete = False
    caught_egg = None
    caught_egg_color = None
    no_egg_grabbed = True
    global FILLED
    if len(eggGroup) == 0:
        FILLED = False
    return start_game, start_drop, dropping, game_complete, caught_egg, caught_egg_color, no_egg_grabbed
# LOGAN: Function for adding gudemon to caught list if they are not yet added or returning nothing
def add_Gudemon(color):
    #legendary 3, rare 2, uncommon 1, common 0
    # Things to be added:
    #way to have pull in the data set instead of explictily calling parts of list
    # Way to sort either through sorting the list but better to have sort methods through the XML AND STYLESHEET
    if color == 3:
        #rand = randomint()
        Gudemon = Gudemon_List[6]
    if color == 2:
        rand = random.randint(4, 5)
        Gudemon = Gudemon_List[rand]
    if color == 1:
        #rand = randomint()
        Gudemon = Gudemon_List[3]
    if color == 0:
        rand = random.randint(0, 2)
        Gudemon = Gudemon_List[rand]
    if Gudemon not in Gudemon_Caught:
        # add new gudemon
        Gudemon_Caught.append(Gudemon)
        # iterate through guedom and concatenate each for the text files to and new file
        finalString = ""
        finalString = """<?xml version="1.0" encoding="UTF-8"?>
        <?xml-stylesheet type="text/css" href="GudexStyleSheet.css"?>
        <Gudex>"""
        for gudemonName in Gudemon_Caught:
            tempFile= open("GudemonTXTs/"+gudemonName+".txt", "r")
            finalString = finalString + tempFile.read()
            tempFile.close()
        # replace gudex with format of gudex + new out put
        finalString = finalString + """
        </Gudex>"""
        gudex1 = open("GudemonTXTs/Gudex.xml", "w")
        gudex1.write(finalString)
        gudex1.close()

# Gameplay
while gaming:
    event = pygame.event.poll()
    position = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    screen.fill((244, 238, 174))
    screen.blit(background, (0, 0))
    if event.type == pygame.QUIT:
        gaming = False
    joystickDefault(25, 500, joy_z)
    claw(claw_x, claw_y)
    screen.blit(startButton, (startButton_x, startButton_y))
    screen.blit(dropButton, (dropButton_x, dropButton_y))
    if not FILLED:
        add_sprites()
    eggGroup.draw(screen)
    screen.blit(rules, (rules_x, rules_y))
    screen.blit(gudex, (gudex_x, gudex_y))

    if not START_GAME:
        onStartButton = button_clicked_on(start_rect, onStartButton)
        if onStartButton:
            START_GAME, onStartButton = button_clicked_off(start_rect, START_GAME, onStartButton)
        # allow to check rules & gudex here
        onRules = button_clicked_on(rules_rect, onRules)
        if onRules:
            webbrowser.open(
                "http://localhost:63342/GudetamaClawMachineGame/rulesAndHowTo.html?_ijt=8alueor662jvoeuikcccm1g9v2&_ij_reload=RELOAD_ON_SAVE")
            onRules = False
        onGudex = button_clicked_on(gudex_rect, onGudex)
        if onGudex:
            webbrowser.open(
                "file:///" + os.path.join(os.path.dirname(__file__), 'GudemonTXTs/Gudex.xml'))
            onGudex = False

    if START_GAME:
        if not START_DROP:
            onDropButton = button_clicked_on(drop_rect, onDropButton)
            if onDropButton:
                START_DROP, onDropButton = button_clicked_off(drop_rect, START_DROP, onDropButton)
            claw_xChange, joy_z = move_claw(claw_x)
            claw_x += claw_xChange
            joystickDefault(25, 500, joy_z)
            claw(claw_x, claw_y)

        if START_DROP:
            isDropping, claw_xChange, claw_yChange, GAME_COMPLETE = drop_claw(isDropping, claw_x, claw_y, 100, 150)
            claw_x += claw_xChange
            claw_y += claw_yChange
            claw(claw_x, claw_y)

        if GAME_COMPLETE:
            START_GAME, START_DROP, isDropping, GAME_COMPLETE, CAUGHT_EGG, CAUGHT_EGG_COLOR, NO_EGG_GRABBED = game_reset()
    pygame.display.update()
    clock.tick(60)
