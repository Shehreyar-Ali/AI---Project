from PIL import Image, ImageDraw
import visualisation as vs

def make_step(maze,step_num,step_maze):
  for i in range(len(step_maze)):
    for j in range(len(step_maze[i])):
      make_step_helper(i,j,maze,step_num,step_maze)
      
def make_step_helper(i,j,maze,step_num,step_maze):

  if step_maze[i][j] == step_num:

    if i>0 and step_maze[i-1][j] == 0 and maze[i-1][j] == 0:
      step_maze[i-1][j] = step_num + 1
    
    if j>0 and step_maze[i][j-1] == 0 and maze[i][j-1] == 0:
      step_maze[i][j-1] = step_num + 1
    
    if i<len(step_maze)-1 and step_maze[i+1][j] == 0 and maze[i+1][j] == 0:
      step_maze[i+1][j] = step_num + 1
    
    if j<len(step_maze[i])-1 and step_maze[i][j+1] == 0 and maze[i][j+1] == 0:
        step_maze[i][j+1] = step_num + 1

def fill_step_maze(maze,start,ending,timing,step_maze,gif_list):
  i,j = start
  step_maze[i][j] = 1
  step_num = 0

  while step_maze[ending[0]][ending[1]] == 0:
    step_num += 1
    make_step(maze,step_num,step_maze)
    if not timing:
      vs.draw_matrix(maze, step_maze,gif_list,start,ending)



def bfs_process(maze,start,ending,timing,gif_list):
  
  step_maze = [[0 for _ in range (len(maze[0]))] for _ in range (len(maze))]

  fill_step_maze(maze,start,ending,timing,step_maze,gif_list)

  (i, j) = ending
  step_num = step_maze[i][j]
  the_path = [(i,j)]
  
  while step_num > 1:
    if i > 0 and step_maze[i - 1][j] == step_num-1:
      i, j = i-1, j
      the_path.append((i, j))
      step_num-=1
    elif j > 0 and step_maze[i][j - 1] == step_num-1:
      i, j = i, j-1
      the_path.append((i, j))
      step_num-=1
    elif i < len(step_maze) - 1 and step_maze[i + 1][j] == step_num-1:
      i, j = i+1, j
      the_path.append((i, j))
      step_num-=1
    elif j < len(step_maze[i]) - 1 and step_maze[i][j + 1] == step_num-1:
      i, j = i, j+1
      the_path.append((i, j))
      step_num -= 1
    if not timing:
      vs.draw_matrix(maze,step_maze,gif_list,start,ending, the_path)

  if not timing:
    for i in range(10):
      if i % 2 == 0:
          vs.draw_matrix(maze,step_maze,gif_list,start,ending, the_path)
      else:
          vs.draw_matrix(maze,step_maze,gif_list,start,ending)
      
  return (step_maze,the_path)


def main(maze, start, ending, timing):
    gif_list=[]
    step_maze, the_path = bfs_process(maze,start,ending,timing,gif_list)
    
    if not timing:
      print(step_maze)
      print(the_path)
      gif_list[0].save('bfs_images/bfs_maze.gif',
               save_all=True, append_images=gif_list[1:],
               optimize=False, duration=1, loop=0)

