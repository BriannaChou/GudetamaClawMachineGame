"""
Displays a button (white rectangle) and starts a game when clicked
Start of game gets rid of button and displays a claw (white square) that can be moved left and right
Another button present (red square) to drop claw at any point
    Clicking button will drop claw straight down, move it back up immediately, and
    to the right (back to original, starting position)

Basic game organized with functions/methods
"""


import pygame

pygame.init()

screen_width, screen_height = 750, 500
screen = pygame.display.set_mode((screen_width, screen_height))

startButton_x, startButton_y, startButton_width, startButton_height = 300, 320, 150, 50
startButton = pygame.Rect(startButton_x, startButton_y, startButton_width, startButton_height)

dropButton_x, dropButton_y, dropButton_width, dropButton_height = 10, 440, 50, 50
dropButton = pygame.Rect(dropButton_x, dropButton_y, dropButton_width, dropButton_height)

claw_x, claw_y, claw_width, claw_height = 680, 20, 50, 50

LEFT = 1
run = True
vel = 2
onStartButton = False
START_GAME = False
onDropButton = False
START_DROP = False
isDropping = True


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


def move_claw(x):
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width - claw_width:
        x += vel
    return x


def drop_claw(is_dropping, x, y):
    if y > 400:
        is_dropping = False
    if is_dropping:
        y += vel
    elif not is_dropping and y != 20:
        y -= vel
    elif y == 20 and x < 680:
        x += vel
    return is_dropping, x, y


while run:
    event = pygame.event.poll()
    position = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if event.type == pygame.QUIT:
        run = False

    if not START_GAME:
        onStartButton = button_clicked_on(startButton, onStartButton)
        if onStartButton:
            START_GAME, onStartButton = button_clicked_off(startButton, START_GAME, onStartButton)
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), startButton)

    if START_GAME:
        if not START_DROP:
            onDropButton = button_clicked_on(dropButton, onDropButton)
            if onDropButton:
                START_DROP, onDropButton = button_clicked_off(dropButton, START_DROP, onDropButton)
            claw_x = move_claw(claw_x)
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (255, 255, 255), (claw_x, claw_y, claw_width, claw_height))
            pygame.draw.rect(screen, (255, 0, 0), dropButton)

        if START_DROP:
            isDropping, claw_x, claw_y = drop_claw(isDropping, claw_x, claw_y)
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (255, 255, 255), (claw_x, claw_y, claw_width, claw_height))

    pygame.display.update()
