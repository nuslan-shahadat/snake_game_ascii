import keyboard
import os
import asyncio
import random

ROW = 20
COLUMN = 20

BACKGROUND = " ."

GRID = [BACKGROUND for _ in range(ROW*COLUMN)]

SNAKE_POS = []
SNAKE_TEXTURE = " @"
SNAKE_LENGTH = 3

GAME_LOOP = True

UP = False
DOWN = False
RIGHT = False
LEFT = False

FPS = 30

FOOD_TEXTURE = " O"
RANDOM_FOOD = 2
CURRENT_MOVE = 0


def print_grid():
    grid = GRID.copy()
    for i in range(COLUMN-1):
        grid.insert((i+1)*ROW+i,"\n")
    grid =  "".join(grid)
    print(grid)


def mid_index():
    mid_row = ROW//2
    return (mid_row*COLUMN)+(mid_row)

def generate_random_food():
    global RANDOM_FOOD
    RANDOM_FOOD = random.choice(list(set(i for i in range(ROW*COLUMN))-set(SNAKE_POS)))

def move_up():
    SNAKE_POS.insert(0,abs(SNAKE_POS[0]-ROW))

def move_down():
    SNAKE_POS.insert(0,abs(SNAKE_POS[0]+ROW))


def move_right():
    SNAKE_POS.insert(0,abs(SNAKE_POS[0]+1))

def move_left():
    SNAKE_POS.insert(0,abs(SNAKE_POS[0]-1))


def snake_update():
    if len(SNAKE_POS) == 0:
        SNAKE_POS.insert(0,mid_index())
        SNAKE_POS.insert(0,mid_index())

    if len(SNAKE_POS) > SNAKE_LENGTH:
        
        GRID[SNAKE_POS[-1]] = BACKGROUND
        SNAKE_POS.pop(-1)
    if SNAKE_POS[0] % ROW != ROW-1 and SNAKE_POS[0] % ROW != 0 :
        GRID[int(SNAKE_POS[0])] = SNAKE_TEXTURE
    print(SNAKE_POS)



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

    global CURRENT_MOVE

    if UP and CURRENT_MOVE != 2:
        CURRENT_MOVE = 1

    if DOWN and CURRENT_MOVE != 1:
        CURRENT_MOVE = 2

    if RIGHT and CURRENT_MOVE != 4:
        CURRENT_MOVE = 3

    if LEFT and CURRENT_MOVE != 3:
        CURRENT_MOVE = 4
    
    
    if CURRENT_MOVE == 1:
        move_up()

    if CURRENT_MOVE == 2:
        move_down()

    if CURRENT_MOVE == 3:
        move_right()

    if CURRENT_MOVE == 4:
        move_left()

async def food_update():
    global SNAKE_LENGTH
    global RANDOM_FOOD
    GRID[RANDOM_FOOD] = FOOD_TEXTURE
    if SNAKE_POS[0] == RANDOM_FOOD:
        SNAKE_LENGTH += 1
        GRID[RANDOM_FOOD] = SNAKE_TEXTURE
        generate_random_food()


while GAME_LOOP:
    asyncio.run(event_checker())
    snake_move()
    asyncio.run(update_window())
    asyncio.run(food_update())
    


    


