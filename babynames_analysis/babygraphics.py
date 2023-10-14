"""
File: babygraphics.py
Name: Sunny
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

    # width = (CANVAS_WIDTH - GRAPH_MARGIN_SIZE) // len(YEARS)
    width = (CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) / 12
    line = width * year_index + GRAPH_MARGIN_SIZE
    return line


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT,
                           width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT, text=str(YEARS[i]),
                           anchor=tkinter.SW)


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
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #
    x_value = (CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)
    y_value = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK
    # rank_lst = []
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        for j in range(len(YEARS)):
            year1 = YEARS[j]
            if str(year1) in name_data[name]:
                first_rank = int(name_data[name][str(year1)])
            else:
                first_rank = MAX_RANK + 1
            if j < len(YEARS)-1:
                year2 = YEARS[j + 1]
                if str(year2) in name_data[name]:
                    sec_rank = int(name_data[name][str(year2)])
                else:
                    sec_rank = MAX_RANK + 1
                if first_rank > MAX_RANK and sec_rank > MAX_RANK or first_rank > MAX_RANK and sec_rank == MAX_RANK:
                    canvas.create_line(GRAPH_MARGIN_SIZE + j * x_value, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       GRAPH_MARGIN_SIZE + (j + 1) * x_value, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, fill=COLORS[i % len(COLORS)])
                    canvas.create_text(GRAPH_MARGIN_SIZE + j * x_value + TEXT_DX,
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       text=str(name) + str("*"), anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

                elif first_rank > MAX_RANK > sec_rank:
                    canvas.create_line(GRAPH_MARGIN_SIZE + j * x_value, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       GRAPH_MARGIN_SIZE + (j + 1) * x_value, GRAPH_MARGIN_SIZE + sec_rank * y_value,
                                       width=LINE_WIDTH, fill=COLORS[i % len(COLORS)])
                    canvas.create_text(GRAPH_MARGIN_SIZE + j * x_value + TEXT_DX,
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       text=str(name) + str(" *"), anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

                elif first_rank < MAX_RANK and sec_rank < MAX_RANK:
                    canvas.create_line(GRAPH_MARGIN_SIZE + j * x_value, GRAPH_MARGIN_SIZE + first_rank * y_value,
                                       GRAPH_MARGIN_SIZE + (j + 1) * x_value, GRAPH_MARGIN_SIZE + sec_rank * y_value,
                                       width=LINE_WIDTH, fill=COLORS[i % len(COLORS)])
                    canvas.create_text(GRAPH_MARGIN_SIZE + j * x_value + TEXT_DX,
                                       GRAPH_MARGIN_SIZE + first_rank * y_value,
                                       text=str(name) + str(first_rank), anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

                elif first_rank < MAX_RANK < sec_rank or first_rank < MAX_RANK and sec_rank == MAX_RANK:
                    canvas.create_line(GRAPH_MARGIN_SIZE + j * x_value, GRAPH_MARGIN_SIZE + first_rank * y_value,
                                       GRAPH_MARGIN_SIZE + (j + 1) * x_value, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, fill=COLORS[i % len(COLORS)])
                    canvas.create_text(GRAPH_MARGIN_SIZE + j * x_value + TEXT_DX,
                                       GRAPH_MARGIN_SIZE + first_rank * y_value,
                                       text=str(name) + str("*"), anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
            else:
                if first_rank > MAX_RANK:
                    canvas.create_text(GRAPH_MARGIN_SIZE + j * x_value + TEXT_DX,
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       text=str(name) + str("*"), anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

                elif first_rank > MAX_RANK:
                    canvas.create_text(GRAPH_MARGIN_SIZE + j * x_value + TEXT_DX,
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       text=str(name) + str(" *"), anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

                elif first_rank < MAX_RANK:
                    canvas.create_text(GRAPH_MARGIN_SIZE + j * x_value + TEXT_DX,
                                       GRAPH_MARGIN_SIZE + first_rank * y_value,
                                       text=str(name) + str(first_rank), anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

                elif first_rank < MAX_RANK:
                    canvas.create_text(GRAPH_MARGIN_SIZE + j * x_value + TEXT_DX,
                                       GRAPH_MARGIN_SIZE + first_rank * y_value,
                                       text=str(name) + str("*"), anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])


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
