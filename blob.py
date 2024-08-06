import random

import pygame
from typing import Tuple
from typing import Self

from position import Position


class Blob:
    def __init__(self, position: Position, size):
        self.position = position
        self.size = size
        self.colour = self.randomcolour()



    def randomly_reposition(self):
        self.position = Position(random.randint(10, 2450), random.randint(1, 2450))

    def draw(self, window):
        return pygame.draw.circle(window, self.colour, (self.position.x, self.position.y), self.size)

    def randomcolour(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)

