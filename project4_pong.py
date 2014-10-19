# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
NEW_GAME = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, NEW_GAME # these are vectors stored as lists
    if NEW_GAME:
        print "ola"
        ball_pos = [WIDTH/2, HEIGHT/2]
        x_velocity = 1 #random.randrange(120, 240)
        y_velocity = 1 #random.randrange(60, 180)
        if direction == RIGHT:
            ball_vel = [x_velocity, -y_velocity]
        elif direction == LEFT:
            ball_vel = [-x_velocity,-y_velocity]
        NEW_GAME=False

    #update ball position    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    print ball_pos
    
    #validate colision top
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    #validate colision DOWN
    if ball_pos[1] >= HEIGHT- BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    #validate colision left
    if ball_pos[0] >= (WIDTH - PAD_WIDTH - 1 - BALL_RADIUS):
        # if touch pad
        #ball_vel[0] = -ball_vel[0]
        #elsif
        NEW_GAME=True
        spawn_ball(LEFT)
    
    #validate colision right
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):
        # if touch pad
        ball_vel[0] =  -ball_vel[0]
        #elsif
        NEW_GAME=True
        spawn_ball(RIGHT)
        
    return ball_pos

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global NEW_GAME
    NEW_GAME = True
    spawn_ball(RIGHT)


    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos= spawn_ball(LEFT)
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    #paddle left (1)
    if key == simplegui.KEY_MAP["s"]:
        paddle1_pos[1] += paddle1_vel
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_pos[1] -= paddle1_vel
    
    #paddle right (2)
    if key == simplegui.KEY_MAP["down"]:
        paddle2_pos[1] += paddle2_vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_pos[1] -= paddle2_vel

def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
