# TODO: This class will be the paddle that is used to affect the motion of the ball

class paddle:

    def __init__(self, pos):
        self.pos = pos
        self.color = [0.7, 0.3, 0.9]
        self.height = 10
        self.length = 70

    def set_pos(self, pos_x, vp):
        if pos_x < vp[0] - self.length/2 and pos_x > self.length/2:
            self.pos.x = pos_x - self.length/2
    
    def check_collision(self, ball):
        x_boundaries = [self.pos.x - self.length/2 , self.pos.x + self.length/2]
        y = self.pos.y

        if ball.pos.y - ball.radius <= y:
            if x_boundaries[0] <= ball.pos.x >= x_boundaries[1]:
                return True
        return False