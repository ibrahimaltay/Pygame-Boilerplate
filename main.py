import os
import sys
from pygame.locals import *
from methods import *
import pygame
pygame.init()
import time

config = GetConfiguration()
colors = GetColors()

WIDTH = int(config["WIDTH"])
HEIGHT = int(config["HEIGHT"])

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kart Oyunu")
FPS=60
clock = pygame.time.Clock()

run=True
while run:
    win.fill(colors["White"])
    pygame.display.update()
    clock.tick(FPS)

    # MAIN LOGIC GOES HERE



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run=False

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                run = False


pygame.quit()











