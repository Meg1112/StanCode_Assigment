"""
File: StoneMasonKarel.py
Name: Meg
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:Karel is on the left corner,facing east.
    post-condition:Karel is build all column and on the right corner,facing east
    """
    for i in range(4):
        build_column()
        change_side()
    build_column()
    to_corner()


def build_column():
    """
    pre-condition:Karel is on the left corner,facing east.
    post-condition:Karel is build one line column and on the right corner,facing east
    """
    while front_is_clear():
        if on_beeper():
            for i in range(4):
                move()
        else:
            put_beeper()
            for i in range(4):
                move()
    if not on_beeper():
        put_beeper()


def change_side():
    """
    pre-condition:Karel is build one street column and on the right corner,facing east
    post-condition:Karel is back to left side,facing east
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_left()
        while front_is_clear():
            move()
        turn_around()


def to_corner():
    """
    pre-condition:Karel is on the top of right,facing east
    post-condition:Karel is build all column and on the right corner,facing east
    """
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
