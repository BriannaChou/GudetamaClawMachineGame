"""
Class that draws numEggs amount of eggs that don't overlap within an area at the bottom of the canvas
"""

import random
import pygame

# Note: black rectangle around the shape shouldn't be a problem if we're using actual images (like for the claw)
# Might not be necessary, they're from the examples I was looking at
COLOR = (255, 100, 98)
SURFACE_COLOR = (0, 0, 0)
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class EllipseSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.ellipse(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()


pygame.init()

BLUE = (0, 0, 255)

all_sprites_list = pygame.sprite.Group()
current = 0
numEggs = 25
width = 45
height = 50
ex = []
FILLED = False


def add_sprites():
    global current
    global FILLED
    bounds = []
    failures = 0

    while current < numEggs:
        overlap = False
        object_ = EllipseSprite(BLUE, width, height)
        object_.rect.x = random.randint(0, screen.get_width() - width)
        object_.rect.y = random.randint(425, screen.get_height() - height)
        object_rect = pygame.Rect(object_.rect.x, object_.rect.y, width, height)

        for rectangle in bounds:
            if rectangle.colliderect(object_rect):
                overlap = True

        if not overlap:
            all_sprites_list.add(object_)
            bounds.append(object_rect)
            current += 1
            failures = 0
        else:
            failures += 1

        if failures == 50:
            current = 0
            bounds = []
            all_sprites_list.empty()


    FILLED = True


run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not FILLED:
        add_sprites()

    screen.fill((255, 255, 255))
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
