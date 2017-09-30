
import random
a = 10; b = 10; c = 10
fortune = [a,b,c]

def one_round():
    p = int(3*random.random())
    for i in range(3):
        if i==p:
            fortune[i] += 2
        else:
            fortune[i] -= 1

def stop():
    for i in fortune:
        if i==0:
            return True
    return False


def play_game():
    global fortune
    fortune = [a,b,c]; cnt = 0
    while not stop():
        one_round(); cnt += 1
    return cnt

#www.iplaypy.com
def simulate(n):
    cnt = [play_game() for i in range(n)]
    sum = reduce(lambda x,y: x+y, cnt, 0)
    return sum*1.0/n

