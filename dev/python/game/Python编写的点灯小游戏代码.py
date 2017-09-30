
def InitTable(size, value):
    return [[value for i in range(size)] for j in range(size)]

class LightBoard:
    def __init__(self, size, status=""):
        self.clickBoard = InitTable(size, -1)
        self.lightBoard = InitTable(size, 0)
        self.toCheck = []

        for i in range(size):
            for j in range(size):
                self.PushToCheck((i,j))

        for pos, value in enumerate(status):
            if value == "1":
                self.lightBoard[pos/size][pos%size] = 1

        self.size = size

    def PopToCheck(self):
        if len(self.toCheck) > 0:
            pos = self.toCheck[-1]
            del self.toCheck[-1]

        else:
            pos = None
        return pos

    def PushToCheck(self, pos):
        self.toCheck.append(pos)

    def ConnectedLight(self, pos):
        x, y = pos
        yield pos
        if x - 1 >= 0: yield x-1,y
        if x + 1 <self.size: yield x+1,y
        if y -1 >= 0: yield x, y-1
        if y+1 < self.size: yield x, y+1

    def NotCheckLight(self, pos):
        return [(x,y) for x, y in self.ConnectedLight(pos) if self.clickBoard[x][y] == -1]

    def SetCheck(self, pos, value):
        x, y = pos
        self.clickBoard[x][y] = value

        for x, y in self.ConnectedLight(pos):
            self.lightBoard[x][y] = 1 - self.lightBoard[x][y]

    def Pass(self, pos):
        x, y = pos
        self.clickBoard[x][y] = 0

    def CancelPass(self, pos):
        x, y = pos
        self.clickBoard[x][y] = -1

    def CheckError(self, pos):
        for p in self.ConnectedLight(pos):
            x, y = p

            if self.lightBoard[x][y] == 0 and len(self.NotCheckLight(p)) == 0:
                return True
        return False

def Solve(board):
    clickpos = board.PopToCheck()

    if clickpos == None:
        return board.clickBoard
    pos = board.NotCheckLight(clickpos)[0]
    board.SetCheck(pos, 1)

    if not board.CheckError( pos ):
        r = Solve(board)
        if r: return r
    board.SetCheck(pos, -1)
    board.Pass(pos)

    if not board.CheckError( pos ):
        r = Solve(board)
        if r: return r
    board.CancelPass(pos)
    board.PushToCheck(clickpos)

    return False

from Tkinter import *

class LightButton(Button):
    def __init__(self, parent, pos, board):
        Button.__init__(self, parent, width=2)
        self.board = board
        self.status = 0
        self.x, self.y = pos
        self.SetColor()
        self.bind("<Button-1>",self.onClick)
        self.bind("<Button-3>",self.onRightClick)

    def SetColor(self):
        if self.status == 0:
            self.config(bg="#cccccc")

        if self.status == 1:
            self.config(bg="#ffcccc")

    def onClick(self,event):
        toclick = [(0, 0), (-1,0), (1,0), (0, 1), (0, -1)]
        self.config(text="")
        for x,y in toclick:
            try:
                b = self.board[(self.x-x, self.y-y)]
                b.status = 1 - b.status
                b.SetColor()
            except:
                pass

    def onRightClick(self, event):
        self.status = 1 - self.status
        self.SetColor()

if __name__ == "__main__":
    from tkSimpleDialog import askinteger

    def SolveIt():
        boardStatus = ["0"] * Size * Size

        for pos, light in buttons.items():
            if light.status == 1:
                boardStatus[pos[1]*Size+pos[0]] = "1"
        clickBoard = Solve(LightBoard(Size, "".join(boardStatus)))

        for x, r in enumerate(clickBoard):
            for y, c in enumerate(r):
                if c == 1:
                    buttons[(y,x)].config(text="*")
#www.iplaypy.com

    def Clear():
        for button in buttons.values():
            button.status = 0
            button.SetColor()
    root = Tk()
    root.title("Light Solver")
    f = Frame(root)
    f.pack(side = TOP)
    Button(f, text="Solve", command=SolveIt).pack(side=LEFT)
    Button(f, text="Clear", command=Clear).pack(side=LEFT)
    buttons = {}
    Size = askinteger("Light Solver", "Please Input Board Size", initialvalue=5)
    for y in range(Size):
        f = Frame(root)
        f.pack(side = LEFT)
        for x in range(Size):
            pos = x, y
            b = LightButton(f, pos, buttons)
            b.pack()
            buttons[pos] = b
    mainloop()

