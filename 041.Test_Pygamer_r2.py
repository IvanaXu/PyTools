# -*-coding:utf-8-*-

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Hello, World!")

background = pygame.image.load('041.Test_Pygamer_r2_timg.jpg').convert()
mouse_cursor = pygame.image.load(
    '041.Test_Pygamer_r2_chess.png').convert_alpha()
xy = (0, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))

    x, y = pygame.mouse.get_pos()
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2

    if xy != (x, y):
        print("x, y:", x, y)
        xy = (x, y)
    screen.blit(mouse_cursor, (x, y))
    pygame.display.update()
