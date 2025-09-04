import math

ROW = 21
COLUMN = 21

BORDER_UP = "-"
BORDER_DOWN = "-"
BORDER_RIGHT = "|"
BORDER_LEFT = "|"

BACKGROUND = " ."

GRID = [BACKGROUND for _ in range(ROW*COLUMN)]

def print_grid():
    grid = GRID
    for i in range(COLUMN-1):
        grid.insert((i+1)*ROW+i,"\n")
    grid =  "".join(grid)
    print(grid)


def mid_index():
    mid_row = ROW//2
    return (mid_row*COLUMN)+(mid_row)
