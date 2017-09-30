
#在交互模式下,输入以下python代码
[x for x in range(1,10) if not [y for y in range(2,x) if x % y == 0]]
#output 
#[1,3,5,7]
#www.iplaypy.com