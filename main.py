import pygame 
from pygame.locals import * 

from OpenGL.GL import * 
from OpenGL.GLU import *

from paddle import *
from point_and_vector import *
from draw_helper import *
from collision_helper import *
from ball import *
from obstacle import *


viewport = [800, 800]

game_ball = ball()
game_paddle = paddle(point(int(viewport[0]/2), 50))
game_paddle.pos.x = game_paddle.pos.x - game_paddle.length/2
game_obstacle = obstacle(340, 450, 460, 505)

clock = None
delta_time = 0
bricks = []
game_won = False
game_lost = False
start_of_game = True


def init_game():
    global clock
    global bricks

    clock = pygame.time.Clock()
    pygame.display.init() 
    pygame.display.set_mode((viewport[0], viewport[1]), DOUBLEBUF|OPENGL)  
    glClearColor(0.0, 0.0, 0.0, 1.0)
    clock.tick()

    bricks = create_bricks()
    

def update():
    global game_ball
    global game_paddle
    global game_obstacle
    global delta_time
    global bricks
    global game_won
    global game_lost

    delta_time = clock.tick() / 2000

    # Check for collision with walls
    wall_collision = check_wall_collision(game_ball, delta_time)
    if wall_collision is not None:
        # Check for bottom wall
        if wall_collision.x is None:
            game_lost = True
        else: 
            game_ball.motion = wall_collision
    
    # Check for collision with bricks
    for b in bricks: 
        brick_collision = check_brick_collision(game_ball, delta_time, b)
        if brick_collision is not None:
            game_ball.motion = brick_collision
            bricks.remove(b)
            if len(bricks) == 0: 
                game_won = True

    # Check for collision with paddle
    paddle_collision = check_paddle_collision(game_ball, delta_time, game_paddle)
    if paddle_collision is not None:
        game_ball.motion = paddle_collision

    # Check for collision with obstacle
    obstacle_collision = check_obstacle_collision(game_ball, delta_time, game_obstacle)
    if obstacle_collision is not None:
        game_ball.motion = obstacle_collision

    # Update position
    game_ball.pos += game_ball.motion * delta_time

    
def display(): 
    global bricks
    global game_ball
    global game_paddle
    global game_obstacle
    global game_won
    global game_lost
    global start_of_game

    # Initialize matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Set up view port and viewing window
    glViewport(0, 0, viewport[0], viewport[1])
    gluOrtho2D(0, viewport[0], 0, viewport[1])
    glClear(GL_COLOR_BUFFER_BIT) 

    # If game over, stop drawing and handle the display messages for game state
    if game_won or game_lost or start_of_game:
        # Prompt user to click to restart game
        draw_click(viewport)
        if game_won:
            # Draw the message "You win!"
            draw_win(viewport)
        elif game_lost:
            # Draw the message "You lose!"
            draw_lose(viewport)
    else: 
        # Draw game objects
        draw_bricks(bricks)
        draw_obstacle(game_obstacle)

        glPushMatrix()
        glTranslate(game_paddle.pos.x, game_paddle.pos.y, 0)
        draw_paddle(game_paddle)
        glPopMatrix()

        glPushMatrix()
        glTranslate(game_ball.pos.x, game_ball.pos.y, 0) 
        draw_ball(game_ball)                        
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
        # Game restart
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_won or game_lost or start_of_game: 
                reset_game()
        # Paddle motion
        elif event.type == pygame.MOUSEMOTION:
            game_paddle.set_pos(event.pos[0], viewport)
        
    update() 
    display() 


# Reset the game and allow the user to continue playing
def reset_game(): 
    global bricks
    global game_ball
    global game_won
    global game_lost
    global start_of_game

    bricks = create_bricks()
    game_ball = ball()
    game_won = False
    game_lost = False
    start_of_game = False


if __name__ == "__main__": 
    init_game() 

    while True:
        game_loop()