import random
import pygame

screen = pygame.display.set_mode((750, 500))


class Egg(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])

        pygame.draw.ellipse(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()


pygame.init()

drop_x, drop_y, drop_width, drop_height = 350, 225, 50, 50
drop_button = pygame.Rect(drop_x, drop_y, drop_width, drop_height)
claw_x, claw_y, claw_width, claw_height = 400, 10, 50, 50
LEFT = 1
onButton = False
StartDrop = False
drop = True  # Is claw dropping or not
run = True

vel = 2

BLUE = (0, 0, 255)

eggGroup = pygame.sprite.Group()
current = 0
numEggs = 15
egg_width = 45
egg_height = 50
eggBounds = []
FILLED = False
NO_EGG_GRABBED = True   # Whether an egg has been grabbed (claw and egg collide)
CAUGHT_EGG = None       # The specific Egg sprite that the claw has collided with


# Method to add <numEggs> sprites to a group to display
def add_sprites():
    global current      # Current number of eggs in the group
    global FILLED       # Whether the group has been filled with eggs
    bounds = []         # Used to test whether eggs are overlapping
    failures = 0        # Current number of failures (consecutive overlapping instances)
    max_failures = 50   # Max number of failures before group reset

    while current < numEggs:
        overlap = False
        object_ = Egg(BLUE, egg_width, egg_height)
        object_.rect.x = random.randint(0, screen.get_width() - egg_width)
        object_.rect.y = random.randint(350, screen.get_height() - egg_height)
        object_rect = pygame.Rect(object_.rect.x, object_.rect.y, egg_width, egg_height)

        for rectangle in bounds:
            if rectangle.colliderect(object_rect):
                overlap = True

        if not overlap:
            eggGroup.add(object_)
            bounds.append(object_rect)
            # eggBounds is the amount of allowance for claw and egg collision
            # The allowance for each egg is half of the width centered from the egg
            # See green rectangles in demo, can be deleted
            eggBounds.append(pygame.Rect(object_.rect.x + egg_width // 4, object_.rect.y, egg_width // 2, egg_height))
            current += 1
            failures = 0
        else:
            failures += 1

        if failures == max_failures:    # Empty the sprite group and start over with adding sprites
            current = 0
            bounds = []
            eggGroup.empty()

    FILLED = True


run = True

while run:
    event = pygame.event.poll()
    position = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if event.type == pygame.QUIT:
        run = False

    if not FILLED:      # only go through to add sprites once, only need one group
        add_sprites()

    screen.fill((0, 0, 0))
    eggGroup.draw(screen)

    # Not needed, for demo purposes only (allowances for claw and egg collision)
    for b in eggBounds:
        pygame.draw.rect(screen, (0, 255, 0), b)

    if not StartDrop:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT \
                and drop_button.collidepoint(position[0], position[1]):
            onButton = True
        if onButton:
            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT \
                    and drop_button.collidepoint(position[0], position[1]):
                StartDrop = True
        pygame.draw.rect(screen, (255, 0, 0), drop_button)
    if StartDrop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.draw.rect(screen, (255, 255, 255), (claw_x, claw_y, claw_width, claw_height))
        if claw_y >= 400:
            drop = False
        if drop:
            claw_y += vel

            # Added for collision testing:
            clawMidpoint = (claw_x + claw_width//2, claw_y + claw_height)   # The bottommost center point of the claw
            if NO_EGG_GRABBED:
                index = 0   # So that the specific sprite can be located
                for egg in eggBounds:
                    if egg.collidepoint(clawMidpoint):
                        CAUGHT_EGG = eggGroup.sprites()[index]  # The specific Egg sprite that collided with the claw
                        print(CAUGHT_EGG.rect)
                        NO_EGG_GRABBED = False
                        break   # Break because only need one egg collision
                    index += 1

        elif not drop and claw_y != 10:
            claw_y -= vel
        elif claw_y == 10 and claw_x < 690:
            claw_x += vel

    pygame.display.update()

pygame.quit()
