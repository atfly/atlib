
def fnPrime(n):
	for i in range(2,n,1):
		if(n % i == 0):
			return bool(0)
	return bool(1)
