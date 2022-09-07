# TODO: This class will be the paddle that is used to affect the motion of the ball

class paddle:

    def __init__(self, pos):
        self.pos = pos
        self.color = [0.7, 0.3, 0.9]
        self.height = 10
        self.length = 50

    def set_pos(self, pos_x, vp):
        if pos_x < vp[0] - self.length/2 and pos_x > self.length/2:
            self.pos.x = pos_x - self.length/2