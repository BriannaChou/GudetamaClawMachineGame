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

'''
import pygame

#Intialize the Pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

#Clock
clock = pygame.time.Clock()

#Background
background = pygame.image.load("images/GudetamaBackground.jpg")
background = pygame.transform.scale(background,(800,600))

#Caption
pygame.display.set_caption("Gudetama Claw Machine Game")

#Claw Machine
clawMachineIcon = pygame.image.load("images/ClawMachineIcon.png")
clawMachineIcon = pygame.transform.scale(clawMachineIcon,(100,150))

#Joystick
joystickDefaultIcon = pygame.image.load("images/joystick_default.png")
joystickDefaultIcon = pygame.transform.scale(joystickDefaultIcon,(250,250))
joystickLeft = pygame.image.load("images/joystick_left.png")
joystickLeft = pygame.transform.scale(joystickLeft,(250,250))
joystickRight = pygame.image.load("images/joystick_right.png")
joystickRight = pygame.transform.scale(joystickRight,(250,250))

#Buttons
startButton_x, startButton_y, startButton_width, startButton_height = 300, 320, 150, 50
startButton = pygame.Rect(startButton_x, startButton_y, startButton_width, startButton_height)

dropButton_x, dropButton_y, dropButton_width, dropButton_height = 700, 500, 50, 50
dropButton = pygame.Rect(dropButton_x, dropButton_y, dropButton_width, dropButton_height)

#Button Variables
onDropButton = False
START_DROP = False
isDropping = True

#General Variables
x = 0
y = 0
z=0
x_change = 0
y_change = 0
joystick_sprites = dict()
LEFT = 1


#Functions
def button_clicked_on(button, on_button):   # Works for start & drop buttons -> take <button> parameter to specify
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT \
            and button.collidepoint(position[0], position[1]):
        on_button = True
    return on_button

def button_clicked_off(button, start_function, on_button):
    if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT \
            and button.collidepoint(position[0], position[1]):
        start_function = True
    elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT \
            and not button.collidepoint(position[0], position[1]):
        on_button = False
    return start_function, on_button

def drop_claw(is_dropping, x1, y1):
    if y1 > 400:
        is_dropping = False
    if is_dropping:
        y1 += y_change
    elif not is_dropping and y1 != 20:
        y1 -= y_change
    elif y1 == 20 and x1 < 680:
        x1 += x_change
    claw(x1, y1)
    return is_dropping

def claw(x1, y1):
    screen.blit(clawMachineIcon, (x1, y1))

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
    position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
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

    if not START_DROP:
        onDropButton = button_clicked_on(dropButton, onDropButton)
        if onDropButton:
            START_DROP, onDropButton = button_clicked_off(dropButton, START_DROP, onDropButton)
        #claw_x = move_claw(claw_x)
        #pygame.draw.rect(screen, (255, 255, 255), (claw_x, claw_y, claw_width, claw_height))
    if START_DROP:
        isDropping = drop_claw(isDropping, x, y)
        claw(x, y)

        #pygame.draw.rect(screen, (255, 255, 255), (claw_x, claw_y, claw_width, claw_height))
    pygame.draw.rect(screen, (255, 255, 255), dropButton)
    pygame.display.update()
    clock.tick(60)

'''
