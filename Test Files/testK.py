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

# Initialize the Pygame
pygame.init()

# Create the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

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

# Joystick
joystickDefaultIcon = pygame.image.load("images/joystick_default.png")
joystickDefaultIcon = pygame.transform.scale(joystickDefaultIcon, (250, 250))
joystickLeft = pygame.image.load("images/joystick_left.png")
joystickLeft = pygame.transform.scale(joystickLeft, (250, 250))
joystickRight = pygame.image.load("images/joystick_right.png")
joystickRight = pygame.transform.scale(joystickRight, (250, 250))

# Other Variables
joystick_sprites = dict()
joy_z = 0
left_click = 1
gaming = True

# Start Button
startButton_x, startButton_y, startButton_width, startButton_height = 400, 500, 50, 50
startButton = pygame.Rect(startButton_x, startButton_y, startButton_width, startButton_height)
onStartButton, START_GAME = False, False

# Drop Claw Button
dropButton_x, dropButton_y, dropButton_width, dropButton_height = 10, 440, 50, 50
dropButton = pygame.Rect(dropButton_x, dropButton_y, dropButton_width, dropButton_height)
onDropButton, START_DROP = False, False
isDropping = True

# Claw Variables
claw_x, claw_y = 0, 0
claw_xChange, claw_yChange = 0, 0


#Functions
def joystickDefault(x,y,z):
    joystickImageNames = [joystickDefaultIcon, joystickLeft, joystickRight]
    if z==0:
        screen.blit(joystickImageNames[z], (x, y))
    elif z==1:
        screen.blit(joystickImageNames[z], (x, y))
    elif z==2:
        screen.blit(joystickImageNames[z], (x, y))

def claw(x, y):
    screen.blit(clawMachineIcon, (x, y))

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
    '''
    Wasn't able to figure out how to do the bounds using this so temporarily commented out
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and x > 0:
            change = -5
            z = 1
        elif event.key == pygame.K_RIGHT and x < screen_width - 60:
            change = 5
            z = 2
    #else:
    #    z = 0
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            change = 0
            z = 0
    '''
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

# Not sure if this works
def drop_claw(is_dropping, x, y):
    if y > 400:
        is_dropping = False
    if is_dropping:
        y_change = 5
    elif not is_dropping and y != 20:
        y_change = -5
    elif y == 20 and x > 0:
        x_change = -5
    return is_dropping, x_change, y_change


# Gameplay
while gaming:
    event = pygame.event.poll()
    position = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    #screen.blit(background, (0, 0))
    if event.type == pygame.QUIT:
        gaming = False

    if not START_GAME:
        onStartButton = button_clicked_on(startButton, onStartButton)
        if onStartButton:
            START_GAME, onStartButton = button_clicked_off(startButton, START_GAME, onStartButton)
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), startButton)
    if START_GAME:
        claw_xChange, joy_z = move_claw(claw_x)
        claw_x += claw_xChange
        screen.blit(background, (0, 0))
        joystickDefault(-50, 450, joy_z)
        claw(claw_x, claw_y)
    pygame.display.update()
    clock.tick(60)
