class ball:

    def __init__(self, pos, radius, motion):
        self.pos = pos
        self.radius = radius
        self.motion = motion
        self.color = [0.4, 0.3, 0.8]
        self.collision = False

    def check_change_dir(self, viewport):
        if self.pos.x <= self.radius or self.pos.x >= viewport[0] - self.radius:
            self.change_x_dir()
        if self.pos.y <= self.radius or self.pos.y >= viewport[1] - self.radius:
            self.change_y_dir()
    
    def change_y_dir(self):
        self.motion.y = -self.motion.y

    def change_x_dir(self):
        self.motion.x = -self.motion.x
