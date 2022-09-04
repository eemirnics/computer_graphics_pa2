import pygame 
from pygame.locals import * 

from OpenGL.GL import * 
from OpenGL.GLU import *

from vector import *
from point import *
from draw_helper import *


position = point(350, 350)
motion = vector(50, -60)
clock = None
delta_time = 0


def init_game(): 
    global clock
    clock = pygame.time.Clock()

    pygame.display.init() 
    pygame.display.set_mode((800, 800), DOUBLEBUF|OPENGL)  
    glClearColor(0.95, 0.85, 0.97, 1.0)
    clock.tick()
    

# TODO: Some kind of note about needing to make this recursive
def update(): 
    global position
    global motion
    global delta_time

    delta_time = clock.tick() / 1000

    # Reverse direction if the square reaches an edge
    if position.x <= 0 or position.x >= 700:
        motion.x = -motion.x
    if position.y <= 0 or position.y >= 700:
        motion.y = -motion.y

    # Update position
    position += motion * delta_time


def display(): 
    global position
    global motion

    # Initialize matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Set up view port and viewing window
    glViewport(0, 0, 800, 800)
    gluOrtho2D(0, 800, 0, 800)

    glClear(GL_COLOR_BUFFER_BIT) 

    draw_brick_row()

    glPushMatrix()

    # Translate to position 
    glTranslate(position.x, position.y, 0)

    draw_ball()
    
    glPopMatrix()

    # Signifies done drawing and screen can now display
    pygame.display.flip()


def game_loop(): 
    global position
    global motion

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN: 
            if event.key == K_ESCAPE:
                pygame.quit()
                quit()
        
    update() 
    display() 


if __name__ == "__main__": 
    init_game() 
    while True: 
        game_loop()