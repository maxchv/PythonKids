#http://www.codeskulptor.org/#user14_2efEcq2Lra_76.py
# implementation of card game - Memory

import simpleguitk as simplegui
import random

# helper function to initialize globals
def init():
    global MOVES, CARDS, STATE, PREV, PREVPREV, label
    CARDS = {}
    MOVES = 1
    STATE = 0
    PREV = None
    PREVPREV = None
    label.set_text("Moves = 0")
    vals = list(range(8))*2
    random.shuffle(vals)
    for i in range(16):
        CARDS[i]={"click": False,    # it is exposed          
                  "value": vals[i]}
     
# define event handlers
def mouseclick(pos):
    global label, MOVES, STATE, PREV, PREVPREV
    CURR = pos[0]//50    
    if not CARDS[CURR]["click"]:
        CARDS[CURR]["click"] = True
        if STATE == 0:
            STATE = 1        
        elif STATE == 1:        
            STATE = 2                  
        else:
            if CARDS[PREV]['value'] != CARDS[PREVPREV]['value']:                                                    
                CARDS[PREV]["click"] = False                            
                CARDS[PREVPREV]["click"] = False                
            STATE = 1
            MOVES+=1                           
        label.set_text("Moves = "+str(MOVES))
        PREVPREV = PREV
        PREV = CURR   
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in CARDS:        
        canvas.draw_line((i*50, 0), (i*50, 100), 1, "Red")        
        if CARDS[i]["click"]:
            canvas.draw_polygon([(i*50, 0), ((i+1)*50, 0), ((i+1)*50, 100), (i*50, 100)], 1, "Black", "Black")
            canvas.draw_text(str(CARDS[i]["value"]), (i*50+15, 50+15), 50, "White")
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.set_canvas_background("Green")
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric
