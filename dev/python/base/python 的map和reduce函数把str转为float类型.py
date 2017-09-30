
def str2float(s):
	def str2int(ns):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ns]

	def f(x,y):
		return x*10+y
	resultNum = 0
	numL = s.split('.')

	for index,numS in enumerate(numL):
		if index==0:
			resultNum = resultNum + reduce(f,map(str2int,numS))
		else:
			resultNum = resultNum + reduce(f,map(str2int,numS))*pow(10,0-len(numS))
	return resultNum