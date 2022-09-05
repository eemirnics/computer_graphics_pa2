import pygame 
from pygame.locals import * 

from OpenGL.GL import * 
from OpenGL.GLU import *
from paddle import *

from vector import *
from point import *
from draw_helper import *
from ball import *

viewport = [800, 800]

position = point(350, 350)
motion = vector(50, -60)
game_ball = ball(position, 15, motion)

game_paddle = paddle(point(int(viewport[0]/2), 50))
game_paddle.pos.x = game_paddle.pos.x - game_paddle.length/2

clock = None
delta_time = 0
bricks = []


def init_game():
    global clock
    global bricks
    clock = pygame.time.Clock()

    pygame.display.init() 
    pygame.display.set_mode((viewport[0], viewport[1]), DOUBLEBUF|OPENGL)  
    glClearColor(0.95, 0.85, 0.97, 1.0)
    clock.tick()

    bricks = create_bricks()
    

# TODO: Some kind of note about needing to make this recursive
def update():
    global game_ball
    global delta_time
    global bricks

    delta_time = clock.tick() / 1000

    # Reverse direction if the ball reaches an edge
    if game_ball.pos.x <= game_ball.radius or game_ball.pos.x > viewport[0] - game_ball.radius:
        game_ball.motion.x = -game_ball.motion.x
    if game_ball.pos.y <= game_ball.radius or game_ball.pos.y > viewport[1] - game_ball.radius:
        game_ball.motion.y = -game_ball.motion.y

    # Update position
    game_ball.pos += game_ball.motion * (delta_time * 2.0)

    for b in bricks: 
        if b.check_collision(position):
            bricks.remove(b)


def display(): 
    global bricks
    global game_ball

    # Initialize matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Set up view port and viewing window
    glViewport(0, 0, viewport[0], viewport[1])
    gluOrtho2D(0, viewport[0], 0, viewport[1])

    glClear(GL_COLOR_BUFFER_BIT) 

    draw_bricks(bricks)

    glPushMatrix()

    # Translate to position 
    glTranslate(game_ball.pos.x, game_ball.pos.y, 0)

    draw_ball(game_ball)
    
    glPopMatrix()

    glPushMatrix()
    
    # Translate
    glTranslate(game_paddle.pos.x, game_paddle.pos.y, 0)
    
    draw_paddle(game_paddle)

    glPopMatrix()
    # Signifies done drawing and screen can now display
    pygame.display.flip()

def game_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN: 
            if event.key == K_ESCAPE:
                pygame.quit()
                quit()
        elif event.type == pygame.MOUSEMOTION:
            paddle.update_paddle_pos(game_paddle, event.rel[0])
        
    update() 
    display() 


if __name__ == "__main__": 
    init_game() 
    while True: 
        game_loop()