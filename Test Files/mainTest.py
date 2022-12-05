import random
import pygame

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

# Start Button
startButton_x, startButton_y, startButton_width, startButton_height = 350, 550, 100, 40
start_rect = pygame.Rect(startButton_x, startButton_y, startButton_width, startButton_height)
startButton = pygame.image.load("../images/StartButton.png")
startButton = pygame.transform.scale(startButton, (startButton_width, startButton_height))
onStartButton, START_GAME = False, False

# Drop Claw Button
dropButton_x, dropButton_y, dropButton_width, dropButton_height = 600, 550, 100, 40
drop_rect = pygame.Rect(dropButton_x, dropButton_y, dropButton_width, dropButton_height)
dropButton = pygame.image.load("../images/DropButton.png")
dropButton = pygame.transform.scale(dropButton, (dropButton_width, dropButton_height))
onDropButton, START_DROP = False, False
isDropping = True

# Other Variables
joystick_sprites = dict()
joy_z = 0
left_click = 1
gaming = True
GAME_COMPLETE = False

# Claw Variables
claw_x, claw_y = 0, 0
claw_xChange, claw_yChange = 0, 0

# Eggs
egg_width = 47
egg_height = 60
eggDimensions = (egg_width, egg_height)
blue = pygame.image.load("../images/blueEgg.png")
blue = pygame.transform.scale(blue, eggDimensions)
red = pygame.image.load("../images/redEgg.png")
red = pygame.transform.scale(red, eggDimensions)
yellow = pygame.image.load("../images/yellowEgg.png")
yellow = pygame.transform.scale(yellow, eggDimensions)
gold = pygame.image.load("../images/goldenEgg_special.png")
gold = pygame.transform.scale(gold, eggDimensions)

# Other Egg Variables
eggGroup = pygame.sprite.Group()
current = 0
numEggs = 20
eggBounds = []
eggColors = []
FILLED = False
NO_EGG_GRABBED = True
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
        else:
            screen.blit(clawMachineIconGold, (x, y))


def add_sprites():
    global current
    global FILLED
    global eggBounds
    global eggColors
    color = None
    eggValue = None
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
        egg.rect.x = random.randint(0, screen.get_width() - egg_width)
        egg.rect.y = random.randint(350, 500 - egg_height)
        egg_rect = pygame.Rect(egg.rect.x, egg.rect.y, egg_width, egg_height)

        for rectangle in collision_bounds:
            if rectangle.colliderect(egg_rect):
                overlap = True

        if not overlap:
            eggGroup.add(egg)
            collision_bounds.append(egg_rect)
            eggBounds.append(pygame.Rect(egg.rect.x + egg_width // 4, egg.rect.y, egg_width // 2, egg_height))
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
    if y > 325:
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
                    CAUGHT_EGG_COLOR = eggColors[index]
                    print(CAUGHT_EGG_COLOR)
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
    start_game = False
    start_drop = False
    dropping = True
    game_complete = False
    return start_game, start_drop, dropping, game_complete


# Gameplay
while gaming:
    event = pygame.event.poll()
    position = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    screen.blit(background, (0, 0))
    if event.type == pygame.QUIT:
        gaming = False
    joystickDefault(-50, 450, joy_z)
    claw(claw_x, claw_y)
    screen.blit(startButton, (startButton_x, startButton_y))
    screen.blit(dropButton, (dropButton_x, dropButton_y))
    if not FILLED:
        add_sprites()
    eggGroup.draw(screen)

    if not START_GAME:
        onStartButton = button_clicked_on(start_rect, onStartButton)
        if onStartButton:
            START_GAME, onStartButton = button_clicked_off(start_rect, START_GAME, onStartButton)

    if START_GAME:
        if not START_DROP:
            onDropButton = button_clicked_on(drop_rect, onDropButton)
            if onDropButton:
                START_DROP, onDropButton = button_clicked_off(drop_rect, START_DROP, onDropButton)
            claw_xChange, joy_z = move_claw(claw_x)
            claw_x += claw_xChange
            joystickDefault(-50, 450, joy_z)
            claw(claw_x, claw_y)

        if START_DROP:
            isDropping, claw_xChange, claw_yChange, GAME_COMPLETE = drop_claw(isDropping, claw_x, claw_y, 100, 150)
            claw_x += claw_xChange
            claw_y += claw_yChange
            claw(claw_x, claw_y)

        if GAME_COMPLETE:
            START_GAME, START_DROP, isDropping, GAME_COMPLETE = game_reset()
    pygame.display.update()
    clock.tick(60)
