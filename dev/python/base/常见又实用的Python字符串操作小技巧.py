
print "Fill an empty string:"
empty_string = ""
for k in range(65, 91):
  empty_string += chr(k)
print empty_string

print "\nOriginal string (California humor):"
s = "She has 8 body piercings and none are visible"
print s

#www.iplaypy.com
print "\nSeparate string at any whitespace to a list of words:"
sL = []
sL = s.split()
print sL
print "\nShow item 4 on the list (lists are zero based):"
print sL[4]

# iterate through the list and also show item numbers
print "\nIterate (walk) through the list:"
for k in range (len(sL)):
    print k, sL[k]

# print words and length
print "\nAgain this time show words and ( length ):"
for word in sL:
    print word, " (", len(word), ")"

# append one more word
print "\nAdd one more word to the end:"
sL.append("yet!")
print sL

print "\nJoin the list of words to form a string again:"
# single space = " " as a delimiter
print " ".join(sL) + '\n'

# a string can be enclosed in " or ' so if you want to
# use " as part of the string, enclose it with '
s2 = '"How to Serve Your Fellow Man"'
s3 = "Cannibal's recipe book:"

# left justify string s3 and pad with 2 spaces past its length
# then concatenate ( use + ) with string s2
print "Concatenate two strings, leftjustify and pad first string:"
print s3.ljust(len(s3) + 2) + s2 + '\n'

s4 = "hippopotamus"
print "full string  = ", s4

print "spell/space it:"
for char in s4:
  print char,
print

print "count the characters:"
# create an empty dictionary
charCount = {}
for char in s4:
  charCount[char] = charCount.get(char, 0) + 1
print charCount

print "full string  = ", s4
print "first char   = ", s4[0]
print "last char    = ", s4[-1]
"""
now for something completely different, slicing ...
[starting-at-index : but-less-than-index [ : step]]
start defaults to 0, end to len(sequence), step to 1
"""
print "first 2 char = ", s4[0:2]
print "next 2 char  = ", s4[2:4]
print "last 2 char  = ", s4[-2:]
print "exclude first 3 char  = ", s4[3: ]
print "exclude last 4 char   = ", s4[:-4]
print "reverse the string    = ", s4[::-1]
print "the whole word again  = ", s4
# [start:end:step]
print "spell skipping 2 char = ", s4[::2]

print "concatenate 3 strings = ", s4 + s4 + s4
# same result
print "simply multiply by 3  = ", s4 * 3
# prints 50 dashes
print '-' * 50

print

print "Convert an integer or float to a string with repr() or str():"
num1 = 3.14
print "num1       =", num1
print "repr(num1) = %s" % repr(num1)
print "str(num1)  = %s" % str(num1)
print
str1 = str(num1)
print "Convert numeric string back to an integer or float with eval():"
num2 = eval(str1)
print "eval(str1)       =", eval(str1)
print "type(eval(str1)) =", type(eval(str1))
print "If you know the type, you can use int(str1) or float(str1)"
print
print "An added bonus, function int() has a base option:"
print "binary to decimal int('1111', 2)     =", int('1111', 2)
print "hexadecimal to decimal int('FF', 16) =", int('FF', 16)
print
print "One more bonus, eval() can evaluate a math expression string:"
print "eval('3 * 4 + 2') =", eval('3 * 4 + 2')

print

print "Comparing strings:"
print "cmp('mouse', 'mouse') = ", cmp('mouse', 'mouse')
print "cmp('mouse', 'louse') = ", cmp('mouse', 'louse')
print "cmp('louse', 'mouse') = ", cmp('louse', 'mouse')

print

# make your own words, a little character fun ...
str1 = 'Aack'       # 'Auck' might be a temptation
print "Replace A in %s with other letters:" % str1
# go from B to Z
for b in range(66, 91):
  ch = chr(b)
  if ch == 'Q':     # special case Q, use Qu
    ch = ch + 'u'
  print str1.replace('A', ch)
  
print

# how to create a multiline string ...
print "This is a multiline string:"
mlStr = """Noses are running.
Feet are smelling.
Park on driveway.
Drive on parkwa
3b8
y.
Recite at a play.
Play at a recital.
"""
print mlStr
print "Show the line that starts with Park:"
# find Park index/position
pos1 = mlStr.find("Park")
# find index of the end of that line
pos2 = mlStr.find("\n", pos1)
# slice the line from the string
line = mlStr[pos1:pos2]
print line

print

# if you just want to see if a substring is there ...
subStr = 'smell'
if subStr in mlStr:
    print "Found substring '%s'" % subStr

print

print "There are", mlStr.count('a'), "'a' in the multiline string."
print "They are at index:"
index = mlStr.find('a')  # find first
print index
while index != -1:      # look for more
    index = mlStr.find('a', index + 1)
    if index > 0:
        print index

print

print "Extract a substring located between two given substrings, here the quotes:"

def extract(text, sub1, sub2):
    """extract a substring between two substrings sub1 and sub2 in text"""
    return te
3c48
xt.split(sub1)[-1].split(sub2)[0]

str3 = 'I bought the "Python Cookbook" and could not find one single recipe about cooking the slithery beast!'
# notice that here beginning and trailing spaces can be included with the quotes
str4 = extract(str3, ' "', '" ')
print str3
print str4

print

print "Line continuation (\) can also be used for long or multiline strings:"
# combining three strings to one string
# (ignores whitespace between strings)
# (do not add a space right behind the \)
str1 = "The alien wheezes, 'Darn, this is it.  I will die now! \n"\
       "Tell my 2.4 million larvae that I esteem them ... \n"\
       "Good-bye, truculent universe.'"
print str1

print

# file names are strings, so let's find them
# find all the .py files in the working folder (path = '')
import os  # module needed for listdir()
print "Add all the python files in the working folder to a list:"
path = ''
ext  = '.py'
filelist = []
for filename in os.listdir(path):
  if filename.endswith(ext):
    filelist.append(filename)

# show the list
print filelist

print "\nPrint the file list one item on a line:"
# new line as delimiter
print "\n".join(filelist)

print

# a function can have a documentation string
def formatDollar(amount):
  "formatDollar(amount) returns a string with the amount formatted to $ currency"
  return "$%.2f" % amount

print "The function's documentation string:"
print formatDollar.__doc__
print
print "For example", 123.9 * 0.0725,"formatted to", formatDollar(123.9 * 0.0725)

