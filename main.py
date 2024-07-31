
from typing import Tuple
import random

import pygame

from player import Player
from blob import Blob


pygame.init()



run = True

blobs = [Blob((random.randint(1, 500), random.randint(1, 500)),  random.randint(1, 5)) for x in range(5)]

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption('Agario')

player1x = 200
player1y = 200
player1width = 10
player1height = 10

player = Player()

while run:
    #Delay
    #pygame.time.delay(10)
    mousepos = pygame.mouse.get_pos()

    window.fill("White")

    for blob in blobs:
        blob.draw(window)

    print(mousepos




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #quits game
            run = False

    key = pygame.key.get_pressed()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()









