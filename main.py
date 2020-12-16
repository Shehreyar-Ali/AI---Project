import astar as ast
import bfs
import time
import mazeCreator as mc
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')



def mazeTesting(itr, x, y, showOutput, showMaze):

    showMaze = not showMaze

    ast_timeTakenList = []
    bfs_timeTakenList = []

    for i in range(itr):

        a = mc.main(x,y,True,[],[])

        start = 0,1
        ending = mc.endPoint(a)
        

        start1 = time.time()
        ast.main(a,start,ending,showMaze)
        end1 = time.time()
        

        start2 = time.time()
        bfs.main(a,start,ending,showMaze)
        end2 = time.time()

        ast_timeTakenList.append(end1-start1)
        bfs_timeTakenList.append(end2-start2)

        if showOutput:
            print('ASTAR Iteration: ', i, ' Time Taken:  ', end1-start1)
            print('BFS Iteration: ', i, ' Time Taken:  ', end2-start2 )

    
    return ast_timeTakenList, bfs_timeTakenList




def main(timing):
    
    astTime, bfsTime = mazeTesting(100,10,10,False, not timing)

    if timing:
        plt.plot([i for i in range(len(astTime))], astTime, label = "A star")
        plt.plot([i for i in range(len(bfsTime))], bfsTime, label = "BFS")

        plt.xlabel("Iterations")
        plt.ylabel("Time taken/s")
        plt.title("A star vs BFS maze solver")
        plt.legend()
        
        plt.show()



main(True)





# mc.main(20,20,True)
# a = mc.maze
# start = 0,1
# ending = mc.endPoint()

# ast.main(a,start,ending,True)

# bfs.main(a,start,ending,True)






"""

    Create Maze and all its req stuff

    ------------------------------------------------

        [start timer1]

    Run ast for that maze - {doesnt draw out image}

        [end timer1]

    ------------------------------------------------

        [start timer2]

    Run bfs for that maze - {doesnt draw out image}

        [end timer2]

    ------------------------------------------------


    ast_timeTakenList.append(time1)
    bfs_timeTakenList.append(time2)


"""