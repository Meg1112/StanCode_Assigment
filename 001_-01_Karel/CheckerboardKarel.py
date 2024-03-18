"""
File: CheckerboardKarel.py
Name: Meg
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:Karel is on(1,1),facing east
    post-condition:Karl draw a checkerboard using beepers
    """
    while front_is_clear():
        fill_one_line()
        back_to_left_even()
        change_line()
    fill_one_vertical_line()
    back_to_down()


def fill_one_vertical_line():
    """
    pre-condition:Karel is on left,facing east
    post-condition:Karel is on vertical top,fill beepers in one vertical line,and facing north
    """
    if facing_east():
        turn_left()
        while front_is_clear():
            if not on_beeper():
                put_beeper()
            if front_is_clear():
                move()
            if front_is_clear():
                move()


def back_to_down():
    """
    pre-condition:Karel is on vertical top,fill beepers in one vertical line,and facing north
    post-condition:Karel is on vertical bottom,and facing south
    """
    if facing_north():
        if not front_is_clear():
            if not on_beeper():
                put_beeper()
                turn_around()
                if front_is_clear():
                    move()
                if on_beeper():
                    turn_around()
                    if front_is_clear():
                        move()
                    if on_beeper():
                        pick_beeper()
                    turn_around()
                    while front_is_clear():
                        move()
                else:
                    while front_is_clear():
                        move()


def fill_one_line():
    """
    pre-condition:Karel is on left,facing east
    post-condition:Karel is on right,fill beepers in one line,and facing east
    """
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        if front_is_clear():
            move()
        if front_is_clear():
            move()


def back_to_left_even():
    """
    pre-condition:Karel is on right,fill beepers in one line,and facing east
    post-condition:Karel is on far left,facing west
    """
    if not front_is_clear():
        if not on_beeper():
            put_beeper()
            turn_around()
            move()
            if on_beeper():
                turn_around()
                move()
                if on_beeper():
                    pick_beeper()
                turn_around()
                while front_is_clear():
                    move()
            else:
                while front_is_clear():
                    move()


def change_line():
    """
    pre-condition:Karel is on left, facing west
    post-condition:if Karel is on odd line on far left, facing east or move one step from left side, facing east.
    if in corner facing north.
    """
    if on_beeper():
        turn_right()
        if front_is_clear():
            move()
            turn_right()
            move()
    else:
        turn_right()
        if front_is_clear():
            move()
            turn_right()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
