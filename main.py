import time

ROW = 11
COLUMN = 11

BACKGROUND = " ."

GRID = [BACKGROUND for _ in range(ROW*COLUMN)]

SNAKE_POS = []
SNAKE_TEXTURE = " @"
SNAKE_LENGTH = 2

def print_grid():
    grid = GRID.copy()
    for i in range(COLUMN-1):
        grid.insert((i+1)*ROW+i,"\n")
    grid =  "".join(grid)
    print(grid)


def mid_index():
    mid_row = ROW//2
    return (mid_row*COLUMN)+(mid_row)


def move_up():
    SNAKE_POS.insert(0,(SNAKE_POS[0]-ROW))

def move_down():
    SNAKE_POS.insert(0,(SNAKE_POS[0]+ROW))

def move_right():
    SNAKE_POS.insert(0,(SNAKE_POS[0]+1))

def move_left():
    SNAKE_POS.insert(0,(SNAKE_POS[0]-1))

def snake_update():
    if len(SNAKE_POS) == 0:
        SNAKE_POS.insert(0,mid_index())

    if len(SNAKE_POS) > SNAKE_LENGTH:
        GRID.pop(SNAKE_POS[len(SNAKE_POS)-1])
        GRID.insert(SNAKE_POS[len(SNAKE_POS)-1],BACKGROUND)
        SNAKE_POS.pop(len(SNAKE_POS)-1)
    GRID[SNAKE_POS[0]] = SNAKE_TEXTURE
    # print(SNAKE_POS)
    # print(SNAKE_POS[len(SNAKE_POS)-1])
    # print(SNAKE_POS[0])
    # print(GRID)


# snake_update()
# print_grid()
# time.sleep(1)
# move_down()
# snake_update()
# print_grid()
# time.sleep(1)
# move_left()
# snake_update()
# print_grid()
# time.sleep(1)
# move_left()
# snake_update()
# print_grid()
# time.sleep(1)
# move_up()
# snake_update()
# print_grid()
# time.sleep(1)
# move_right()
# snake_update()
# print_grid()

