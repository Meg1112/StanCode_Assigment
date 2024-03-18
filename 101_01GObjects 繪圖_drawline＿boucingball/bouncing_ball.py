"""
File: bouncing_ball.py
Name:Meg
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
ball.fill_color = "black"
window.add(ball)
count = 0
stop = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(drop)


def drop(mouse):
    global stop
    global ball
    global count
    h_move = GRAVITY
    stop += 1
    if stop > 1:  # if in bouncing, make mouseclick no use.
        pass
    else:
        while True:
            if count >= 3:  # if bouncing ball run >= 3 times,then put back ball and stop the game.
                break
            ball.move(VX, h_move)
            if ball.x >= window.width:  # put ball to original location.
                count += 1  # count how many time the bouncing ball run.
                ball_round = GOval(SIZE, SIZE, x=START_X, y=START_Y)
                ball_round.filled = True
                ball_round.fill_color = "black"
                ball = ball_round
                stop = 0  # After bouncing, make "stop" return to 0.
                return window.add(ball_round)
            if ball.y >= window.height:  # if ball drop on the ground.
                h_move = -h_move * REDUCE
            elif GRAVITY == 0:  # if ball  bouncing on the top.
                h_move = -h_move
            else:
                h_move += GRAVITY
            pause(DELAY)
        end_ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)  # Make new different ball in window,then function will stop.
        end_ball.filled = True
        end_ball.fill_color = "black"
        window.add(end_ball)


if __name__ == "__main__":
    main()
