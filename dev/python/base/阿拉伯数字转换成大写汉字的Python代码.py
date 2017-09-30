
def IIf( b, s1, s2):
　　if b:
　　　　return s1
　　else:
　　　　return s2
def num2chn(nin=None):
　　　　cs =
('零','壹','贰','叁','肆','伍','陆','柒','捌','玖','◇','分','角','圆','拾','佰','仟',
'万','拾','佰','仟','亿','拾','佰','仟','万')
　　　　st = ''; st1=''
　　　　s = '%0.2f' % (nin)　　　　
　　　　sln =len(s)

　　　　if sln >; 15: return None

　　　　fg = (nin<1)

　　　　for i in range(0, sln-3):
　　　　　　　　ns = ord(s[sln-i-4]) - ord('0')
　　　　　　　　st=IIf((ns==0)and(fg or (i==8)or(i==4)or(i==0)), '', cs[ns])
　　　　　　+ IIf((ns==0)and((i<>;8)and(i<>;4)and(i<>;0)or fg
and(i==0)),'', cs[i+13])
　　　　　　+ st
　　　　　　　　fg = (ns==0)
　　　　fg = False
#---------www.iplaypy.com--------------------

　　　　for i in [1,2]:
　　　　　　　　ns = ord(s[sln-i]) - ord('0')
　　　　　　　　st1 = IIf((ns==0)and((i==1)or(i==2)and(fg or (nin<1))), '', cs[ns])
　　　　　　　+ IIf((ns>;0), cs[i+10], IIf((i==2) or fg, '', '整'))
　　　　　　　+ st1
　　　　　　　　fg = (ns==0)
　　　　st.replace('亿万','万')
　　　　return IIf( nin==0, '零', st + st1)

if __name__ == '__main__':
　　num = 12340.1
　　print num
　　print num2chn(num)
