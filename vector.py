from point import *

class vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return point(self.x * other, self.y * other)