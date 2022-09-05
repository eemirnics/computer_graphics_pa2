from math import cos, sin, pi
from OpenGL.GL import * 
from OpenGL.GLU import *
from random import random

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

# Draw a single brick
def draw_brick():
    glBegin(GL_QUADS)
    glColor3f(random(), random(), random())
    glVertex2f(0, 0)
    glVertex2f(50, 0)
    glVertex2f(50, 25)
    glVertex2f(0, 25)
    glEnd()

# Draw rows of bricks
def draw_brick_row(): 
    for i in range(16):
        glPushMatrix()
        glTranslate(50 * i, 775, 0)
        draw_brick()
        glPopMatrix()