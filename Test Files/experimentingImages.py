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
"""import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
background = pygame.image.load('../images/GudetamaBackground.jpg')
pygame.display.set_caption('A bit of Gudetama')

'''black = (0, 0, 0)
white = (255, 255, 255)'''

clock = pygame.time.Clock()
crashed = False
gudetamaImg = pygame.image.load('../images/ClawMachineIcon.png')
joystick_default = pygame.image.load('../images/joystick_default.png')
joystick_left = pygame.image.load('../images/joystick_left.png')
joystick_right = pygame.image.load('../images/joystick_right.png')
gudetamaImg = pygame.transform.scale(gudetamaImg,(100,150))

def car(x, y):
    gameDisplay.blit(gudetamaImg, (x, y))
x=0
y=0
x_change = 0
car_speed = 0

while not crashed:
    gameDisplay.fill(0,0,0)
    gameDisplay.blit(background, (display_width, display_height))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True

        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        ######################
    ##
    x += x_change
    ##
    car(x, y)
    pygame.display.update()
    clock.tick(60)

'''if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        x_change = -5
    elif event.key == pygame.K_RIGHT:
        x_change = 5
if event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        x_change = 0 '''


Displays a button (white rectangle) and starts a game when clicked
Start of game gets rid of button and displays a claw (white square) that can be moved left and right
Another button present (red square) to drop claw at any point
    Clicking button will drop claw straight down, move it back up immediately, and
    to the right (back to original, starting position)"""


