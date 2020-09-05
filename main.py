import random
import os

grid = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
players = ["O", "X"]
turn = random.randint(0, len(players) - 1)

def displayGrid():
    os.system("cls")
    for i in grid:
        print(" ".join(i))
    print()
        
def checkResult():
    t = players[turn]
    win = False
    for y in range(3):
        if grid[y][0] == t and grid[y][1] == t and grid[y][2] == t:
            win = True
    for x in range(3):
        if grid[0][x] == t and grid[1][x] == t and grid[2][x] == t:
            win = True
    if grid[0][0] == t and grid[1][1] == t and grid[2][2] == t:
        win = True
    if grid[2][0] == t and grid[1][1] == t and grid[0][2] == t:
        win = True
    checked = 0
    for y in range(3):
        for x in range(3):
            if grid[y][x] != "-":
                checked += 1
    if win:
        return t
    elif checked == 9:
        return -1
    else:
        return 0
    
while True:
    displayGrid()
    pos = input("Player " + players[turn] + ", (x y) : ").split()
    grid[int(pos[1])][int(pos[0])] = players[turn]
    if checkResult() != 0:
        break;
    turn = (turn + 1) % len(players)

displayGrid()

if (checkResult() == -1):
    print("Equality !")
else:
    print("Player " + checkResult() + " win the game !")