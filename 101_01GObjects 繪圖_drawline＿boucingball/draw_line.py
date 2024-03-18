"""
File: draw_line.py
Name:Meg
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5
window = GWindow()
count = 0
one_object_x = 0
one_object_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(circle)


def circle(mouse):
    global count
    global one_object_x
    global one_object_y
    count += 1
    if count % 2 != 0:  # if click time is odd, then draw a circle
        one_object_x = mouse.x-SIZE/2  # keep x position of circle
        one_object_y = mouse.y-SIZE/2  # keep y position of circle
        click_circle = GOval(SIZE, SIZE, x=one_object_x, y=one_object_y)
        window.add(click_circle)
    else:  # if click times is not odd, then cancel circle and draw a line
        r_circle = window.get_object_at(one_object_x+SIZE/2, one_object_y+SIZE/2)  # find (x, y)at center of circle
        if r_circle is not None:
            window.remove(r_circle)  # remove circle
        draw_line = GLine(one_object_x, one_object_y, mouse.x, mouse.y)
        window.add(draw_line)


if __name__ == "__main__":
    main()
