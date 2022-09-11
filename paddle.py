from point_and_vector import *

class paddle:

    def __init__(self, pos):
        self.pos = pos
        self.color = [1.0, 1.0, 1.0]
        self.height = 2
        self.length = 100
        self.normal = Vector(0, -self.length)


    def set_pos(self, pos_x, vp):
        if pos_x < vp[0] - self.length/2 and pos_x > self.length/2:
            self.pos.x = pos_x - self.length/2