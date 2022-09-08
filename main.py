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
game_won = True
game_lost = False
screen = []


def init_game():
    global clock
    global bricks
    global screen
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
    global game_won
    global game_lost

    delta_time = clock.tick() / 1000

    # Reverse direction if the ball reaches an edge
    game_ball.check_change_dir(viewport)
    # TODO: Add condition lose condition

    # Update position
    game_ball.pos += game_ball.motion * (delta_time * 3.0)

    # Check for collision with bricks
    for b in bricks: 
        if b.check_collision(game_ball.pos):
            bricks.remove(b)
            if len(bricks) == 0: 
                game_won = True

    # Check for collision with paddle
    if game_paddle.check_collision(game_ball):
        game_ball.change_y_dir()

def display(): 
    global bricks
    global game_ball
    global game_won
    global game_lost
    global screen

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
    if game_won or game_lost:
        # font = pygame.font.SysFont(None, 48)
        # font1 = pygame.font.SysFont('chalkduster.ttf', 72)
        # img1 = font1.render('chalkduster.ttf', True, pygame.Color(0, 0, 0))
        # screen.blit(img1, (20, 20))
        # TODO: Figure out how to draw text
        pass
        if game_won:
            # Draw the message "You win!"
            pass
        elif game_lost: 
            # Draw the message "You lose!"
            pass
    else: 
        # Draw game objects
        draw_bricks(bricks)

        glPushMatrix()
        glTranslate(game_paddle.pos.x, game_paddle.pos.y, 0)
        draw_paddle(game_paddle)
        glPopMatrix()

        glPushMatrix()
        glTranslate(game_ball.pos.x, game_ball.pos.y, 0) # if we add +100 to game_ball.pos.x the paddle bounce works,
        draw_ball(game_ball)                             # but we can't do that, how to fix it?
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_won or game_lost: 
                reset_game()
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

    bricks = create_bricks()
    game_ball = ball(point(350, 350), 15, vector(50, -60))
    game_won = False
    game_lost = False


if __name__ == "__main__": 
    init_game() 

    while True:
        game_loop()