import tkinter as tk

class Window:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, mazeheight, mazewidth):
        self.__root = tk.Tk()
        self.__root.title("Maze")
        self.maze = tk.Canvas(self.__root, width=mazewidth, height=mazeheight, background="white")
        self.maze.pack()
        self.mazerunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks() 
        self.__root.update()
    
    def wait_for_close(self):
        self.mazerunning = True
        while(self.mazerunning == True):
            self.redraw()
    
    def close(self):
        self.mazerunning = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.maze, fill_color)






