
import random

maze = []
visited = []
stack = []
grid = []

def initMaze(n,m):
    for i in range(m):
        maze.append([1]*n)
    
    n -= 1
    m -= 1 
    for i in range(1,n):
        for j in range(2,m):
            grid.append((i,j))
    # print(grid)

    maze[0][1] = 0
    maze[-1][-2] = 0















    

    return maze, grid
    
def showMaze():
    for i in maze:
        print(i)


def putZero(row,col):
    # print("zero")
    maze[row][col] = 0




def createMaze(row, col):
    

    stack.append((row, col))
    visited.append((row, col))

    while len(stack) > 0:

        cell = []

        if (row + 1, col) not in visited and (row + 1, col) in grid:       
            cell.append("right")                                   

        if (row - 1, col) not in visited and (row - 1, col) in grid:       
            cell.append("left")

        if (row , col + 1) not in visited and (row , col + 1) in grid:     
            cell.append("down")

        if (row, col - 1) not in visited and (row , col - 1) in grid:      
            cell.append("up")
        
        if len(cell) > 0:

            if len(cell) > 0:                                          # check to see if cell list is emptcol
                cell_chosen = (random.choice(cell))                    # select one of the cell randomlcol

            if cell_chosen == "right":                             # if this cell has been chosen
                putZero(row,col)     
                # print("right")
                
                row = row + 1                                          # make this cell the current cell
                visited.append((row, col))                              # add to visited list
                stack.append((row, col))                                # place current cell on to stack

            elif cell_chosen == "left":
                putZero(row,col)
                # print("left")
                row = row - 1
                visited.append((row, col))
                stack.append((row, col))

            elif cell_chosen == "down":
                putZero(row,col)
                # print("down")
                col = col + 1
                visited.append((row, col))
                stack.append((row, col))

            elif cell_chosen == "up":
                putZero(row,col)
                # print("up")
                col = col - 1
                visited.append((row, col))
                stack.append((row, col))
        else:
            row, col = stack.pop()                                    # if no cells are available pop one from the stack



maze, grid = initMaze(20,20)
createMaze(1,1)
showMaze()



