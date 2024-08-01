import pygame
from typing import Tuple
from typing import Self
from position import Position

import math
from operator import sub


class Player:
    def __init__(self, position: Position, size: int=20, name: str = "No Name"):
        self.surface = pygame.Surface((size * 2, size * 2))
        self.position = position
        self.size = size #pygame.mouse.get_pos()
        self.name = name

    def collide(self, other) -> bool:
        dist = self.position.dist(other.position)  #math.hypot(*map(sub, self.position, other.position))

        return dist <= self.size + other.size

    def draw(self, surface: pygame.Surface):

        pygame.draw.circle(surface, (255, 0, 255), (self.position.x, self.position.y), self.size, width=0)
        #surface.blit(self.surface, self.position)

    def update(self):
        mouse_position = Position(*pygame.mouse.get_pos())
        self.position += (mouse_position - self.position).normalize() * 2
