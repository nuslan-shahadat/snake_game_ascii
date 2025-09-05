import keyboard
import os
import asyncio
import random
import math
import sys

ROW = 15
COLUMN = 15

BACKGROUND = " ."
FOOD_TEXTURE = " #"
SNAKE_TEXTURE = " 0"

GRID = [BACKGROUND for _ in range(ROW*COLUMN)]

SNAKE_POS = []
SNAKE_LENGTH = 2

GAME_LOOP = True

UP = False
DOWN = False
RIGHT = False
LEFT = False

FPS = 600

RANDOM_FOOD = 2
CURRENT_MOVE = 0

DIFF = (ROW*COLUMN)-ROW

SCORE = 0
SCORE_VALUE = 10


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
    if SNAKE_POS[0] < ROW and UP == True:
        SNAKE_POS.insert(0,SNAKE_POS[0]+DIFF)
    else:
        SNAKE_POS.insert(0,SNAKE_POS[0]-ROW)

def move_down():
    if SNAKE_POS[0] >= DIFF and DOWN == True:
        SNAKE_POS.insert(0,SNAKE_POS[0]-DIFF)
    else:
        SNAKE_POS.insert(0,SNAKE_POS[0]+ROW)


def move_right():
    if (SNAKE_POS[0] % ROW == ROW-1) and RIGHT == True:
        SNAKE_POS.insert(0,SNAKE_POS[0]-ROW+1)
    else:
        SNAKE_POS.insert(0,SNAKE_POS[0]+1)

def move_left():
    if (SNAKE_POS[0] % ROW == 0) and LEFT == True:
        SNAKE_POS.insert(0,SNAKE_POS[0]+ROW-1)
    else:
        SNAKE_POS.insert(0,SNAKE_POS[0]-1)


def snake_update():
    if len(SNAKE_POS) == 0:
        SNAKE_POS.insert(0,mid_index())

    if len(SNAKE_POS) > SNAKE_LENGTH:
        GRID[SNAKE_POS[-1]] = BACKGROUND
        SNAKE_POS.pop(-1)

    GRID[int(SNAKE_POS[0])] = SNAKE_TEXTURE



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
    score_str = f"SCORE: {SCORE}"
    print(((ROW//2)-(len(score_str)//2)+2)*"  ",score_str)
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
    global SCORE
    global SNAKE_LENGTH
    global RANDOM_FOOD
    GRID[RANDOM_FOOD] = FOOD_TEXTURE
    if SNAKE_POS[0] == RANDOM_FOOD:
        SNAKE_LENGTH += 1
        SCORE += SCORE_VALUE
        GRID[RANDOM_FOOD] = SNAKE_TEXTURE
        generate_random_food()

def death_check():
    global GAME_LOOP
    for index,i in enumerate(SNAKE_POS):
        if index != 0:
            if i == SNAKE_POS[0]:
                GAME_LOOP = False
while GAME_LOOP:
    asyncio.run(event_checker())
    snake_move()
    asyncio.run(update_window())
    asyncio.run(food_update())
    death_check()
clear_window()
final_str = f"Final Score: {SCORE}"
game_over_str = "GAME OVER" 

extra1 = 3
extra2 = 5
print(
    f"""
        {ROW*"##"}
        {"#"+(ROW-2)*"  "+"  #"}
        {"#"+((math.ceil((ROW-len(game_over_str))/2)-1)+extra1)*"  "+game_over_str+((ROW-(math.ceil((ROW-len(game_over_str))/2)+math.ceil(len(game_over_str)/2)+1))-extra1)*"  "+"  #"}
        {"#"+(ROW-2)*"  "+"  #"}
        {ROW*"##"}
        {"#"+(ROW-2)*"  "+"  #"}
        {"#"+((math.ceil((ROW-len(final_str))/2)-1)+extra2)*"  "+final_str+((ROW-(math.ceil((ROW-len(final_str))/2)+math.ceil(len(final_str)/2)+1))-extra2)*"  "+"  #"}
        {"#"+(ROW-2)*"  "+"  #"}
        {ROW*"##"}


        press 'esc' to leave.....
    """)
keyboard.wait("esc")
clear_window()
sys.exit()


    


