from typing import Self
from math import hypot

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, other: Self) -> Self:
        return Position(self.x - other.x, self.y - other.y)

    def __add__(self, other: Self) -> Self:
        return Position(self.x + other.x, self.y + other.y)

    def dist(self, other: Self) -> float:
        return hypot(self.x - other.x, self.y - other.y)

    def modulus(self):
        return hypot(self.x, self.y)

    def normalize(self):
        if self.modulus() != 0:
            self.x /= self.modulus()
            self.y /= self.modulus()

        return self

    def __mul__(self, n: int):
        return Position(self.x * n, self.y * n)