import cell
import time
import random
from collections import deque

class Maze:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window = None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.cells = []
        if seed != None:
            random.seed(seed)
        else:
            random.seed(0)
    
    def create_cells(self):
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                column.append(cell.Cell((self.x1 + (i * self.cell_size_x)), (self.y1 + (j * self.cell_size_y)), (self.x1 + self.cell_size_x + (i * self.cell_size_x)), 
                (self.y1 + self.cell_size_y + (j * self.cell_size_y)), self.window))
            self.cells.append(column)
            column.clear
        
        adjacency = {}
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                order = random.randint(0,23)
                adjacent = []
                match order:                    
                    case 0:
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1])
                    case 1:
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1])
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])
                    case 2:
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1])
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])   
                    case 3:
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1])
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])                                             
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])
                    case 4:
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])     
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1])                                        
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])                       
                    case 5:
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])   
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])  
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1])
                    case 6:
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])  
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])   
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1])     
                    case 7:
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])  
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1])
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])   
                    case 8:
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])  
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1])    
                    case 9:
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1])   
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])    
                    case 10:
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1])   
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])  
                    case 11:
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1]) 
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])    
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])    
                    case 12:
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1]) 
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])    
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j]) 
                    case 13:
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1]) 
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])  
                        if j > 0:
                            adjacent.append(self.cells[i][j-1]) 
                    case 14:
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1]) 
                        if j > 0:
                            adjacent.append(self.cells[i][j-1]) 
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])   
                    case 15:
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1]) 
                        if j > 0:
                            adjacent.append(self.cells[i][j-1]) 
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])   
                    case 16:
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1]) 
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])
                        if j > 0:
                            adjacent.append(self.cells[i][j-1]) 
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])  
                    case 17:
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1]) 
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])                            
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])  
                    case 18:    
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])   
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1]) 
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])                            
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])  
                    case 19:
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])   
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1]) 
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])  
                    case 20:
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])   
                        if i > 0:
                            adjacent.append(self.cells[i-1][j]) 
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1]) 
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])     
                    case 21:
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j])   
                        if i > 0:
                            adjacent.append(self.cells[i-1][j]) 
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])  
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1]) 
                    case 22:
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j]) 
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])   
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])  
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1])     
                    case 23:
                        if i < self.num_cols-1:
                            adjacent.append(self.cells[i+1][j]) 
                        if j > 0:
                            adjacent.append(self.cells[i][j-1])   
                        if j < self.num_rows-1:
                            adjacent.append(self.cells[i][j+1]) 
                        if i > 0:
                            adjacent.append(self.cells[i-1][j])                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                adjacency[self.cells[i][j]] = adjacent

        for i in self.cells:
            for j in i:
                j.draw()
                self.animate()
        
        self.break_walls_r(adjacency)
        self.break_entrance_and_exit()
        self.reset_cells_visited()
    
    def break_entrance_and_exit(self):
        entrance = self.cells[0][0]
        entrance.has_left = False
        entrance.draw()
        self.animate()
        mazeexit = self.cells[self.num_cols-1][self.num_rows-1]
        mazeexit.has_right = False
        mazeexit.draw()
        self.animate()
    
    def break_walls_r(self, adjacency):
        self.cells[0][0].visited = True
        queue = deque([self.cells[0][0]])

        while queue:
            current_node = queue.popleft()         
            adjacent = adjacency[current_node]
            for neighbor in adjacent:
                if not neighbor.visited:
                    queue.append(neighbor)
                    neighbor.visited = True 
                    if neighbor.x1 > current_node.x1:
                        neighbor.has_left = False
                        current_node.has_right = False
                    if neighbor.x1 < current_node.x1:
                        neighbor.has_right = False
                        current_node.has_left = False
                    if neighbor.y1 > current_node.y1:
                        neighbor.has_top = False
                        current_node.has_bottom = False
                    if neighbor.y1 < current_node.y1:
                        neighbor.has_bottom = False
                        current_node.has_top = False
                    neighbor.draw()
                    current_node.draw()
                    self.animate()

    def animate(self):
        self.window.redraw()
        time.sleep(.01)
    
    def reset_cells_visited(self):
        for i in self.cells:
            for j in i:
                j.visited = False
        
   