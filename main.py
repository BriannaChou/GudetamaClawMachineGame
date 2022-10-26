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
import pygame

#Intialize the Pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

#Clock
clock = pygame.time.Clock()

#Background
background = pygame.image.load("../images/GudetamaBackground.jpg")
background = pygame.transform.scale(background,(800,600))

#Caption
pygame.display.set_caption("Gudetama Claw Machine Game")

#Claw Machine
clawMachineIcon = pygame.image.load("../images/ClawMachineIcon.png")
clawMachineIcon = pygame.transform.scale(clawMachineIcon,(100,150))

#Joystick
joystickDefaultIcon = pygame.image.load("../images/joystick_default.png")
joystickDefaultIcon = pygame.transform.scale(joystickDefaultIcon,(250,250))
joystickLeft = pygame.image.load("../images/joystick_left.png")
joystickLeft = pygame.transform.scale(joystickLeft,(250,250))
joystickRight = pygame.image.load("../images/joystick_right.png")
joystickRight = pygame.transform.scale(joystickRight,(250,250))

#Buttons
dropButton_x, dropButton_y, dropButton_width, dropButton_height = 10, 440, 50, 50
dropButton = pygame.Rect(dropButton_x, dropButton_y, dropButton_width, dropButton_height)

x = 0
y = 0
z=0
x_change = 0
y_change = 0
joystick_sprites = dict()
def claw(x, y):
    screen.blit(clawMachineIcon, (x, y))

def joystickDefault(x,y,z):
    joystickImageNames = [joystickDefaultIcon, joystickLeft, joystickRight]
    if z==0:
        screen.blit(joystickImageNames[z], (x, y))
    elif z==1:
        screen.blit(joystickImageNames[z], (x, y))
    elif z==2:
        screen.blit(joystickImageNames[z], (x, y))

#Game loop
gaming = True
while gaming:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
                z=1
            elif event.key == pygame.K_RIGHT:
                x_change = 5
                z=2
        else:
            z=0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    x += x_change
    ##
    joystickDefault(-50, 450,z)
    claw(x, y)
    pygame.display.update()
    clock.tick(60)
