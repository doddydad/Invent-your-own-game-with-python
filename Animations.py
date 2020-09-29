# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:00:24 2020

@author: Andrew
"""

import sys, pygame, time
from pygame.locals import *

# Creating the window surface
pygame.init()

WINDOWHEIGHT = 400
WINDOWWIDTH = 400

window_surface = pygame.display.set_mode((WINDOWHEIGHT, WINDOWWIDTH), 0, 32)
pygame.display.set_caption("Nerds")

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

# set up box data structure (dictionaries)
# Doing by the book, but these look like shitty discount objects
b1 = {"rect": pygame.Rect(300, 180, 50, 100), "colour": RED, "dir": UPRIGHT}
b2 = {"rect": pygame.Rect(200, 200, 20, 20), "colour": GREEN, "dir": UPLEFT}
b3 = {"rect": pygame.Rect(100, 150, 60, 60), "colour": BLUE, "dir": DOWNRIGHT}
boxes = [b1, b2, b3]

# The actual animation
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    window_surface.fill(WHITE)

    for b in boxes:
        if "down" in b["dir"]:
            b["rect"].top += MOVESPEED
        if "up" in b["dir"]:
            b["rect"].top -= MOVESPEED
        if "left" in b["dir"]:
            b["rect"].left -= MOVESPEED
        if "right" in b["dir"]:
            b["rect"].left += MOVESPEED

        # Edge collision check
        if b["rect"].top < 0:
            if b["dir"] == UPRIGHT:
                b["dir"] = DOWNRIGHT
            if b["dir"] == UPLEFT:
                b["dir"] = DOWNLEFT
        if b["rect"].bottom > WINDOWHEIGHT:
            if b["dir"] == DOWNRIGHT:
                b["dir"] = UPRIGHT
            if b["dir"] == DOWNLEFT:
                b["dir"] = UPLEFT
        if b["rect"].left < 0:
            if b["dir"] == UPLEFT:
                b["dir"] = UPRIGHT
            if b["dir"] == DOWNLEFT:
                b["dir"] = DOWNRIGHT
        if b["rect"].right > WINDOWWIDTH:
            if b["dir"] == UPRIGHT:
                b["dir"] = UPLEFT
            if b["dir"] == DOWNRIGHT:
                b["dir"] = DOWNLEFT

        pygame.draw.rect(window_surface, b["colour"], b["rect"])

    pygame.display.update()
    time.sleep(0.02)
