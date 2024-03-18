"""
File: MidpointKarel.py
Name: Meg
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:Karel is on(1,1),facing east
    post-condition:Karel is at center of 1st Street
    """
    put_one_line_beeper()
    while front_is_clear():
        move()
        west_side_pick_beeper()
        east_side_pick_beeper()


def put_one_line_beeper():
    """
    pre-condition:Karel is on(1,1),facing east
    post-condition:Karel is on far right,facing west
    """
    while front_is_clear():
        move()
        put_beeper()
    pick_beeper()
    turn_around()


def east_side_pick_beeper():
    """
    pre-condition:Karel is on far right,facing east
    post-condition:Karel was picked Easternmost side beeper,facing west
    """
    if not front_is_clear():
        if facing_east():
            turn_around()#facing west
            while not on_beeper():
                move()
            if front_is_clear():
                move()
            if front_is_clear():
                move()
            if on_beeper():
                turn_around()#facing east
                move()
                move()
                pick_beeper()
                turn_around()#facing west
            else:
                turn_around()#facing east
                if front_is_clear():
                    move()
                if on_beeper():
                    move()
                    if on_beeper():
                        pick_beeper()
                        turn_around()#facing west
                else:
                    back_to_center()


def west_side_pick_beeper():
    """
    pre-condition:Karel is on far left,facing west
    post-condition:Karel was picked westernmost side beeper,facing east
    """
    if not front_is_clear():
        if facing_west():
            turn_around()#facing east
            while not on_beeper():
                move()
            if front_is_clear():
                move()
            if front_is_clear():
                move()
            if on_beeper():
                turn_around()#facing west
                move()
                move()
                pick_beeper()
                turn_around()#facing east
            else:
                turn_around()#facing west
                if front_is_clear():
                    move()
                if on_beeper():
                    move()
                    if on_beeper():
                        pick_beeper()
                        turn_around()#facing east
                else:
                    back_to_center()


def back_to_center():
    """
    pre-condition:Karel is on street one anypoint
    post-condition:Karel is on beeper,facing south
    """
    while front_is_clear():
        move()
    turn_around()
    while not on_beeper():
        move()
    if facing_west():
        turn_left()
    else:
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
