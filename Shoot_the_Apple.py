# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 20:37:45 2018

@author: PaulJ
"""

import time
import random
# import pygame
import pgzrun

WIDTH = 1200
HEIGHT = 800

timer = 30.0
score = 0
hits = 0
misses = 0
spin_apple = False
last_shot = 'no_shot_yet'
frame_rate = 0.33  # seconds
total_time_elapsed = 0
fruit_choice = 'apple'

apple = Actor('apple')
apple.x = random.randint(10, WIDTH-10)
apple.y = random.randint(10, HEIGHT-10)

orange = Actor('orange')
orange.x = random.randint(10, WIDTH-10)
orange.y = random.randint(10, HEIGHT-10)

pineapple = Actor('pineapple')
pineapple.x = random.randint(10, WIDTH-10)
pineapple.y = random.randint(10, HEIGHT-10)


def draw():      # Called whenever screen needs to be refreshed
    global spin_apple, last_shot
    screen.clear()
    apple.draw()
    orange.draw()
    pineapple.draw()
    screen.draw.text('Score: ' + str(score),
                     color='white',
                     topleft=(10, 10))
    screen.draw.text('Time: ' + str(int(timer)),
                     color='white',
                     topright=(WIDTH-10,10))
    if last_shot == 'hit':
        screen.draw.text('Good Shot!',
                         color='white',
                         center=(WIDTH/2, HEIGHT/2))
        time.sleep(0.25)
        apple.x = random.randint(10, WIDTH-10)
        apple.y = random.randint(10, HEIGHT-10)
        apple.draw()
        last_shot = None
    elif last_shot == 'miss':
        screen.draw.text('You Missed. Loser!',
                         color='white',
                         center=(WIDTH/2, HEIGHT/2))
        time.sleep(1)
        last_shot = None


def update(elapsed_time):     # Called once per frame, parameter is seconds
    global total_time_elapsed, timer, spin_apple
    timer -= elapsed_time
    if timer < -0:
        print('Score: ', str(score) + '. Hits:', str(hits) + '. Misses:',
              str(misses))
        exit()
    """
    if spin_apple:
        for angle in range(0, 361, 45):
            apple.angle = angle
            apple.draw()
            time.sleep(0.125)
        spin_apple = False
    """
    total_time_elapsed += elapsed_time
    if total_time_elapsed <= frame_rate:
        return
    else:
        total_time_elapsed = 0

    fruit_choice = random.choice(['apple', 'orange', 'pineapple'])

    if fruit_choice == 'apple':
        apple.x = random.randint(10, WIDTH-10)
        apple.y = random.randint(10, HEIGHT-10)
        apple.draw()
        orange.draw()
        pineapple.draw()
    elif fruit_choice == 'orange':
        orange.x = random.randint(10, WIDTH-10)
        orange.y = random.randint(10, HEIGHT-10)
        apple.draw()
        orange.draw()
        pineapple.draw()
    elif fruit_choice == 'pineapple':
        pineapple.x = random.randint(10, WIDTH-10)
        pineapple.y = random.randint(10, HEIGHT-10)
        pineapple.draw()
        apple.draw()
        orange.draw()


def on_mouse_down(pos):
    global score, frame_rate, last_shot, timer, spin_apple, hits, misses
    if apple.collidepoint(pos):
        score += 1
        hits += 1
        frame_rate *= 0.95
        timer += 1
        last_shot = 'hit'
    else:
        score -= 1
        misses += 1
        frame_rate *= 1.05
        # timer -= 1
        last_shot = 'miss'
        spin_apple = True
    # quit()

# place_fruit()

pgzrun.go()
