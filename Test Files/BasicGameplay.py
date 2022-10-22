"""
Displays a button (white rectangle) and starts a game when clicked
Start of game gets rid of button and displays a claw (white square) that can be moved left and right
Another button present (red square) to drop claw at any point
    Clicking button will drop claw straight down, move it back up immediately, and
    to the right (back to original, starting position)
"""

import pygame

pygame.init()

screen_width, screen_height = 750, 500
screen = pygame.display.set_mode((screen_width, screen_height))

startButton_x, startButton_y, startButton_width, startButton_height = 300, 320, 150, 50
startButton = pygame.Rect(startButton_x, startButton_y, startButton_width, startButton_height)

dropButton_x, dropButton_y, dropButton_width, dropButton_height = 10, 440, 50, 50
dropButton = pygame.Rect(dropButton_x, dropButton_y, dropButton_width, dropButton_height)

claw_x, claw_y, claw_width, claw_height = 690, 20, 50, 50

LEFT = 1
run = True
vel = 2
onStartButton = False
START_GAME = False
onDropButton = False
START_DROP = False
isDropping = True

while run:
    event = pygame.event.poll()
    position = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if event.type == pygame.QUIT:
        run = False
    if not START_GAME:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT \
                and startButton.collidepoint(position[0], position[1]):
            onStartButton = True
        if onStartButton:
            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT \
                    and startButton.collidepoint(position[0], position[1]):
                START_GAME = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT \
                    and not startButton.collidepoint(position[0], position[1]):
                onStartButton = False
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), startButton)
    if START_GAME:
        if not START_DROP:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT \
                    and dropButton.collidepoint(position[0], position[1]):
                onDropButton = True
            if onDropButton:
                if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT \
                        and dropButton.collidepoint(position[0], position[1]):
                    START_DROP = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT \
                        and not dropButton.collidepoint(position[0], position[1]):
                    onDropButton = False
            if keys[pygame.K_LEFT] and claw_x > 0:
                claw_x -= vel
            if keys[pygame.K_RIGHT] and claw_x < screen_width - claw_width:
                claw_x += vel
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (255, 255, 255), (claw_x, claw_y, claw_width, claw_height))
            #screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (255, 0, 0), dropButton)
        if START_DROP:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (255, 255, 255), (claw_x, claw_y, claw_width, claw_height))
            if claw_y >= 400:
                isDropping = False
            if isDropping:
                claw_y += 2
            elif not isDropping and claw_y != 20:
                claw_y -= 2
            elif claw_y == 20 and claw_x < 690:
                claw_x += 2
    pygame.display.update()
