from point_and_vector import *

class obstacle:

    def __init__(self, x1, y1, x2, y2):
        self.a = point(x1, y1)
        self.b = point(x2, y2)