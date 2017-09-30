
from numpy import *
from math import *

a=(['x','y','z'])
sum_com=0

for i in range(3):
    y=input("Enter %s component:"%a[i])
    m=y**2
    sum_com += m

magnitude=sqrt(sum_com)
#www.iplaypy.com

print "The magnitude of vector is %s"%magnitude
