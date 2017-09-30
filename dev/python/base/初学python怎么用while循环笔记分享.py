
L=[]
print 'please input five number'
i=0

while i<5:
    n=int(raw_input('Enter your number:'))
    L.append(n)
    i+=1

print L

print 'Now,you can select them'

print 'summation averages exit'

#www.iplaypy.com

go=True
while go:

    s=raw_input('I will:')

    if s=='summation':
        print sum(L)
    elif s=='averages':
        print sum(L)/len(L)
    elif s=='exit':
        go=False
        print 'Done'
    else:
        
        print 'Not have options'
       
