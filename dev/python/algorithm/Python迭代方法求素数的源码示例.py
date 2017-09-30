
for x in range(1,20,2):
    fg=0
    for y in range(2,x/2+1):
        if  (x%y==0):
            fg=1
    if (fg==0):print x

#www.iplaypy.com
L1 = [x for x in range ( 1 , 100 ) if not [y for y in range ( 2 ,x/2+1)   if x % y == 0 ]]
print L1