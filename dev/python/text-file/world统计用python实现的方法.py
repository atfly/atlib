
# -*- coding:utf-8 -*- 
import re
def mycmp (x,y):
    if x[1] > y[1]:
        return 1
    elif x[1] < y[1]:
        return -1
    else:
        if x[0] > y[0]:
            return -1
        elif x[0] ==y[0]:
            return 0
        else:
            return 1

file = open("word.py")

text = file.read()

wordList = str.split(re.sub(r'\W|\d',' ',text))

wordList= zip(set(wordList),map(lambda x:wordList.count(x),set(wordList)))

wordList.sort(reverse=True,cmp=mycmp)

for word in wordList:
    print word[0],":",word[1]

