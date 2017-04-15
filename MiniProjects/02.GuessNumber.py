# http://www.codeskulptor.org/#user11_x45xCJLDzz_22.py
# http://www.codeskulptor.org/#user11_d6b9YIiY9oDC4XE.py
#
# My realisation "Guess the number" 
# input will come from buttons and an input field
# all output for the game will be printed in the console


# Dear classmate, who will test my mini-project #2.
#
# I wrote program with using canvas drawing, 
# though it was not task this mini-project. 
# However I am did is for my pleasure.
# Please, do not take points for this.

import simpleguitk as simplegui
import random
import math

# initialize global variables used in your code
width = 300
height = 200

num_range = 100
secret_number = None
remaining_guesses = None

message = None
message2 = ""


# helper funcion to initial game
def init():
    global secret_number, remaining_guesses, message
    secret_number = random.randrange(0, num_range)
    print("Новая игра. Диапазон от 0 до", num_range)
    remaining_guesses = math.ceil(math.log(num_range, 2))
    print("Number of remaining guesses is ", remaining_guesses, "\n")
    message = "Новая игра [0 " + str(num_range) + ")"


# define event handlers for control panel    
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range, message2
    num_range = 100
    message2 = ""
    init()


def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range, message2
    num_range = 1000
    message2 = ""
    init()


def get_input(guess):
    # main game logic goes here	
    global remaining_guesses, message, message2
    g = int(guess)
    print("Guess was", g)
    remaining_guesses -= 1
    message = "Remaining guesses is " + str(remaining_guesses)
    print("Number of remaining guesses is ", remaining_guesses)
    if remaining_guesses > 0:
        if g > secret_number:
            message2 = "Lower!"
            print("Lower!\n")
        elif g < secret_number:
            message2 = "Higher!"
            print("Higher!\n")
        else:
            message2 = "Correct!"
            print("Correct!\n")
            init()
    else:
        message2 = "You are loser"
        print("You did not guess secret number.")
        print("Secret number was ", secret_number, "\n")
        init()


def draw(canvas):
    canvas.draw_text(message, (width / 2 - len(message) * 11 / 2, height / 3), 20, "Lime")
    canvas.draw_text(message2, (width / 2 - len(message2) * 11 / 2, height * 3 / 4), 20, "Lime")


# create frame
frame = simplegui.create_frame("Угадай число", width, height)

# register event handlers for control elements
frame.add_button("Диапазон [0, 100)", range100, 200)
frame.add_button("Диапазон [0, 1000)", range1000, 200)
frame.add_input("Введите число", get_input, 200)

frame.set_draw_handler(draw)

# start frame

init()

frame.start()
