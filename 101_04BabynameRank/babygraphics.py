"""
File: babygraphics.py
Name: Meg
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    width_in = width - GRAPH_MARGIN_SIZE*2
    x_coordinate = year_index*(width_in / len(YEARS)) + GRAPH_MARGIN_SIZE
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas
    # upper line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # lower line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # vertical line and years
    for i in range(len(YEARS)):
        y_1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, y_1, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid
    for i in range(len(lookup_names)):  # count how many name will be drew
        name_s = lookup_names[i]
        # get line color. if too many request, reuse first color
        if i > len(COLORS)-1:
            color = COLORS[i - len(COLORS)]
        else:
            color = COLORS[i]
        for j in range(len(YEARS)):
            name_d = name_data[name_s]
            x_0 = get_x_coordinate(CANVAS_WIDTH, j)
            x_1 = get_x_coordinate(CANVAS_WIDTH, j + 1)
            if str(YEARS[j]) in name_d:  # if year(no rank) in name_data
                # get first y point
                y_0 = int(name_d[str(YEARS[j])])+GRAPH_MARGIN_SIZE
                if y_0 > CANVAS_HEIGHT - GRAPH_MARGIN_SIZE:
                    y_0 = y_0 * (CANVAS_HEIGHT/MAX_RANK)  # rank
                # mark name and rank
                canvas.create_text(x_0 + TEXT_DX, y_0, text=name_s + str(name_d[str(YEARS[j])]),
                                   anchor=tkinter.SW, fill=color)
            else:
                y_0 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                # mark name and rank
                canvas.create_text(x_0 + TEXT_DX, y_0, text=name_s+"*", anchor=tkinter.SW, fill=color)
            # get second y point
            if j+1 < len(YEARS):
                if str(YEARS[(j + 1)]) in name_d:
                    y_1 = int(name_d[str(YEARS[j+1])])+GRAPH_MARGIN_SIZE
                    if y_1 > CANVAS_HEIGHT - GRAPH_MARGIN_SIZE:
                        y_1 = y_1 * (CANVAS_HEIGHT/MAX_RANK)  # rank
                else:
                    y_1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    # draw line
                canvas.create_line(x_0, y_0, x_1, y_1, fill=color, width=LINE_WIDTH)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
