import random

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Dimensions need to be different --> different file sizes
# Which color is which rarity is temp
eggDimensions = (60, 60)
blue = pygame.image.load("../images/blueEgg.png")
blue = pygame.transform.scale(blue, eggDimensions)
red = pygame.image.load("../images/redEgg.png")
red = pygame.transform.scale(red, (47, 60))
yellow = pygame.image.load("../images/yellowEgg.png")
yellow = pygame.transform.scale(yellow, (47, 60))
gold = pygame.image.load("../images/goldenEgg_special.png")
gold = pygame.transform.scale(gold, (47, 60))


class Egg(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        self.image = image

        self.rect = self.image.get_rect()


eggGroup = pygame.sprite.Group()
current = 0
numEggs = 15
eggBounds = []
FILLED = False


def add_sprites():
    global current
    global FILLED
    color = None
    collision_bounds = []
    failures = 0
    max_failures = 50

    while current < numEggs:
        overlap = False
        rand = random.randint(1, 20)
        if rand < 11:
            color = blue
        elif rand < 17:
            color = red
        elif rand < 20:
            color = yellow
        else:
            color = gold

        egg = Egg(color)
        egg.rect.x = random.randint(0, screen.get_width() - eggDimensions[0])
        egg.rect.y = random.randint(400, screen.get_height() - eggDimensions[1])
        egg_rect = pygame.Rect(egg.rect.x, egg.rect.y, eggDimensions[0], eggDimensions[1])

        for rectangle in collision_bounds:
            if rectangle.colliderect(egg_rect):
                overlap = True

        if not overlap:
            eggGroup.add(egg)
            collision_bounds.append(egg_rect)
            #eggBounds.append(pygame.Rect(egg.rect.x + eggDimensions[0]//4, egg.rect.y,
            #                             eggDimensions[0]//2, eggDimensions[1]))
            current += 1
            failures = 0
        else:
            failures += 1

        if failures == max_failures:
            current = 0
            collision_bounds = []
            eggGroup.empty()

    FILLED = True


gaming = True

while gaming:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        gaming = False
    screen.fill((0, 0, 0))
    # screen.blit(blue, (50, 50))
    if not FILLED:
        add_sprites()
    eggGroup.draw(screen)

    pygame.display.update()
