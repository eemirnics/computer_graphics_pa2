from point import *

class brick:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.collision = False


    def check_collision(self, position):
        if position.x >= self.x and position.x < self.x + 50 and position.y >= self.y + 600 and position.y < self.y + 625:
            self.collision = True
        return self.collision
