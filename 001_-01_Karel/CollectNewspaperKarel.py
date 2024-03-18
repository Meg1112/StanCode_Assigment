"""
File: CollectNewspaperKarel.py
Name: Meg
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:Karel is in upper left corner of it house, facing east
    post-condition:Karel is return in the left corner with newspaper,facing east
    """
    move_to_newspaper()
    pick_newspaper_back()


def move_to_newspaper():
    """
    pre-condition:Karel is at(3,6), facing east
    post-condition:Karel was pick newspaper at(6,3) ,facing east
    """
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def pick_newspaper_back():
    """
    pre-condition:Karel was picked newspaper at(6,3) ,facing east
    post-condition:Karel is return to(3,6) with newspaper,facing east
    """
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    while front_is_clear():
        move()
    turn_around()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
