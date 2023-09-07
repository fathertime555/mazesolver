import window
import maze_with_BFS
import maze
import random

win = window.Window(600, 800)
maze1 = maze.Maze(2, 2, 10, 10, 61, 59.5, win, random.random())
maze1.create_cells()
win.wait_for_close()