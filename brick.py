from point_and_vector import *

class brick:

    def __init__(self, x, y, color):
        self.pos = point(x, y + 600)
        self.color = color
        self.collision = False
        self.width = 50
        self.height = 25
