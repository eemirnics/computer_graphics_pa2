class ball:

    def __init__(self, pos, radius, motion):
        self.pos = pos
        self.radius = radius
        self.motion = motion
        self.color = [0.4, 0.3, 0.8]
        self.collision = False
