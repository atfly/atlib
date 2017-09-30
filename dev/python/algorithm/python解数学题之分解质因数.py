
from math import *
#判断n是否为素数
def isprime(n):
	if n <= 1:
		return 0
	m = int(sqrt(n))+1
	for x in range(2,m):
		if n%x == 0:
			return 0
	return 1
#利用递归分解n并打印质因数
def bprime(n):
	if isprime(n):
		print(n)
	else:
		x = 2
		while x <= int(n/2):
			if n%x == 0:
				print(x)
				return bprime(n/x)
			x = x + 1
bprime(30)  #测试分解30