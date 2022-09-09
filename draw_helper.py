from math import cos, sin, pi
from OpenGL.GL import * 
from OpenGL.GLU import *
from random import random
from brick import *


# Draw the game ball
def draw_ball(ball):
    posx, posy = 0,0
    sides = 32
    radius = ball.radius

    glBegin(GL_POLYGON)
    glColor3f(ball.color[0], ball.color[1], ball.color[2])
    for i in range(100):
        cosine= radius * cos(i*2*pi/sides) + posx
        sine  = radius * sin(i*2*pi/sides) + posy
        glVertex2f(cosine,sine)
    glEnd()


# Draw paddle
def draw_paddle(paddle):
    glBegin(GL_QUADS)
    glColor3f(paddle.color[0], paddle.color[1], paddle.color[2])
    glVertex2f(0, 0)
    glVertex2f(paddle.length, 0)
    glVertex2f(paddle.length, paddle.height)
    glVertex2f(0, paddle.height)
    glEnd()

# Draw x
def draw_x(vp):
    height = 60
    width = 10

    glPushMatrix()
    glTranslate(vp[0]/2, vp[1]/2, 0)
    glRotate(45, 0, 0, 1)
    glBegin(GL_TRIANGLE_STRIP)
    glColor(0.9, 0.1, 0)
    glVertex2f(-width, height)
    glVertex2f(width, height)
    glVertex2f(-width,-height)
    glVertex2f(width, -height)
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)
    glColor(0.9, 0.1, 0)
    glVertex2f(-height, width)
    glVertex2f(height, width)
    glVertex2f(-height, -width)
    glVertex2f(height, -width)
    glEnd()

    glPopMatrix()

def draw_check(vp):
    height = 60
    width = 10

    glPushMatrix()
    glTranslate(vp[0]/2, vp[1]/2, 0)
    glBegin(GL_TRIANGLE_STRIP)
    glColor(0, 0.9, 0.1)
    glVertex2f(-width, height)
    glVertex2f(width, height)
    glVertex2f(-width,-height)
    glVertex2f(width, -height)
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)
    glColor(0, 0.9, 0.1)
    glVertex2f(-width, width - height)
    glVertex2f(-width, -width - height)
    glVertex2f(height, width - height)
    glVertex2f(height, -width - height)
    glEnd()

    glPopMatrix()

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