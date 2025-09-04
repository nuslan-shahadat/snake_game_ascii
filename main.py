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

FPS = 60

FOOD_TEXTURE = " O"
RANDOM_FOOD = 0


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
    RANDOM_FOOD = random.randint(0,(ROW*COLUMN)-1)
    for i in SNAKE_POS:
        if i == RANDOM_FOOD or i == mid_index():
            return generate_random_food
    return RANDOM_FOOD

def move_up():
    
    if SNAKE_POS[0] < ROW and UP == True:
        GRID[-(ROW-SNAKE_POS[0])] = SNAKE_TEXTURE
        SNAKE_POS.insert(0,-(ROW-SNAKE_POS[0]))
        SNAKE_POS.pop(-1)
    else:
        SNAKE_POS.insert(0,(SNAKE_POS[0]-ROW))

def move_down():
    if SNAKE_POS[0] > (ROW*COLUMN)-ROW-1 and DOWN == True:
        GRID[ROW-SNAKE_POS[0]+1] = SNAKE_TEXTURE
        SNAKE_POS.insert(0,ROW-SNAKE_POS[0]+1)
        SNAKE_POS.pop(-1)
    else:
        SNAKE_POS.insert(0,(SNAKE_POS[0]+ROW))


def move_right():
    if SNAKE_POS[0] % ROW == ROW-1 and RIGHT == True:
        GRID[SNAKE_POS[0]-ROW+1] = SNAKE_TEXTURE
        SNAKE_POS.insert(0,(SNAKE_POS[0]-ROW+1))
        SNAKE_POS.pop(-1)
    else:
        SNAKE_POS.insert(0,(SNAKE_POS[0]+1))

def move_left():
    if SNAKE_POS[0] % ROW == 0 and LEFT == True:
        GRID[SNAKE_POS[0]+ROW-1] = SNAKE_TEXTURE
        SNAKE_POS.insert(0,(SNAKE_POS[0]+ROW-1))
        SNAKE_POS.pop(-1)
    else:
        SNAKE_POS.insert(0,(SNAKE_POS[0]-1))


def snake_update():
    if len(SNAKE_POS) == 0:
        SNAKE_POS.insert(0,mid_index())
        # SNAKE_POS.insert(0,mid_index())

    if len(SNAKE_POS) > SNAKE_LENGTH:
        
        GRID[SNAKE_POS[-1]] = BACKGROUND
        SNAKE_POS.pop(-1)
    if SNAKE_POS[0] % ROW != ROW-1 and SNAKE_POS[0] % ROW != 0 :
        GRID[int(SNAKE_POS[0])] = SNAKE_TEXTURE
    print(SNAKE_POS)



def food_update():
    RANDOM_FOOD = generate_random_food()
    print(RANDOM_FOOD)
    GRID[int(RANDOM_FOOD)] = FOOD_TEXTURE

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

FOOD_POS = generate_random_food()
food_update()
async def check_food():
    global SNAKE_LENGTH
    for i in SNAKE_POS:
        if i == RANDOM_FOOD:
            food_update()
            SNAKE_LENGTH += 1


while GAME_LOOP:
    asyncio.run(event_checker())
    snake_move()
    asyncio.run(check_food())
    asyncio.run(update_window())
    


    


