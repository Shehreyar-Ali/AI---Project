import astar as ast
import bfs
import time
import mazeCreator as mc
import matplotlib.pyplot as plt
# import breezypythongui as bpg
import tkinter as tk
from tkinter import ttk
plt.style.use('seaborn-whitegrid')

# a = mc.main(20,20,True,[],[])
# start = 0,1
# ending = mc.endPoint(a)

# ast.main(a,start,ending,False)

# bfs.main(a,start,ending,False)





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




def main(itr,dimensions,showMazeGifs = False):

    print(showMazeGifs)

    if showMazeGifs:
        mazeTesting(1,dimensions,dimensions,False,True)

    else:
        astTime, bfsTime = mazeTesting(itr,dimensions,dimensions,False,False)

        plt.clf()
        
        plt.plot([i for i in range(len(astTime))], astTime, label = "A star")
        plt.plot([i for i in range(len(bfsTime))], bfsTime, label = "BFS")

        plt.xlabel("Iterations")
        plt.ylabel("Time taken/s")
        plt.title("A star vs BFS maze solver")
        plt.legend()
        
        plt.show()
    



def interface():

    root = tk.Tk()
    root.geometry("800x200")

    itr_label = tk.Label(text = "Please input number of iterations")
    itr_label.pack(side = tk.LEFT)

    itr_entry = tk.Entry(root, width = 15, bd = 5)
    itr_entry.pack(side = tk.LEFT)
    
    dim_label = tk.Label(text = "Please input a number for the n x n maze to be made")
    dim_label.pack(side = tk.LEFT)

    dim_entry = tk.Entry(root, width = 15, bd = 5)
    dim_entry.pack(side = tk.LEFT)

    status = tk.IntVar()

    showMaze_checkbox = tk.Checkbutton(root, text = "Create Gif?", variable = status )
    showMaze_checkbox.pack(side = tk.RIGHT)

    b1 = ttk.Button(root, text = "Run")
    
    b1.config(command = lambda: main( int(itr_entry.get()), int(dim_entry.get()),  status.get() ))
    b1.pack(side = tk.BOTTOM)

    

    root.mainloop()

interface()

# for i in range(3):
#     main(5,10,True)
#     time.sleep(3)





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