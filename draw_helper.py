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


# Draw lose
def draw_lose(vp):
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


# Draw check mark for win
def draw_win(vp):
    height = 60
    width = 10

    glPushMatrix()
    glTranslate(vp[0]/2 + 20, vp[1]/2, 0)
    glRotate(-45, 0, 0, 1)
    glBegin(GL_TRIANGLE_STRIP)
    glColor(0, 0.9, 0.1)
    glVertex2f(-width, height)
    glVertex2f(width, height)
    glVertex2f(-width,-height)
    glVertex2f(width, -height)
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)
    glColor(0, 0.9, 0.1)
    glVertex2f(width, width - height)
    glVertex2f(width, -width - height)
    glVertex2f(-height, width - height)
    glVertex2f(-height, -width - height)
    glEnd()

    glPopMatrix()


# Draw a mouse for click
def draw_click(vp):
    x = 50

    glPushMatrix()
    glTranslate(vp[0]/2, vp[1]/2 - 200, 0)
    glRotate(45, 0, 0, 1)
    glBegin(GL_TRIANGLE_STRIP)
    glColor(1.0, 1.0, 1.0)
    glVertex2f(-x, 0)
    glVertex2f(0, x*2)
    glVertex2f(x,0)
    glEnd()

    y = 80
    x1 = 10

    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(-x1, 0)
    glVertex2f(x1, 0)
    glVertex2f(-x1, -y)
    glVertex2f(x1, -y)
    glEnd()

    glPopMatrix()


# Draw a single brick
def draw_brick(b):
    glBegin(GL_QUADS)
    glColor3f(b.color[0], b.color[1], b.color[2])
    glVertex2f(b.pos.x, b.pos.y)
    glVertex2f(b.pos.x + 50, b.pos.y)
    glVertex2f(b.pos.x + 50, b.pos.y + 25)
    glVertex2f(b.pos.x, b.pos.y + 25)
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


# Draw obstacle
def draw_obstacle(obstacle):
    glBegin(GL_LINES)
    glColor3f(0.8, 1.0, 0.9)
    glVertex2f(obstacle.a.x, obstacle.a.y)
    glVertex2f(obstacle.b.x, obstacle.b.y)
    glEnd()