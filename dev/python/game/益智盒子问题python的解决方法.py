
import sys  
import random  

def strategy(boxes, p):  
    ''''' return True if strategy success '''  
    return False  

def simulate(n, strategy, times):  
    ''''' n: number of boxes or prisoners
        strategy: strategy used 
        times: random simulation times 
        return numbers of succeeded prisoners as list 
        www.iplaypy.com
    '''  
    boxes = range(n)  
    result = []  

    for i in xrange(times):  
        random.shuffle(boxes)  
        success = 0  
        for p in xrange(n):  
            if strategy(boxes, p):  
                success += 1  
        result.append(success)  

    return result  

def standard_strategy(boxes,p):
    times_remain = len(boxes)/2
    current = p

    while times_remain > 0:
        times_remain -=1
        if boxes[current] ==p:
            return True
        else:
            current = boxes[current]

    return False

n = 100
result = simulate(n,standard_strategy,100)

print result

import matplotlib.pyplot as plt

dist = [result.count(i) for i in range(n+2)]

plt.bar(range(n+2),dist)

plt.show()
