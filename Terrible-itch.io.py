# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:08:20 2020

@author: Andrew
"""

import pygame, time, sys, random
from pygame.locals import *
# Creating the window surface
pygame.init()

WINDOWHEIGHT = 400
WINDOWWIDTH = 400

window_surface = pygame.display.set_mode((WINDOWHEIGHT, WINDOWWIDTH), 0, 32)
pygame.display.set_caption("Nerds")
main_clock = pygame.time.Clock()

# Setting some constants
DOWNRIGHT = "downright"
DOWNLEFT = "downleft"
UPRIGHT = "upright"
UPLEFT = "upleft"
MOVESPEED = 4

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

food_counter = 0
NEWFOOD = 40
FOODSIZE = 20

player = pygame.Rect(300, 100, 50, 50)

foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),
                             random.randint(0, WINDOWHEIGHT - FOODSIZE),
                             FOODSIZE, FOODSIZE))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    window_surface.fill(WHITE)
    for food in foods:
        pygame.draw.rect(window_surface, BLACK, food)
    pygame.display.update()









