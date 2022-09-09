class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return point(self.x * other, self.y * other)

    def dot(self, other): 
        return (self.x * other.x) + (self.y * other.y)


class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)

    def __sub__(self, other): 
        return Vector(self.x - other.x, self.y - other.y)