import sys
import pygame

pygame.init()

screen_width, screen_height = 500, 250
screen = pygame.display.set_mode((500, 250))
width, height = 20, 20
x, y = 50, 50
vel = 1
run = True
START = False

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        START = True
    if START:
        if keys[pygame.K_LEFT] and x > 0:
            x -= vel
        if keys[pygame.K_RIGHT] and x < screen_width-width:
            x += vel
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
        pygame.display.update()
pygame.quit()
