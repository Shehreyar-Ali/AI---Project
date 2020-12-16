import random

# maze = []
# visited = []
# stack = []
# grid = []

# rowLimit = None
# colLimit = None

def initMaze(n, m, maze, grid):


    rowLimit = n*2
    colLimit = m*2


    rowLimit = n*2
    colLimit = m*2

    n*=2
    m*=2

    for i in range(m):
        maze.append([1]*(n-1))

    
    

    for i in range(1,n):
        for j in range(1,m-1):
            grid.append((i,j))

    maze[0][1] = 0
    maze[-1][-2] = 0

    

    # for i in grid:
    #     print(i)

    return maze, grid, rowLimit, colLimit
    
def showMaze(maze):
    for i in maze:
        print(i)

def putZero(row, col, maze):
    # print("zero")
    maze[row][col] = 0


def createMaze(row, col, rowLimit, colLimit, maze, grid, visited, stack):
    stack.append((row, col))
    visited.append((row, col))

    # print(stack, visited)

    while len(stack) > 0 and (row,col) != (rowLimit-1, colLimit - 2):
    # for i in range(10):

        cell = []

        if (row + 2, col) not in visited and (row + 2, col) in grid:       
            cell.append("down")
            

        if (row - 2, col) not in visited and (row - 2, col) in grid:       
            cell.append("up")
            

        if (row , col + 2) not in visited and (row , col + 2) in grid:     
            cell.append("right")
            

        if (row, col - 2) not in visited and (row , col - 2) in grid:      
            cell.append("left")
            
        
        if len(cell) > 0:

            if len(cell) > 0:                                          # check to see if cell list is emptcol
                cell_chosen = (random.choice(cell))                    # select one of the cell randomlcol

            if cell_chosen == "down":# and col + 2 < colLimit :                             # if this cell has been chosen
                putZero(row + 1,col,maze)
                putZero(row + 2,col,maze)
                
                # print("down",(row,col),"->",(row + 2, col))                                   
                
                row = row + 2                                          # make this cell the current cell
                visited.append((row, col))                              # add to visited list
                stack.append((row, col))                                # place current cell on to stack

            elif cell_chosen == "up":# and col - 2 > -colLimit:
                putZero(row - 1,col,maze)
                putZero(row - 2,col,maze)

                # print("up",(row,col),"->",(row - 2, col))
                
                row = row - 2
                visited.append((row, col))
                stack.append((row, col))

            elif cell_chosen == "right":# and row + 2 < rowLimit:
                putZero(row,col + 1,maze)
                putZero(row,col + 2,maze)
                
                # print("right", (row,col),"->",(row , col + 2))

                col = col + 2
                visited.append((row, col))
                stack.append((row, col))

            elif cell_chosen == "left":# and row - 2 > -rowLimit:
                putZero(row,col - 1,maze)
                putZero(row,col - 2,maze)
                
                # print("left",(row,col),"->",(row , col - 2))

                col = col - 2
                visited.append((row, col))
                stack.append((row, col))
        else:
            row, col = stack.pop()                                    # if no cells are available pop one from the stack


def endPoint(maze):
    result = []
    for i in range(len(maze)):
        if (maze[i].count(0) == 1 and i >0):
            result.append(i)
            result.append(maze[i].index(0))
    return result[0], result[1]




def main(x, y, timing, maze, grid):
    visited = []
    stack = []
    maze1, grid1, rowLimit, colLimit = initMaze(x,y,maze,grid)
    createMaze(0,1,rowLimit,colLimit,maze1,grid1, visited, stack)
    z = maze.pop(0)

    if not timing:
        showMaze(maze1)
    
    return maze1


# maze, grid, rowLimit, colLimit = initMaze(20,20)
# createMaze(0,1)
# showMaze()
# maze.pop(0)
# print(len(maze))
# =======

# # print(len(maze))
# >>>>>>> worked-ish


