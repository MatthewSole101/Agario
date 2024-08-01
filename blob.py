import random

import pygame
from typing import Tuple
from typing import Self

from position import Position


class Blob:
    def __init__(self, position: Position, size):
        self.position = position
        self.size = size
        #self.consumed = False

    def randomly_reposition(self):
        self.position = Position(random.randint(10, 450), random.randint(1, 500))

    def draw(self, window):
        return pygame.draw.circle(window, 'red', (self.position.x, self.position.y), self.size)
