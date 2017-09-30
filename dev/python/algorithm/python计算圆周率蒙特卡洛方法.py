
import random
count = 1000000;

incount = 0;

for i in range(count) :
	x = random.random()
	y = random.random()
	if (x**2 + y**2) < 1 :
		incount+=1
print(incount* 4.0 / count ) 