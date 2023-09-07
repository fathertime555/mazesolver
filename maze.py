import cell
import time
import random
import disjoint

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
        self.adjacency = {}
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

        edges = []     
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                if j > 0 and (self.cells[i][j-1], self.cells[i][j]) not in edges:
                    edges.append((self.cells[i][j], self.cells[i][j-1]))
                if i > 0 and (self.cells[i-1][j], self.cells[i][j]) not in edges:
                    edges.append((self.cells[i][j], self.cells[i-1][j]))
                if i < self.num_cols-1 and (self.cells[i+1][j], self.cells[i][j]) not in edges:
                    edges.append((self.cells[i][j], self.cells[i+1][j]))
                if j < self.num_rows-1 and (self.cells[i][j+1], self.cells[i][j]) not in edges:
                    edges.append((self.cells[i][j], self.cells[i][j+1]))                                                                                                                                                                                                                                                                                                                                                                                                                                              

        for i in self.cells:
            for j in i:
                j.draw()
                self.animate()
        
        random.shuffle(edges)
        self.break_walls_r(edges)
        self.break_entrance_and_exit()
        self.reset_cells_visited()
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                adjacent = []
                if j > 0 and not self.cells[i][j].has_top:
                    adjacent.append(self.cells[i][j-1])
                if i > 0 and not self.cells[i][j].has_left:
                    adjacent.append(self.cells[i-1][j])
                if i < self.num_cols-1 and not self.cells[i][j].has_right:
                    adjacent.append(self.cells[i+1][j])
                if j < self.num_rows-1 and not self.cells[i][j].has_bottom:    
                    adjacent.append(self.cells[i][j+1])
                self.adjacency[self.cells[i][j]] = adjacent
        self.solve(self.cells[0][0])
    
    def break_entrance_and_exit(self):
        entrance = self.cells[0][0]
        entrance.has_left = False
        entrance.draw()
        self.animate()
        mazeexit = self.cells[self.num_cols-1][self.num_rows-1]
        mazeexit.has_right = False
        mazeexit.draw()
        self.animate()
    
    def break_walls_r(self, edges):
        mazecells = []
        for i in self.cells:
            for j in i:
                mazecells.append(j)
        disjoint_set = disjoint.DisjointSet(mazecells)
        for edge in edges:
            a, b = edge
            if  disjoint_set.find(a) != disjoint_set.find(b):
                if a.x1 > b.x1:
                    a.has_left = False
                    b.has_right = False
                if a.x1 < b.x1:
                    a.has_right = False
                    b.has_left = False
                if a.y1 > b.y1:
                    a.has_top = False
                    b.has_bottom = False
                if a.y1 < b.y1:
                    a.has_bottom = False
                    b.has_top = False
                for i in self.cells:
                    for j in i:
                        if j.parent == a.parent:
                            j.parent = b.parent
                disjoint_set.union(a, b)
                a.draw()
                b.draw()
                self.animate()

    def animate(self):
        self.window.redraw()
        time.sleep(.01)

    
    def reset_cells_visited(self):
        for i in self.cells:
            for j in i:
                j.visited = False
        
    def solve(self, node):
        node.visited = True
        if node == self.cells[self.num_cols - 1][self.num_rows - 1]:
            return True
        for i in self.adjacency[node]:
            if not i.visited:
                node.draw_move(i)
                self.animate()
                result = self.solve(i)
                if result:
                    return True
            


        
   