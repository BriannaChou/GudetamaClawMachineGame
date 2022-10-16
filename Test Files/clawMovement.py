"""
Displays a button (red square) to begin dropping claw (white square)
Put start of game (x movement) before drop mechanics
Drops claw down and moves it up immediately after reaching a certain point until it reaches original y (10)
Moves claw right until it reaches original x (690)
"""

import pygame

pygame.init()

screen_width, screen_height = 750, 500
screen = pygame.display.set_mode((screen_width, screen_height))
drop_x, drop_y, drop_width, drop_height = 350, 225, 50, 50
drop_button = pygame.Rect(drop_x, drop_y, drop_width, drop_height)
claw_x, claw_y, claw_width, claw_height = 400, 10, 50, 50
LEFT = 1
onButton = False
StartDrop = False
drop = True  # Is claw dropping or not
run = True

while run:
    event = pygame.event.poll()
    position = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if event.type == pygame.QUIT:
        run = False
    if not StartDrop:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT \
                and drop_button.collidepoint(position[0], position[1]):
            onButton = True
        if onButton:
            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT \
                    and drop_button.collidepoint(position[0], position[1]):
                StartDrop = True
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), drop_button)
    if StartDrop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (claw_x, claw_y, claw_width, claw_height))
        if claw_y >= 400:
            drop = False
        if drop:
            claw_y += 2
        elif not drop and claw_y != 10:  # 10 only works if it decreases by 2 or 5
            claw_y -= 2
        elif claw_y == 10 and claw_x < 690:  # 10 only works if it decreases by 2 or 5
            claw_x += 2
    pygame.display.update()
