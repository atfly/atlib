
all(map(lambda x: -1<x<256,map(int,ipstr.split('.'))))

#ipv4有效，如果担心int方法异常，可以使用safeInt:

def safeInt(s):
    a = 256:
    try:
        a = int(s)
    except:
        pass #do nothing :)
    return a

#www.iplaypy.com
#对于ipv6 我觉得这种方法应该也是可行的 因为ipv4地址本身就是一个32位整数 ipv6不太了解 :(