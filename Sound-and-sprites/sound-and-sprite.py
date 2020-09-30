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
pygame.display.set_caption("Noisy Nerds")
main_clock = pygame.time.Clock()

# Setting some constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Food creation. Well you eat it
food_counter = 0
MAXFOOD = 40
FOODSIZE = 20
food_image = pygame.image.load("food.png")

# Movement variables
move_left = False
move_right = False
move_up = False
move_down = False

# player stuff
player_size = 30
player = pygame.Rect(300, 100, player_size, player_size)
player_image = pygame.image.load("player.png")
player_stretched_image = pygame.transform.scale(player_image, (player_size,
                                                               player_size))
MOVESPEED = 4

# Music setup
pick_up_sound = pygame.mixer.Sound("Kiss.wav")
pygame.mixer.music.load("froge.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1, 0.0)
music_playing = True

# Setting out where the food is
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

        # Change the keyboard variables
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                move_left = True
            if event.key == K_RIGHT or event.key == K_d:
                move_right = True
            if event.key == K_UP or event.key == K_w:
                move_up = True
            if event.key == K_DOWN or event.key == K_s:
                move_down = True

            # Quits as an alternative method
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            # Teleports player as an option
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

            if event.key == K_m:
                if music_playing:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                music_playing = not music_playing

        # Changing back when you release the key
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                move_left = False
            if event.key == K_RIGHT or event.key == K_d:
                move_right = False
            if event.key == K_UP or event.key == K_w:
                move_up = False
            if event.key == K_DOWN or event.key == K_s:
                move_down = False

        # Creates a new thing you can hit when you click
        if event.type == MOUSEBUTTONDOWN:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))
            if len(foods) >= MAXFOOD:
                foods.remove(foods[0])

    # Automatically creates new food counters
    food_counter += 1
    if food_counter >= 20:
        food_counter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWHEIGHT - FOODSIZE),
                                 random.randint(0, WINDOWWIDTH - FOODSIZE),
                                 FOODSIZE, FOODSIZE))
        if len(foods) > MAXFOOD:
            foods.remove(foods[0])

    # Moving the player
    if move_down and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if move_up and player.top > 0:
        player.top -= MOVESPEED
    if move_left and player.left > 0:
        player.left -= MOVESPEED
    if move_right and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    window_surface.fill(WHITE)

    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player.width += 1
            player.height += 1
            player_stretched_image = pygame.transform.scale(
                player_image, (player.width, player.height))
            if music_playing:
                pick_up_sound.play()

    for food in foods:
        window_surface.blit(food_image, food)
    window_surface.blit(player_stretched_image, player)

    pygame.display.update()
    time.sleep(0.02)
