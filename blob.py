import pygame
from typing import Tuple
from typing import Self


class Blob:
    def __init__(self, position: Tuple[int, int], size):
        self.position = position
        self.size = size
    def draw(self, window):
        return pygame.draw.circle(window, 'red', self.position, self.size)
