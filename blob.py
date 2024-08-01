import random

import pygame
from typing import Tuple
from typing import Self


class Blob:
    def __init__(self, position: Tuple[int, int], size):
        self.position = position
        self.size = size
    def draw(self, window, colour):
        return pygame.draw.circle(window, colour, self.position, self.size)
    def randomcolour(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)