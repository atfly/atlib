
#! /usr/bin/env python
# -*- coding: utf-8 -*-

#-----------www.iplaypy.com----------------------------
#  Definitions
#    B(4): Box, 2x2
#    V(2): Vertical Bar, 1x2
#    H(3): Horizontal Bar, 2x1
#    D(1): Dot, 1x1
#    E(0): the empty 1x1(or space)
#    U(7): undefined, or (?)
Empty,Dot,Vbar,Hbar,Box,Undef = 0,1,2,3,4,7
row, col = 5, 4

#---------------------------------------------------------------
#  Generates all the valid end matrix
#
C72 = ((0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
       (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
       (2, 3), (2, 4), (2, 5), (2, 6),
       (3, 4), (3, 5), (3, 6),
       (4, 5), (4, 6),
       (5, 6))

#Possible endings(mirror ending is not included)
#  Ending 1: ????    Ending 2: ????
#            ????              ????
#            ????              ?EE?
#            EBB?              ?BB?
#            EBB?              ?BB?

endings = ([7,7,7,7,  7,7,7,7,  7,7,7,7,  0,4,4,7,  0,4,4,7],
           [7,7,7,7,  7,7,7,7,  7,0,0,7,  7,4,4,7,  7,4,4,7])

def print_matrix(m):
    for i in range(5):
        for j in range(4):
            print m[4*i + j],
        print
    print


def all_ending_layouts():
    """Check all possible configurations when CaoCao is at the exit."""
    values = {}

    for end in endings:
        #14 undefined cells, red & black, select 4, 2 red & 2 black
        slot = [i for i in range(20) if Undef == end[i]]
        red = [slot[i] for i in range(14) if (slot[i] % col + slot[i] / col) % 2 == 0]
        black = [slot[i] for i in range(14) if (slot[i] % col + slot[i] / col) % 2]
        # 21 = C(7,2)
        for c1 in C72: 
            for c2 in C72:
                matrix = end[:]
                matrix[red[c1[0]]] = Dot
                matrix[red[c1[1]]] = Dot
                matrix[black[c2[0]]] = Dot
                matrix[black[c2[1]]] = Dot
                for layout in tile(matrix):
                    value = 0L
                    for t in layout:
                        value = value << 3 | t
                    if not values.has_key(value):
                        rvalue = 0L
                        for i in range(5):
                            for j in range(4):
                                rvalue = rvalue << 3 | layout[i*4 + 4-j-1]
                        values[value] = True
                        values[rvalue] = True
                        yield layout

def is_neighbor(slot, i, j):
    xi, yi = slot[i] % col, slot[i] / col
    xj, yj = slot[j] % col, slot[j] / col
    if xj==xi and yj==yi+1:
        return 2
    if xj==xi+1 and yj==yi:
        return 3
    return 0

def tile(matrix):
    """return the valid layout to tile five 1x2/2x1 in 10 slots"""
    matrix_list = [matrix]
    index = 0

    while index < len(matrix_list):
        matrix = matrix_list[index]
        slot = [i for i in range(20) if Undef == matrix[i]]
        n = len(slot)
        if n == 0:
            return matrix_list[index:]

        #for each undefined block, look up its adjacent undefined block's
        p = [[] for i in range(n)]
        min_p, k = n, -1

        for i in range(n):
            for j in range(i+1, n):
                ret = is_neighbor(slot, i, j)
                if ret:
                    p[i].append((j, ret))
                    p[j].append((i, ret))
            if not p[i]:
                k = -1
                break #an isolated block is detected
            if len(p[i]) < min_p:
                min_p, k = len(p[i]), i
        if k != -1:
            #start with the position with the least adjacent undefined slots, enumerate all
            # possible configurations after filling this position

            for neighbor in p[k]:
                new_matrix = matrix[:]
                new_matrix[slot[k]] = neighbor[1]
                new_matrix[slot[neighbor[0]]] = neighbor[1]
                matrix_list.append(new_matrix)
        #process next matrix
        index += 1
    return []

#---------------------------------------------------------------
# spawn all the layouts to be solved

#convert 4*5 DHVB into block layouts(totally 10 blocks)
def convert(matrix):
    b = [0, 0, 0, 0]
    c,d = 0,0
    result = []

    for i in range(20):
        x = i % 4
        y = i / 4
        n = matrix[i]
        if n == Dot:
            result += [1, x, y]

        elif n == Vbar:
            if y == 0 or b[x] == 0:
                b[x] = 2
                result += [2, x, y]
            else:
                b[x] = 0
        elif n == Hbar:
            if c == 0:
                result += [3, x, y]
                c = 3
            else:
                c = 0
        elif n == Box:
            if d % 4 == 0:
                result += [4, x, y]
                d = 1
            else:
                d += 1
    return result

from copy import deepcopy

class Board:
    def __init__(self, layout):
        #the moved index to generate this board
        self.moved = -1
        #init the matrix and items
        self.items = [()] * 10 #BIT:type:3,x:2,y:3), x,y is zero-based
        self.empty = [(0,0), (0,0)] #2 empty slot's position in matrix, (col, row)

        #-1 mean's boundary
        f = -1
        #[1+5+1][1+4+1] of byte, each byte is the (index+1) in items
        #  the extra 1s is for the boundary
        self.matrix = [ [f, f, f, f, f, f],
                        [f, 0, 0, 0, 0, f],
                        [f, 0, 0, 0, 0, f],
                        [f, 0, 0, 0, 0, f],
                        [f, 0, 0, 0, 0, f],
                        [f, 0, 0, 0, 0, f],
                        [f, f, f, f, f, f] ]

        #calculate the items into cell-matrix
        type, x, y = 0, 0, 0
        for i in range(10):
            type = layout[i*3]
            x = layout[i*3+1]
            y = layout[i*3+2]
            self.items[i] = (type, x, y)
            self.matrix[y+1][x+1] = i+1
            if type == Vbar:
                self.matrix[y+2][x+1] = i+1
            elif type == Hbar:
                self.matrix[y+1][x+2] = i+1
            elif type == Box:
                self.matrix[y+1][x+2] = i+1
                self.matrix[y+2][x+1] = i+1
                self.matrix[y+2][x+2] = i+1
        #find out the empty blocks
        count = 0
        for i in range(7):
            for j in range(6):
                if not self.matrix[i][j]:
                    self.empty[count] = (j, i)
                    if not count: count += 1
                    else: return

    def getValue(self):
        val, bt = 0L, 0
        for i in range(1, 6):
            for k in range(1, 5):
                index = self.matrix[i][k] - 1
                if index < 0: bt = 0
                else: bt = self.items[index][0]
                val = val << 3 | bt
        return val

    def getRValue(self):
        val, bt = 0L, 0
        for i in range(1, 6):
            for k in range(4, 0, -1):
                index = self.matrix[i][k] - 1
                if index < 0: bt = 0
                else: bt = self.items[index][0]
                val = val << 3 | bt
        return val

    #spawn new Board by moving the cells around empty cells
    #  changes global variable: g_values
    def spawn(self):
        global g_values
        new_boards = []
        #collect the cells around empty cells
        around = [0] * 8
        #DO NOT change the order of ulrd, it's been depended
        #       ulrd: Up/Left/Right/Down
        ulrd = ((0,-1), (-1,0), (1,0), (0,1))
        for e in self.empty: #two empty blocks, always 2
            x, y = e
            for k in range(4):
                dir = ulrd[k]
                nx = x + dir[0]
                ny = y + dir[1]
1c40

                index = self.matrix[ny][nx] - 1
                if index >= 0:
                    newb = deepcopy(self)
                    newb.moved = index
                    if newb.tryAndMove(index, -dir[0], -dir[1]):
                        value = newb.getValue()
                        if not g_values.has_key(value):
                            if len(g_values) % 1000 == 0:
                                print len(g_values)
                            rvalue = newb.getRValue()
                            g_values[value] = rvalue
                            g_values[rvalue] = value
                            new_boards.append(newb)
        return new_boards

    def tryAndMove(self, index, dx, dy):
        item = self.items[index]
        type, x, y = item
        ret = False
        #ci is short for cell index
        ci1 = ci2 = ci3 = ci4 = 0
        if type == Dot:
            ci1 = self.matrix[y+dy+1][x+dx+1]
            ret = not ci1 or ci1 == index+1
            if ret:
                self.matrix[y+1][x+1] = 0
                self.matrix[y+dy+1][x+dx+1] = index + 1
                self.items[index] = (type, x+dx, y+dy)
                self.setEmpty(x+1, y+1)

        elif type == Vbar:
                ci1 = self.matrix[y+dy+1][x+dx+1]
                ci2 = self.matrix[y+dy+2][x+dx+1]
                ret = (not ci1 or ci1==index+1) and (not ci2 or ci2==index+1)
                if ret:
                    self.matrix[y+1][x+1] = 0
                    self.matrix[y+2][x+1] = 0
                    self.matrix[y+dy+1][x+dx+1] = index + 1
                    self.matrix[y+dy+2][x+dx+1] = index + 1
                    self.items[index] = (type, x+dx, y+dy)
                    if self.matrix[y+1][x+1] == 0: self.setEmpty(x+1, y+1)
                    if self.matrix[y+2][x+1] == 0: self.setEmpty(x+1, y+2)

        elif type == Hbar:
                ci1 = self.matrix[y+dy+1][x+dx+1]
                ci2 = self.matrix[y+dy+1][x+dx+2]
                ret = (not ci1 or ci1==index+1) and (not ci2 or ci2==index+1)
                if ret:
                    self.matrix[y+1][x+1] = 0
                    self.matrix[y+1][x+2] = 0
                    self.matrix[y+dy+1][x+dx+1] = index + 1
                    self.matrix[y+dy+1][x+dx+2] = index + 1
                    self.items[index] = (type, x+dx, y+dy)
                    if self.matrix[y+1][x+1] == 0: self.setEmpty(x+1, y+1)
                    if self.matrix[y+1][x+2] == 0: self.setEmpty(x+2, y+1)

        elif type == Box:
                ci1 = self.matrix[y+dy+1][x+dx+1]
                ci2 = self.matrix[y+dy+1][x+dx+2]
                ci3 = self.matrix[y+dy+2][x+dx+1]
                ci4 = self.matrix[y+dy+2][x+dx+2]
                ret = (not ci1 or ci1==index+1) and (not ci2 or ci2==index+1) and \
                      (not ci3 or ci3==index+1) and (not ci4 or ci4==index+1)
                if ret:
                    self.matrix[y+1][x+1] = 0
                    self.matrix[y+1][x+2] = 0
                    self.matrix[y+2][x+1] = 0
                    self.matrix[y+2][x+2] = 0
                    self.matrix[y+dy+1][x+dx+1] = index+1
                    self.matrix[y+dy+1][x+dx+2] = index+1
                    self.matrix[y+dy+2][x+dx+1] = index+1
                    self.matrix[y+dy+2][x+dx+2] = index+1
                    self.items[index] = (type, x+dx, y+dy)
                    if self.matrix[y+1][x+1] == 0: self.setEmpty(x+1, y+1)
                    if self.matrix[y+1][x+2] == 0: self.setEmpty(x+2, y+1)
                    if self.matrix[y+2][x+1] == 0: self.setEmpty(x+1, y+2)
                    if self.matrix[y+2][x+2] == 0: self.setEmpty(x+2, y+2)
        return ret

    def setEmpty(self, ex, ey):
        x, y = self.empty[0]
        if (self.matrix[y][x]):
            self.empty[0] = (ex, ey)
        else:
            self.empty[1] = (ex, ey)

#-----------------------------------------

#global variables
#all end matrix
#all non-end matrix
#values for all end and non-end matrix
g_values = {}

#print ending count
end_count = 0
for matrix in all_ending_layouts():
    end_count += 1
    #check if this board has been touched
    value = 0L
    for t in matrix:
        value = value << 3 | t
    if g_values.has_key(value):
        continue
    rvalue = 0L
    for i in range(5):
        for j in range(4):
            rvalue = rvalue << 3 | matrix[i*4 + 4-j-1]
    layout = convert(matrix)
    g_values[value] = rvalue
    g_values[rvalue] = value
    #start spawn
    board = Board(layout)
    board_pool = [board]
    index = 0
    while index < len(board_pool):
        board_pool += board_pool[index].spawn()
        index += 1
    print len(g_values)

print "Total Endings count:", end_count
print "Total Layouts count:", len(g_values)

def solve_all_layouts():
    g_nondups = {}
    count = 0
    from os import popen
    outfile = open("input.log", "w+")
    for value in g_values:
        if count % 1000 == 0:
            print count
        if g_nondups.has_key(value):
            continue
        count += 1
        rvalue = g_values[value]
        g_nondups[value] = True
        g_nondups[rvalue] = True
        matrix = [0] * 20
        val = value
        for i in range(20):
            matrix[20-i-1] = val & 7
            val = val >> 3
        layout = convert(matrix)
        layout_str = "".join([str(i) for i in layout])
        print >>outfile, layout_str, value, rvalue, layout
    return count

count = solve_all_layouts()
print "Total Layouts count(no mirror):", count
print "Everything is over, see result.log for detailed result"

