from OpenGL.GL import * 
from OpenGL.GLU import *
from random import random

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