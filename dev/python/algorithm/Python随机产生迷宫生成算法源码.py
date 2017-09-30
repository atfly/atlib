
import sys
from random import randrange, shuffle
from Tkinter import *
from tkSimpleDialog import askstring
 
sys.setrecursionlimit(100000)
 
BOTTOM_WALL = 0
RIGHT_WALL = 1
VISITED = 2
E,S,W,N = 0, 1, 2, 3
DIRECTION = [(0,1),(1,0),(0,-1),(-1,0)]
 
class Maze:
    def __init__(self, row, col):
        self.row , self.col = row, col
        self.maze = [[[True, True, False] for c in range(col)] for r in range(row)]
        self.makepath(randrange(row), randrange(col))
 
    def makepath(self, r, c, direct = None):

        maze = self.maze

        maze[r][c][VISITED] = True

        if direct == N: maze[r][c][BOTTOM_WALL] = False
        if direct == S: maze[r-1][c][BOTTOM_WALL] = False
        if direct == W: maze[r][c][RIGHT_WALL] = False
        if direct == E: maze[r][c-1][RIGHT_WALL] = False
 
        directs = []
        if r > 0: directs.append(N)
        if r < self.row - 1: directs.append(S)
        if c > 0: directs.append(W)
        if c < self.col - 1: directs.append(E)
 
        shuffle(directs)
 
        for d in directs:

            dr, dc = DIRECTION[d]

            if not maze[r+dr][c+dc][VISITED]:
                self.makepath(r+dr, c+dc, d)
 
    def draw(self, size, canvas):
        d = 5

        canvas.config(width = d*2+self.col*size, height = d*2+self.row*size)
        line = canvas.create_line
        line(d,d,self.col*size+d,d)
        line(d,d,d,self.row*size+d)
        #www.iplaypy.com

        for r in range(self.row):
            for c in range(self.col):

                if self.maze[r][c][BOTTOM_WALL]:
                    line(c*size+d, r*size+size+d, c*size+size+d, r*size+size+d)

                if self.maze[r][c][RIGHT_WALL]:
                    line(c*size+size+d, r*size+d, c*size+size+d, r*size+size+d)
 
root = Tk()
root.title("Maze")
canvas = Canvas(root)
canvas.pack()
size = askstring("Maze size", "Please Maze size", initialvalue="25 25")
size = [int(x) for x in size.split()]
Maze(*size).draw(10, canvas)
root.mainloop()
