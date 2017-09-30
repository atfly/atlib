
def bubblesort(s):
	x=0
	N=0
	n=0
	while N<(len(s)-1):
		while n<(len(s)-1):
			if s[x]>s[x+1]:
				s[x],s[x+1] = s[x+1],s[x]
			x+=1
			n+=1
		x=0
		n=0
		N+=1
	return s
def selectsort(s,x,y):
	while (y-x)>1:
		if s[x]>min(s[x:y]):
			k = s.index(min(s[x:y]))
			s[x],s[k] = s[k],s[x]
		x+=1
	return s	
def bubblesort(s):
	for i in range(len(s)-1):
		for j in range(len(s)-1):
			if s[j]>s[j+1]:
				s[j],s[j+1] = s[j+1],s[j]
	return s