# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user4-PgyXog4HlK-57.py
import simpleguitk as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

ball_pos    = [WIDTH/2, HEIGHT/2]
ball_vel    = [0, 0]
paddle1_pos = paddle2_pos = HEIGHT/2  
paddle1_vel = paddle2_vel = 0
score1      = score2 = 0

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos    = [WIDTH/2, HEIGHT/2]
    # random y velocity
    x_vel = random.randrange(120, 240)*0.012
    y_vel = random.randrange(60, 180)*0.012
    #x_vel = 1
    #y_vel = random.random()
    # it is choise direction velocity: up or down
    #if random.randrange(2):
    #    y_vel = - y_vel
    
    if right:
        ball_vel = [x_vel, -y_vel]
    else:
        ball_vel = [-x_vel, -y_vel]
    pass

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    score1 = score2 = 0
    paddle1_pos = paddle2_pos = HEIGHT/2
    paddle1_vel = paddle2_vel = 0
    ball_init(random.randrange(2))    
    pass

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel 
 
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    # check position paddle1_pos
    if paddle1_pos <= HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    elif paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT- HALF_PAD_HEIGHT
    # check position paddle2_pos
    paddle2_pos += paddle2_vel
    if paddle2_pos <= HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    elif paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT- HALF_PAD_HEIGHT
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
 
    # draw paddles    
    # left paddles
    c.draw_polygon([(        0, paddle1_pos - HALF_PAD_HEIGHT),  # left upper
                    (        0, paddle1_pos + HALF_PAD_HEIGHT),  # left lower
                    (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT),  # right lower
                    (PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT)], # right upper
                                             1, "White", "White")
    # right paddles
    c.draw_polygon([(WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), # left upper
                    (WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT), # left lower
                    (            WIDTH, paddle2_pos + HALF_PAD_HEIGHT), # right lower
                    (            WIDTH, paddle2_pos - HALF_PAD_HEIGHT)],# right upper
                                                     1, "White", "White")
     
    # update ball
    # left side
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] >= paddle1_pos + HALF_PAD_HEIGHT or ball_pos[1] <= paddle1_pos - HALF_PAD_HEIGHT:
            score2 += 1
            ball_init(True)
        else:
            ball_vel[0] = - ball_vel[0]*1.1
    # right side        
    elif ball_pos[0] >= (WIDTH - PAD_WIDTH - 1) - BALL_RADIUS:
        if ball_pos[1] >= paddle2_pos + HALF_PAD_HEIGHT or ball_pos[1] <= paddle2_pos - HALF_PAD_HEIGHT:
            score1 += 1
            ball_init(False)    
        else:
            ball_vel[0] = - ball_vel[0]*1.1
    # top and bottom sides
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - 1 ) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball and scores    
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    c.draw_text(str(score1), (WIDTH*0.25, HEIGHT*0.15), 30, "White")
    c.draw_text(str(score2), (WIDTH*0.75, HEIGHT*0.15), 30, "White")    

        
def keydown(key):
    global paddle1_vel, paddle2_vel    
    acc = 3

    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
        
    #if key==simplegui.KEY_MAP["space"]:
    #    init()
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)

# start frame
init()
frame.start()

