import keyboard
import os
import asyncio

ROW = 30
COLUMN = 30

BACKGROUND = " ."

GRID = [BACKGROUND for _ in range(ROW*COLUMN)]

SNAKE_POS = []
SNAKE_TEXTURE = " @"
SNAKE_LENGTH = 10

GAME_LOOP = True

UP = False
DOWN = False
RIGHT = False
LEFT = False

FPS = 30


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

def clear_window():
    os.system("cls")

async def event_checker():

    global UP
    global DOWN
    global RIGHT
    global LEFT

    if keyboard.is_pressed("w"):
        UP = True
        DOWN = False
        RIGHT = False
        LEFT = False
    if keyboard.is_pressed("s"):
        UP = False
        DOWN = True
        RIGHT = False
        LEFT = False
    if keyboard.is_pressed("a"):
        UP = False
        DOWN = False
        RIGHT = False
        LEFT = True
    if keyboard.is_pressed("d"):
        UP = False
        DOWN = False
        RIGHT = True
        LEFT = False

async def update_window():
    clear_window()
    snake_update()
    print_grid()
    await asyncio.sleep(1/FPS)

def snake_move():
    if UP:
        move_up()
    if DOWN:
        move_down()
    if RIGHT:
        move_right()
    if LEFT:
        move_left()

while GAME_LOOP:
    asyncio.run(event_checker())
    snake_move()
    asyncio.run(update_window())
    


    


