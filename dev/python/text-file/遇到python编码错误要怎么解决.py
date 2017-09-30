
# -*- coding: utf8 -*-
'''中文'''

sll=list(__doc__)
nsl=[]

for i in range(len(sll)/3):
    nsl.append(''.join(sll[3*i:3*i+3]).decode('utf8').encode('unicode-escape')[2:])

print '{0:*^80}'.format('汉字转Unicode编码组合')

print ''.join(nsl)
print

strlist=[]

for i in list(''.join(nsl)):
    s=list(str(bin(int(i, 16)))[2:])

    while len(s)<4:
        s.insert(0, '0') 
    strlist.append(''.join(s))

print '{0:*^80}'.format('二进制编码组合')

print ''.join(strlist)
print

#python解码www.iplaypy.com
str2=''.join(strlist)
strlist2=[]

for i in range(len(str2)/4):
    strlist2.append(str(hex(int(str2[i*4:i*4+4], 2))[2:]))
    
print '{0:*^80}'.format('二进制解码为Unicode编码组合')

print ''.join(strlist2)
print

sl=list(''.join(strlist2))

for i in range(len(sl)/4):
    sl.append('\u')

    for j in range(4):
        sl.append(sl[0])
        sl.remove(sl[0])
        
print '{0:*^80}'.format('Unicode编码解码为汉字')
print ''.join(sl).decode('unicode-escape')