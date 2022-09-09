from point_and_vector import *

class paddle:

    def __init__(self, pos):
        self.pos = pos
        self.color = [0.7, 0.3, 0.9]
        self.height = 10
        self.length = 200
        self.normal = Vector(0, self.length)


    def set_pos(self, pos_x, vp):
        if pos_x < vp[0] - self.length/2 and pos_x > self.length/2:
            self.pos.x = pos_x - self.length/2


    # Find thit
    def calculate_thit(self, position, motion):
        b_minus_a = self.pos - position
        n_dot_c = self.normal.dot(motion)
        thit = self.normal.dot(b_minus_a) / n_dot_c
        return thit


    # Check phit
    def check_phit(self, position, thit, motion):
        temp = Vector(thit * motion.x, thit * motion.y)
        phit = point(position.x + temp.x, position.y + temp.y)

        # Check if phit is on line
        if phit.x > self.pos.x and phit.x < self.pos.x + self.length :
            return True
        else:
            return False
        

    # Check collision and return the reflection vector if it occurs
    def check_collision(self, position, motion, delta_time):
        thit = self.calculate_thit(position, motion)
        # print(thit, delta_time)
        if thit > 0 and thit <= delta_time:
            print("TRUE")
            if (self.check_phit(position, thit, motion)):
                return self.calculate_reflection(motion)
        else:
            return None


    # Calculate the reflection vector after the collision
    def calculate_reflection(self, motion):
        temp = (2 * motion.dot(self.normal)) / (self.normal.dot(self.normal))
        temp2 = Vector(temp * self.normal.x, temp * self.normal.y)
        r = Vector(motion.x - temp2.x, motion.y - temp2.y)
        return r

