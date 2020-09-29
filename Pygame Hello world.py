# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:41:41 2020

@author: Andrew
"""

import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

# set up window
window_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Hello World")

# colour constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Font and text
basic_font = pygame.font.SysFont(None, 48)
text = basic_font.render("Hello World", True, WHITE, BLUE)
text_rect = text.get_rect()
text_rect.centerx = window_surface.get_rect().centerx
text_rect.centery = window_surface.get_rect().centery

# Fill with colour
window_surface.fill(WHITE)

# Draw a polygon (surface, colour, points, width)
pygame.draw.polygon(window_surface, GREEN, ((146, 0), (291, 106),
                                            (236, 277), (56, 277), (0, 106)))

# Draw lines (surface, colour, endpoints, width)
pygame.draw.line(window_surface, BLUE, (60, 20), (120, 20), 4)
pygame.draw.line(window_surface, BLUE, (120, 60), (60, 120))
pygame.draw.line(window_surface, BLUE, (60, 120), (120, 120), 4)

# Draw circle (surface, colour, center, radius, width)
pygame.draw.circle(window_surface, RED, (300, 50), 20, 2)

# Draw ellipse (surface, colour, (topleftx, toplefty, width, height), width)
pygame.draw.ellipse(window_surface, GREEN, (300, 250, 60, 80))

# Draw rectangle (surface, colour, (topleftx, toplefty, width, height), width)
pygame.draw.rect(window_surface, RED, (text_rect.left - 20, text_rect.top - 20,
                                       text_rect.width + 40, text_rect.height + 40))

# get a pixel array (fine control)
pix_array = pygame.PixelArray(window_surface)
pix_array[480][320] = BLACK

del pix_array

# Blit (moving around surfaces)
window_surface.blit(text, text_rect)

# Draw window onto screen
pygame.display.update()

# Actually running it
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
