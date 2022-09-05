# TODO: This class will be the paddle that is used to affect the motion of the ball

class paddle:

    def __init__(self, pos):
        self.pos = pos
        self.color = [0.7, 0.3, 0.9]
        self.height = 10
        self.length = 50

    def update_paddle_pos(self, x):
        self.pos.x += x