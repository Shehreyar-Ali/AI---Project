import heapq
import visualisation as vs
from bfs import a
import copy
import mazeCreator as mc
images=[]




#a = mc.maze



start = (0,1)
ending = mc.endPoint()


class Cell(object):
    def __init__(self, x, y, reachable):
        """
        Initialize new cell
        @param x cell x coordinate
        @param y cell y coordinate
        @param reachable is cell reachable? not a wall?
        """
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

    


class AStar(object):
    def __init__(self,maze):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = []
        self.grid=maze
        self.grid_height = len(maze[1])
        self.grid_width = len(maze)
        
    def get_cell(self, x, y):
        """
        Returns a cell from the cells list
    
        @param x cell x coordinate
        @param y cell y coordinate
        @returns cell
        """
        return self.cells[x * self.grid_height + y]

    def get_adjacent_cells(self, cell):
        """
        Returns adjacent cells to a cell. Clockwise starting
        from the one on the right.
    
        @param cell get adjacent cells for this cell
        @returns adjacent cells list
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

    def display_path(self):
        m=[[0]*self.grid_height for _ in range(self.grid_width)]
        #print("here")

        print(self.grid)
        pathlist=[]
        cell = self.end
        while cell.parent is not self.start:
            cell = cell.parent
            pathlist.append((cell.x,cell.y))
        
        m[self.end.x][self.end.y] = len(pathlist)+2
        m[self.start.x][self.start.y] = 1
        w = 2

        for i in reversed(range(len(pathlist))):
            m[pathlist[i][0]][pathlist[i][1]] = w
            w += 1

        pathlist = pathlist[::-1]

        pathlist.insert(0,(self.start.x,self.start.y))
        pathlist.insert(-1,(self.end.x,self.end.y))
        print(pathlist)
        print(m)
        #print(self.grid)
        vs.draw_matrix(self.grid, m, images,(self.start.x,self.start.y),(self.end.x,self.end.y), pathlist)
    
    
    def update_cell(self, adj, cell):
        """
        Update adjacent cell
    
        @param adj adjacent cell to current cell
        @param cell current cell being processed
        """
        adj.g = cell.g + 10
        adj.h = self.get_heuristic(adj)
        adj.parent = cell
        adj.f = adj.h + adj.g

    def process(self,timing = False):
        # add starting cell to open heap queue
        heapq.heappush(self.opened, (self.start.f, self.start))
        while len(self.opened):
            # pop cell from heap queue
            cell = heapq.heappop(self.opened)[1]
            # add cell to closed list so we don't process it twice
            self.closed.add(cell)
            # if ending cell, display found path
            if cell is self.end and timing != True:
                self.display_path()
                
            # get adjacent cells for cell
            adj_cells = self.get_adjacent_cells(cell)
            for adj_cell in adj_cells:
                if adj_cell.reachable and adj_cell not in self.closed:
                    if (adj_cell.f, adj_cell) in self.opened:
                        # if adj cell in open list, check if current path is
                        # better than the one previously found for this adj
                        # cell.
                        if adj_cell.g > cell.g + 10:
                            self.update_cell(adj_cell, cell)
                    else:
                        self.update_cell(adj_cell, cell)
                        # add adj cell to open list
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell))
        if images==[] and timing == False:
            print("no path")
    
    def init_grid(self,start, end):
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

    def get_heuristic(self, cell):
        """
        Compute the heuristic value H for a cell: distance between
        this cell and the ending cell multiply by 10.
    
        @param cell
        @returns heuristic value H
        """
        return 10 * (abs(cell.x - self.end.x) + abs(cell.y - self.end.y))


ass= AStar(a)
ass.init_grid(start,ending)
timing=False
ass.process(timing)


if not timing:
    images[0].save('maze1.jpg')
