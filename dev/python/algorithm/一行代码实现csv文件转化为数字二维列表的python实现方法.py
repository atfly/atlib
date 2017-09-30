
Python 3.1.3
>>> L=[[float (x) for x in y.split(',')] for y in open('data4.csv').read().rstrip().split('\n')[1:]]
>>> print(L)
>>> 
[[550.0, 50.0], [473.0, 50.0], [428.0, 50.0], [446.0, 36.0], [479.0, 14.0], [418.0, 29.0], [469.0, 24.0], [528.0, 30.0], [465.0, 23.0]]
#www.iplaypy.com