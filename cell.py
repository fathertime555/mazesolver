import point
import line

class Cell:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
   
    def __init__(self, x1, y1, x2, y2, window = None, has_left = True, has_right = True, has_top = True, has_bottom = True):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.has_left = has_left
        self.has_right = has_right
        self.has_bottom = has_bottom
        self.has_top = has_top
        self.window = window
        self.visited = False
        self.parent = self
    
    def draw(self): 
        point1 = point.Point(self.x1, self.y1)
        point2 = point.Point(self.x1, self.y2)
        leftwall = line.Line(point1, point2)
        if(self.has_left):
            self.window.draw_line(leftwall, "black")
        else:
            self.window.draw_line(leftwall, "white")

        point1 = point.Point(self.x2, self.y1)
        point2 = point.Point(self.x2, self.y2)
        rightwall = line.Line(point1, point2)
        if(self.has_right):
            self.window.draw_line(rightwall, "black")
        else:
            self.window.draw_line(rightwall, "white")

        point1 = point.Point(self.x1, self.y2)
        point2 = point.Point(self.x2, self.y2)
        bottomwall = line.Line(point1, point2)
        if(self.has_bottom):
            self.window.draw_line(bottomwall, "black")
        else:
            self.window.draw_line(bottomwall, "white")

        point1 = point.Point(self.x1, self.y1)
        point2 = point.Point(self.x2, self.y1)
        topwall = line.Line(point1, point2)
        if(self.has_top):
            self.window.draw_line(topwall, "black")
        else:
            self.window.draw_line(topwall, "white")
    
    def draw_move(self, to_cell, undo = False):
        point1 = point.Point(((self.x2-self.x1)/2) + self.x1, ((self.y2-self.y1)/2) + self.y1)
        point2 = point.Point(((to_cell.x2-to_cell.x1)/2) + to_cell.x1, ((to_cell.y2-to_cell.y1)/2) + to_cell.y1)
        moveline = line.Line(point1, point2)
        if(undo == False):
            self.window.draw_line(moveline, "red")
        else:
            self.window.draw_line(moveline, "grey")