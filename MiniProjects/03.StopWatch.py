# http://www.codeskulptor.org/#user12_6vaz1HhhOq_80.py
# http://www.codeskulptor.org/#user12_JXilvVaUvP3CKjC.py
# "Stopwatch: The Game"
import simplegui
import math

# define global variables
width = 300
height = 200
font_size_time = 36
interval = 100
font_color_time = "White"
font_size_game = 24
font_color_game = "Green"
time = 0
# keep track of the number of times that you have stopped the watch 
nbr_stop_watch = 0
# how many times you manage to stop the watch on a whole second
nbr_win = 0

prev_time = ''

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):    
    seconds = int(t / 10)        
    # tenths_of_seconds = t % 10
    tenths_of_seconds = round(10*(t/10 - seconds))
    hours   = math.floor(seconds / 3600)
    minutes = math.floor((seconds - (hours * 3600))/60)
    seconds = seconds - (hours * 3600) - (minutes * 60)
    
    str_time = "%d:%02d.%d" % (minutes, seconds, tenths_of_seconds)
    if hours > 0:
        str_time = str(hours)+":"+str_time
    
    return str_time
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global timer    
    timer.start() 
    
def stop_handler():
    global time, timer, nbr_stop_watch, nbr_win,  prev_time   
    str_time = format(time)
    if prev_time != str_time:
        prev_time = str_time
        nbr_stop_watch += 1        
        ts = int(str_time[-1])
        if ts == 0:
            nbr_win += 1            
        timer.stop()    
    
def reset_handler():
    global time, nbr_stop_watch, nbr_win        
    stop_handler()
    time = nbr_stop_watch = nbr_win = 0
    
def draw(canvas):
    str_time = format(time)
    x = width/2-len(str_time)*font_size_time/4
    y = height/2+font_size_time/2
    canvas.draw_text(str_time, [x, y], font_size_time, font_color_time)
    
    x = 0.75*width
    y = 0.25*height
    str_game = "%d/%d" % (nbr_win, nbr_stop_watch)
    canvas.draw_text(str_game, [x, y], font_size_game, font_color_game)
       
# define event handler for timer with 0.1 sec interval
def time_handler():
    global time    
    time+=1
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)
button_start = frame.add_button("Start", start_handler, 100)
button_stop  = frame.add_button("Stop" , stop_handler, 100)
button_reset = frame.add_button("Reset", reset_handler, 100)

# register draw handler    
frame.set_draw_handler(draw)

# register event handlers
timer = simplegui.create_timer(interval, time_handler)

# start timer and frame
timer.start()
frame.start()


