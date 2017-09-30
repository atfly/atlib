
import re

t = 'abcakacdabcefg'
#前瞻断言:匹配...开头,包括...本身
print re.findall('(?=a)\w+?', t)
#反前瞻断言:匹配不以...开头,不包括...本身
print re.findall('(?!a)\w+?', t)
#后顾断言:匹配...开头,不包括...本身
print re.findall('(?<=a)\w+?', t)
#反后顾断言:匹配不以...开头,包括...本身
print re.findall('(?<!a)\w+?', t)
