
from math import cos
#导入模块方法
#www.iplaypy.com

#定义函数，正式代码部分开始
def eigenvalues_of_laplacian(n):
    ew = [2*(2-cos(i*pi/n)-cos(j*pi/n)) for i in range(n) for j in range(n)]

    return ew

def num_of_spanning_trees(n):
    ew = eigenvalues_of_laplacian(n)

    return reduce(lambda x,y:x*y, ew[1:])/n**2

