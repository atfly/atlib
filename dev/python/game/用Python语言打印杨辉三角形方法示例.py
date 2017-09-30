

# -*- coding: utf-8 -*-

if __name__ == '__main__':

    a = []

    # 10 层次
    k = 10

    for i in range(k):
        a.append([])
        for j in range(k):
            a[i].append(0)

    for i in range(k):
        a[i][0] = 1
        a[i][i] = 1

    for i in range(2,k):
        for j in range(1,i):
            a[i][j] = a[i - 1][j-1] + a[i - 1][j]

    from sys import stdout
  
    for i in range(k):
        for j in range(i + 1):
            stdout.write(a[i][j])
            stdout.write(' ')
        print

