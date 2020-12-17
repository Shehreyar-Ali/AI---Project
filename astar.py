import heapq
import visualisation as vs



class Cell(object):
    def __init__(self, x, y, reachable):
        """
        Initialize new cell
        
        """
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.cost_walk = 0
        self.heuristic = 0
        self.total = 0

    def __lt__(self, other):
        return self.total < other.total

    
class AStar(object):
    def __init__(self,maze,gif):
        self.cell_list = []
        self.gif_list=gif
        heapq.heapify(self.cell_list)
        self.visited = set()
        self.cells = []
        self.grid=maze
        self.grid_height = len(maze[1])
        self.grid_width = len(maze)
        self.maze_steps=[[0]*self.grid_height for _ in range(self.grid_width)]
        
    def get_cell(self, x, y):
        """
        Returns a cell from the cells list
    
        """
        return self.cells[x * self.grid_height + y]

    def get_adjacent_cells(self, cell):
        """
        Returns adjacent cells to a cell. Clockwise starting
        from the one on the right.

        """
        cells = []
        if cell.x < self.grid_width-1:
            cells.append(self.get_cell(cell.x+1, cell.y))
        if cell.y > 0:
            cells.append(self.get_cell(cell.x, cell.y-1))
        if cell.x > 0:
            cells.append(self.get_cell(cell.x-1, cell.y))
        if cell.y < self.grid_height-1:
            cells.append(self.get_cell(cell.x, cell.y+1))
        return cells

    def create_pathlist(self,my_path):
        cell = self.end
        while cell.parent is not self.start:
            cell = cell.parent
            my_path.append((cell.x,cell.y))
        
        my_path = my_path[::-1]

        my_path.insert(0,(self.start.x,self.start.y))
        my_path.append((self.end.x,self.end.y))
        
        return my_path
    
    def show_maze(self):
        
        print(self.grid)
        pathlist=[]
        pathlist=self.create_pathlist(pathlist)
        
        for i in range(len(pathlist)+1):
            forvis= pathlist[:i]
            vs.draw_matrix(self.grid, self.maze_steps, self.gif_list,(self.start.x,self.start.y),(self.end.x,self.end.y), forvis)
    
        
        print(pathlist)
        print(self.maze_steps)
        
        for i in range(10):
            if i%2 == 0:
                vs.draw_matrix(self.grid, self.maze_steps, self.gif_list,
                (self.start.x,self.start.y),(self.end.x,self.end.y))
            else:
                vs.draw_matrix(self.grid, self.maze_steps, self.gif_list,
                (self.start.x,self.start.y),(self.end.x,self.end.y), forvis)
     
    
    def update_cell(self, adj, cell):
        """
        Update adjacent cell
    
        """
        adj.cost_walk = cell.cost_walk + 10
        adj.heuristic = self.get_heuristic_val(adj)
        adj.parent = cell
        adj.total = adj.heuristic + adj.cost_walk

    def process(self,timing = False):
        # add starting cell to cell_list heap queue
        heapq.heappush(self.cell_list, (self.start.total, self.start))
        
        k = 1

        while len(self.cell_list):
            # pop cell from heap queue
            cell = heapq.heappop(self.cell_list)[1]
            
            # add cell to visited so we don't process it twice
            self.visited.add(cell)
            
            if timing != True:
                self.maze_steps[cell.x][cell.y]=k
                vs.draw_matrix(self.grid, self.maze_steps, self.gif_list,(self.start.x,self.start.y),(self.end.x,self.end.y))
            k+=1
            
            # if ending cell, display found path
            if cell is self.end and timing != True:
                self.show_maze()
                break
            
            # get adjacent cells for cell
            adj_cells = self.get_adjacent_cells(cell)
            
            for adj_cell in adj_cells:
                if adj_cell.reachable and adj_cell not in self.visited:
                    #if (adj_cell.total, adj_cell) in self.cell_list:
                        # if adj cell in cell_list, check if current path is
                        # better than the one previously found for this adj
                        # cell.
                        #if adj_cell.cost_walk > cell.cost_walk + 10:
                        #    self.update_cell(adj_cell, cell)
                    #else:
                    self.update_cell(adj_cell, cell)
                        # add adj cell to cell_list
                    heapq.heappush(self.cell_list, (adj_cell.total, adj_cell))
        
        if self.gif_list==[] and timing == False:
            print("no path")
    
    def init_cells(self,start, end):

        walls = self.init_walls()

        for x in range(self.grid_width):
            for y in range(self.grid_height):
                if (x, y) in walls:
                    reachable = False
                else:
                    reachable = True
                self.cells.append(Cell(x, y, reachable))

        self.start = self.get_cell(start[0],start[1])
        self.end = self.get_cell(end[0],end[1])

    def init_walls(self):
        walls=[]
        
        for i in range(self.grid_width):
	        for j in range(self.grid_height):
		        if self.grid[i][j]==1:
			        walls.append((i,j))
        
        return walls

    def get_heuristic_val(self, cell):
        """
        Compute the heuristic value self.heuristic for a cell: distance between
        this cell and the ending cell multiply by 10.
    
        """
        return 10 * (abs(cell.x - self.end.x) + abs(cell.y - self.end.y))


def main(maze, start, ending, timing):
    gif_list=[]
    ass= AStar(maze,gif_list)
    ass.init_cells(start,ending)
    ass.process(timing)


    if not timing:
        gif_list[0].save('ast_images/ast_maze.gif',
        save_all=True, append_images=gif_list[1:],
        optimize=False, duration=1, loop=0)

