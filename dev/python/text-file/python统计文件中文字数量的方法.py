
from string import *

def countWords(s):
    words=split(s)
    return len(words)       #returns the number of words

filename=open("welcome.txt",'r')    #open an file in reading mode

#www.iplaypy.com
total_words=0

for line in filename:
    total_words=total_words + countWords(line)      #counts the total words

print total_words