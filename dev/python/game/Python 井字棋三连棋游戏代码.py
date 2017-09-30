
import random

def drawBroad(broad):
    print('-----------')
    print(' '+broad[7]+' | '+broad[8]+' | '+broad[9])
    print('-----------')
    print(' '+broad[4]+' | '+broad[5]+' | '+broad[6])
    print('-----------')
    print(' '+broad[1]+' | '+broad[2]+' | '+broad[3])
    print('-----------')

def chooseLetter():
    print('before the game ,please choose the letter "X" or "O"("X will be first"): ')
    letter = input().strip().upper()[0]
    print("you choose :"+letter)
    if (letter == 'X'):
        return 'X'
    elif (letter == 'O'):
        return 'O'
    else:
        chooseLetter()

#if has win return letter
#else return N
def checkWin(broad,letter):
    if ((broad[1] ==letter and broad[2] ==letter and broad[3] ==letter )
    or (broad[4] ==letter and broad[5] ==letter and broad[6] ==letter )
    or (broad[7] ==letter and broad[8] ==letter and broad[9] ==letter )
    
    or (broad[1] ==letter and broad[4] ==letter and broad[7] ==letter )
    or (broad[2] ==letter and broad[5] ==letter and broad[8] ==letter )
    or (broad[3] ==letter and broad[6] ==letter and broad[9] ==letter )
    
    or (broad[7] ==letter and broad[5] ==letter and broad[3] ==letter )
    or (broad[1] ==letter and broad[5] ==letter and broad[9] ==letter )
    ):
        return letter
    else:
        return 'N'

#www.iplaypy.com
def hasLetter(broad,location):
    return broad[location] != ' '

# return freeList
def FreeList(broad):
    freeList=[]
    for i in range(1,10):
        if(not hasLetter(broad,i)):
            freeList.append(i)
    return freeList

def PlayerMove (broad,letter):
    if(FreeList(broad) == []):
        print("tie !!!")
        return 'T'
    playlocation = int(input("your turn:").strip()[0])
    print("***in PlayerMove() ***")
    #if (playlocation  in list(range(1,10))and not hasLetter(broad,playlocation)):
    if(playlocation in FreeList(broad)):
        broad[playlocation] = letter
        drawBroad(broad)
        if(checkWin(broad,letter)!= 'N'):
            print("you win")
            return letter
    else:
        PlayerMove(broad,letter)
    
def NextPlay(letter):
    if(letter == 'X'):
        return 'O'
    else:
        return 'X'

def ComputerMove(broad, computerLetter):
    #1,try to Computer win
    #2,try to break player win
    #3,random location
    if(FreeList(broad) == []):
        print("tie !!!")
        return 'T'
    print("***in ComputerMove() ***")
    if(WillWin(broad,computerLetter)!=0):
        broad[WillWin(broad,computerLetter)]=computerLetter
        print("computer win")
        return computerLetter
    elif(WillWin(broad,NextPlay(computerLetter)!=0)):
        broad[WillWin(broad,NextPlay(computerLetter))]=computerLetter
    else:
        broad[random.choice(FreeList(broad))]=computerLetter
    drawBroad(broad)

# copy board
def BoardTemp(board):
    boardTemp = {}
    for i in range(1,10):
        boardTemp[i] = board[i]
    return boardTemp

# if will win return location
# else return 
def WillWin(board, Letter):
    boardTemp=BoardTemp(board)
    for i in FreeList(board):
        boardTemp[i]=Letter
        if(checkWin(boardTemp,Letter) != 'N'):
            #drawBroad(boardTemp)
            return i
        else:
            boardTemp[i]=" "
    return 0

def GameInit():
    broad = {}
    for i in range(1,10):
        broad[i]=' '
    drawBroad(broad)
    return broad 

def GameBody(board,letter):
    templetter=letter
    rs = ''
    while(True):
        rs = ComputerMove(board, templetter)
        if(rs is not None):
            break
        templetter = NextPlay(templetter)
        rs = PlayerMove(board,templetter)
        if(rs is not None):
            break
        templetter = NextPlay(templetter)
    return rs
    
def GameStart():
    broad = GameInit()
    playerletter = chooseLetter()
    
    if(playerletter == 'X'):
        PlayerMove(broad,playerletter)       
    rs = GameBody(broad,NextPlay(playerletter))
    print("rs:"+rs)
    print(FreeList(broad))
    
GameStart()
