from OpenGL.GL import * 
from OpenGL.GLU import *
from random import random
from brick import *


# Draw the game ball
def draw_ball():
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.5, 0.1)
    glVertex2f(0, 0)
    glVertex2f(100, 0)
    glVertex2f(100, 100)
    glVertex2f(0, 100)
    glEnd()


# Draw a single brick
def draw_brick(b):
    glBegin(GL_QUADS)
    glColor3f(b.color[0], b.color[1], b.color[2])
    glVertex2f(b.x, b.y + 600)
    glVertex2f(b.x + 50, b.y + 600)
    glVertex2f(b.x + 50, b.y + 625)
    glVertex2f(b.x, b.y + 625)
    glEnd()


# Create array of bricks
def create_bricks():
    bricks = []
    for x in range(16):
        for y in range(8):
            new_brick = brick(50 * x, 25 * y, [random(), random(), random()])
            bricks.append(new_brick)
    return bricks


# Draw bricks
def draw_bricks(bricks): 
    for brick in bricks: 
        draw_brick(brick)