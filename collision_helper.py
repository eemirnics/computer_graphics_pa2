from point_and_vector import *
from brick import *
from paddle import *
from obstacle import *


# Find thit
def calculate_thit(n, B, A, c):
    b_minus_a = B - A
    n_dot_c = n.dot(c)
    thit = n.dot(b_minus_a) / n_dot_c
    return thit


# Calculate phit
def calculate_phit(thit, A, c):
    temp = Vector(thit * c.x, thit * c.y)
    phit = point(A.x + temp.x, A.y + temp.y)
    return phit


# Calculate the reflection vector after the collision
def calculate_reflection(n, c):
    temp = (2 * c.dot(n)) / (n.dot(n))
    temp2 = Vector(temp * n.x, temp * n.y)
    r = Vector(c.x - temp2.x, c.y - temp2.y)
    return r


# Check for collisions with walls and return the appropriate reflection vectors
def check_wall_collision(game_ball, delta_time):
    collision = None

    # Check left wall
    thit = calculate_thit(Vector(800, 0), point(0, 800), point(game_ball.pos.x - game_ball.radius, game_ball.pos.y), game_ball.motion)
    if thit > 0 and thit <= delta_time:
        return calculate_reflection(Vector(800, 0), game_ball.motion)

    # Check right wall
    thit = calculate_thit(Vector(-800, 0), point(800, 0), point(game_ball.pos.x + game_ball.radius, game_ball.pos.y), game_ball.motion)
    if thit > 0 and thit <= delta_time:
        return calculate_reflection(Vector(800, 0), game_ball.motion)

    # Check top wall
    thit = calculate_thit(Vector(0, 800), point(800, 800), point(game_ball.pos.x, game_ball.pos.y + game_ball.radius), game_ball.motion)
    if thit > 0 and thit <= delta_time:
        return calculate_reflection(Vector(0, 800), game_ball.motion)

    # Check bottom wall: return Vector with null values if collision
    thit = calculate_thit(Vector(0, -800), point(0, 0), point(game_ball.pos.x, game_ball.pos.y - game_ball.radius), game_ball.motion)
    if thit > 0 and thit <= delta_time:
        return Vector(None, None)

    return collision


# Check for collisions with the paddle and return the appropriate reflection vectors
# There will be no bounces underneath the paddle since a collision with the bottom wall ends the game
def check_paddle_collision(game_ball, delta_time, p):
    collision = None
    circle_outline = game_ball.get_circle_points()

    # Check collision with top of paddle
    for circle_point in circle_outline:
        thit = calculate_thit(Vector(0, p.length), point(p.pos.x + p.length, p.pos.y + p.height), circle_point, game_ball.motion)
        phit = calculate_phit(thit, circle_point, game_ball.motion)
        if thit > 0 and thit <= delta_time:
            if phit.x > p.pos.x and phit.x < p.pos.x + p.length:
                return calculate_reflection(Vector(0, p.length), game_ball.motion)

    return collision


# Check for collisions with a brick and return the appropriate reflection vectors
def check_brick_collision(game_ball, delta_time, b):
    collision = None
    circle_outline = game_ball.get_circle_points()

    for circle_point in circle_outline:
        # Check bottom edge of brick
        thit = calculate_thit(Vector(0, -b.width), b.pos, circle_point, game_ball.motion)
        phit = calculate_phit(thit, circle_point, game_ball.motion)
        if thit > 0 and thit <= delta_time:
            if phit.x > b.pos.x and phit.x < b.pos.x + b.width:
                return calculate_reflection(Vector(0, -b.width), game_ball.motion)

        # Check right edge of brick
        thit = calculate_thit(Vector(-b.height, 0), point(b.pos.x + b.width, b.pos.y), circle_point, game_ball.motion)
        phit = calculate_phit(thit, circle_point, game_ball.motion)
        if thit > 0 and thit <= delta_time:
            if phit.y > b.pos.y and phit.y < b.pos.y + b.height:
                return calculate_reflection(Vector(-b.height, 0), game_ball.motion)

        # Check top edge of brick
        thit = calculate_thit(Vector(0, b.width), point(b.pos.x + b.width, b.pos.y + b.height), circle_point, game_ball.motion)
        phit = calculate_phit(thit, circle_point, game_ball.motion)
        if thit > 0 and thit <= delta_time:
            if phit.x > b.pos.x and phit.x < b.pos.x + b.width:
                return calculate_reflection(Vector(0, b.width), game_ball.motion)

        # Check left edge of brick
        thit = calculate_thit(Vector(b.height, 0), point(b.pos.x, b.pos.y + b.height), circle_point, game_ball.motion)
        phit = calculate_phit(thit, circle_point, game_ball.motion)
        if thit > 0 and thit <= delta_time:
            if phit.y > b.pos.y and phit.y < b.pos.y + b.height:
                return calculate_reflection(Vector(b.height, 0), game_ball.motion)

    return collision


# Check for collision with the obstacle and return the appropriate reflection vectors
def check_obstacle_collision(game_ball, delta_time, o):
    collision = None
    bottom_normal = Vector(o.a.y - o.b.y, -(o.a.x - o.b.x))
    top_normal = Vector(o.a.y - o.b.y, -(o.a.x - o.b.x))
    circle_outline = game_ball.get_circle_points()

    for circle_point in circle_outline:
        # Check collision with bottom of line
        thit = calculate_thit(bottom_normal, o.a, circle_point, game_ball.motion)
        phit = calculate_phit(thit, circle_point, game_ball.motion)
        if thit > 0 and thit <= delta_time:
            if phit.x > o.a.x and phit.x < o.b.x and phit.y > o.a.y and phit.y < o.b.y:
                return calculate_reflection(bottom_normal, game_ball.motion)

        # Check collision with top of line
        thit = calculate_thit(top_normal, o.a, circle_point, game_ball.motion)
        phit = calculate_phit(thit, circle_point, game_ball.motion)
        if thit > 0 and thit <= delta_time:
            if phit.x > o.a.x and phit.x < o.b.x and phit.y > o.a.y and phit.y < o.b.y:
                return calculate_reflection(top_normal, game_ball.motion)

    return collision