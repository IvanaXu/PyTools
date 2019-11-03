import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Demos")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (320, 200), 25, 1)
    pygame.draw.circle(screen, GREEN, (320, 200), 75, 2)
    pygame.draw.circle(screen, BLUE, (320, 200), 125, 3)

    pygame.display.flip()

    clock.tick(10)



