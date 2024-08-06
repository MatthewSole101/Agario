
from typing import Tuple
import random
import time
import pygame
from pygame import Surface, transform

from player import Player
from blob import Blob
from position import Position

pygame.init()
run = True


blobs = [Blob(Position(random.randint(10, 2450), random.randint(1, 2450)),  random.randint(5, 10)) for x in range(100)]


window = pygame.display.set_mode((500, 500))
background = Surface((2500, 2500))
image = pygame.image.load('richard.png')
clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption('Agario')

player1x = 200
player1y = 200
player1width = 10
player1height = 10

player = Player(Position(250, 250))


# Above text
# pygame.display.set_caption()

font = pygame.font.SysFont('Comic Sans', 10)

start_time = time.time()

camera_offset = Position(-1250, -1250)


while run:

    mousepos = pygame.mouse.get_pos()

    window.fill("White")
    background.fill("White")
    #window.blit(image, (0, 0))

    camera_offset -= (Position(*mousepos) - Position(250, 250)).normalize() * 2
    for blob in blobs:
        if player.collide(blob, camera_offset):

            player.size += blob.size
            blob.randomly_reposition()
            #blob.consumed = True

            blob.colour = blob.randomcolour()

        blob.draw(background)



    #blobs = [blob for blob in blobs if not blob.consumed]

    print(mousepos)



    window.blit(background, camera_offset.tuple())
    player.update()
    player.draw(window)



    size_text = font.render('Size: ' + str(player.size), True, (255, 255, 255))
    window.blit(size_text, (0, 0))

    time_text = font.render('Time: ' + str(round(time.time() - start_time, 1)), True, (255, 255, 255))
    window.blit(time_text, (250, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #quits game
            run = False

    print(mousepos)

    key = pygame.key.get_pressed()


    pygame.display.update()
    clock.tick(FPS)
end_time = time.time()
print(round(end_time - start_time, 1), ' seconds')
print('Total size: ' + str(player.size))

pygame.quit()




