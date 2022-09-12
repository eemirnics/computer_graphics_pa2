from point_and_vector import *
import math

class ball:

    def __init__(self):
        self.pos = point(400, 400)
        self.radius = 7
        self.motion = Vector(350, -400)
        self.color = [1.0, 1.0, 1.0]

    # Used to generate an array of points that is a circle outline
    # Because of the brick corners, the entire array of circle points is checked 
    def get_circle_points(self):
        points_on_circle = []
        for angle in range(10):
            p = point(self.pos.x + (self.radius * math.sin(angle * 36)), self.pos.y + (self.radius * math.cos(angle * 36)))
            points_on_circle.append(p)
        return points_on_circle