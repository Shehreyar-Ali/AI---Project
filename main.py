import astar as ast
import bfs

import mazeCreator as mc

mc.main(10,10,True)
a = mc.maze
start = 0,1
ending = mc.endPoint()

ast.main(a,start,ending,False)

bfs.main(a,start,ending,False)


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









