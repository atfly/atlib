
import random

print('**********Guess Number game********')
#www.iplaypy.com
result = random.randint(1,10)
print('result is '+str(result))

while True:
    guess = int(input('Guess Number'))

    if guess < result:
        print('Numbe is low')
        continue

    elif guess > result:
        print('Numbe is high')
        continue

    elif guess > 20 or guess <1:
        print('Numbe is out of range')
        continue

    elif guess == result:
        print('yes you are right!')
        break

    else:
        print('please !!')