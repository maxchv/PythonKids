#!/usr/bin/env python
# -*- coding: utf8 -*-
# Rock-paper-scissors-lizard-Spock 
# http://www.codeskulptor.org/#user2-UzuxyQUAPQ-16.py
# http://www.codeskulptor.org/#user10_tc5hCGsKnf_3.py
# Первый мини-проект: написать простейшую игру камень ножница бумага
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
names = ['rock', 'Spock', 'paper', 'lizard', 'scissors']


# helper functions

def number_to_name(number):
    # fill in your code below

    # convert number to a name using if/elif/else
    # don't forget to return the result!    
    return names[number]


def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    return names.index(name)


def rpsls(name):
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4)

    # compute difference of player_number and comp_number modulo five
    result = (player_number - comp_number) % 5

    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)

    # print results
    print("Player choose", name)
    print("Computer choose", comp_name)

    # determine winner    
    if result == 0:
        print("Player and computer tie!")
    elif result > 2:
        print("Computer wins!")
    else:
        print("Player wins!")

    print()


def rpsls_test(name, comp_name):
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    comp_number = name_to_number(comp_name)

    # compute difference of player_number and comp_number modulo five
    result = (player_number - comp_number) % 5

    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)

    # print results
    print("Player choose", name)
    print("Computer choose", comp_name)

    # determine winner    
    if result == 0:
        print("Player and computer tie!")
    elif result > 2:
        print("Computer wins!")
    else:
        print("Player wins!")

    print()


# test your code
# rpsls("rock")
# rpsls("Spock")
# rpsls("paper")
# rpsls("lizard")
# rpsls("scissors")

# always remember to check your completed program against the grading rubric
rpsls_test("rock", "scissors")
rpsls_test("Spock", "lizard")
rpsls_test("paper", "lizard")
rpsls_test("lizard", "scissors")
rpsls_test("scissors", "Spock")
