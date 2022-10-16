"""
Displays a button (white rectangle) and starts game when clicked
Start of game gets rid of button and displays a claw (white square) that can be moved left and right

Note: use flip() or update() ?
"""

import pygame

pygame.init()

screen_width, screen_height = 750, 500
screen = pygame.display.set_mode((screen_width, screen_height))
button_x, button_y, button_width, button_height = 300, 320, 150, 50
button = pygame.Rect(button_x, button_y, button_width, button_height)  # Object so its coordinates can be referenced
claw_x, claw_y, claw_width, claw_height = 690, 10, 50, 50
# Can't use rect object for claw bc it doesn't update with changes in x
LEFT = 1  # event.button integer value for left-click is 1
onButton = False  # Boolean for whether the down click is on the rectangle
vel = 1.5
START = False  # Indicate if start button has been pressed -> start game
run = True

while run:
    event = pygame.event.poll()
    position = pygame.mouse.get_pos()  # x and y coordinates of the cursor location
    keys = pygame.key.get_pressed()
    if event.type == pygame.QUIT:
        run = False
    if not START:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT \
                and button.collidepoint(position[0], position[1]):  # LEFT mouse button pressed down within rectangle
            onButton = True
        if onButton:  # Mouse button IS pressed down within rectangle
            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT \
                    and button.collidepoint(position[0], position[1]):  # LEFT mouse button released within rectangle
                START = True
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), button)  # use Rect object instead of (x, y, width, and height)
        #pygame.display.flip()  # Updates contents of entire display (update only does a portion)
    if START:  # Start button has been clicked
        if keys[pygame.K_LEFT] and claw_x > 0:
            claw_x -= vel
        if keys[pygame.K_RIGHT] and claw_x < screen_width-claw_width:
            claw_x += vel
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (claw_x, claw_y, claw_width, claw_height))
    pygame.display.update()
