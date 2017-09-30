
import random
import time
import logging

def isSorted(ml):
    for i in range(len(ml) - 1):
        if ml[i] > ml[i + 1]:
            return False
    return True
    
def swap(ml, m, n):
    t = ml[m]
    ml[m] = ml[n]
    ml[n] = t
    
def bubbleSort(ml):
    for m in range(len(ml) - 1):
        for n in range(len(ml) - m - 1):
            if ml[n] > ml[n + 1]:
                swap(ml, n, n + 1)
                
def selectSort(ml):
    for m in range(len(ml) - 1):
        minIndex = m
        for n in range(m + 1, len(ml)):
            if ml[n] < ml[minIndex]:
                minIndex = n
        if minIndex != m:
            swap(ml, minIndex, m)


def quickSort(ml, left = None, right = None):
    def partition(ml, left, right):
        counter = left
        for m in range(left, right):
            if ml[m] < ml[right]:
                swap(ml, counter, m)
                counter += 1
        swap(ml, counter, right)
        return counter
        
    if left == None or right == None:
        quickSort(ml, 0, len(ml) - 1)
    elif left < right:
        p = partition(ml, left, right)
        quickSort(ml, left, p - 1)
        quickSort(ml, p + 1, right)

#www.iplaypy.com
def insertSort(ml):
    for n in range(1, len(ml)):
        temp = ml[n]
        index = n
        while index > 0 and ml[index - 1] > temp:
            ml[index] = ml[index - 1]
            index -= 1
        ml[index] = temp

def ciuraShellSort(ml):
    '''It says this is fast, 
    but it seems it's not as fast as it's supposed to be'''
    op, n = 0, len(ml)
    incs = [2331004, 1036002, 460445, 204643, 90952, 40423, 17965, 7985, 
            3549, 1577, 701, 301, 132, 57, 23, 9, 4, 1]
    for t in range(18):
        h = incs[t]
        if h > n * 4 / 9:
            continue
        for i in range(h, n):
            temp = ml[i]
            j = i - h
            while j >= 0 and ml[j] > temp:
                ml[j + h] = ml[j]
                op += 1
                j -= h
            ml[j + h] = temp
            op += 1

def shellSort(seq):
    '''This shell sort use the nature of python'''
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = round(inc / 2.2)

def shell(data):
    '''This is tranlsated from java version from wiki, 
    not using python feature, it's a little bit slower than previous one'''
    inc = len(data) // 2
    while inc:
        for i in range(inc, len(data)):
            tmp = data[i]
            j = i
            while j >= inc and data[j - inc] > tmp:
                data[j] = data[j - inc]
                j -= inc
            data[j] = tmp
        inc = round(inc / 2.2)
        
def mergesort(n):
        """Recursively merge sort a list. Returns the sorted list."""
        def merge(front, back):
                """Merge two sorted lists together. Returns the merged list."""
                result = []
                while front and back:
                    # pick the smaller one from the front and stick it on
                    # note that list.pop(0) is a linear operation, so this gives quadratic running time...
                    result.append(front.pop(0) if front[0]<=back[0] else back.pop(0))
                # add the remaining end
                result.extend(front or back)
                return result
 
        mid = len(n) // 2
        front = n[:mid]
        back = n[mid:]
        
        if len(front) > 1:
            front = mergesort(front)
        if len(back) > 1:
            back = mergesort(back)

def HeapSort(A):
    def heapify(A):
        start = (len(A) - 2) // 2
        while start >= 0:
            siftDown(A, start, len(A) - 1)
            start -= 1

2000


    def siftDown(A, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and A[child] < A[child + 1]:
                child += 1
            if child <= end and A[root] < A[child]:
                A[root], A[child] = A[child], A[root]
                root = child
            else:
                return

    heapify(A)
    end = len(A) - 1
    while end > 0:
        A[end], A[0] = A[0], A[end]
        siftDown(A, 0, end - 1)
        end -= 1

if __name__ == '__main__':
    mt = [random.randint(1, 100) for i in range(9999)]
    #print(' '.join(map(str, mt)))
    print(isSorted(mt))

    def out(visit):
        if visit != None:
            print(visit.__name__ + ':')
            l = mt[:]
            t1 = time.time()
            visit(l)
            t2 = time.time()
            #print(' '.join(map(str, l)))
            print(isSorted(l))
            print((t2 - t1) * 1000.0)
            
    out(insertSort)
    out(bubbleSort)
    out(selectSort)
    out(quickSort)
    out(ciuraShellSort)
    out(shellSort)
    out(shell)
    out(mergesort)
    out(HeapSort)
