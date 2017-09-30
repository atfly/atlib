
#!/usr/bin/python3
#-----------------------------------------------
import sys
times=0
 
#初始化一个字母表
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 
plain=input("Please input your plain text: ")
value=input("Please input your key(included negatives): ")
 
try:
	value=int(value)
except ValueError:
	print("Please input an integer.")
	sys.exit()

#将用户输入的内容转换为列表，每个字母都是列表中的一个对象。
secret_list=list(plain)
secret_list_len=len(secret_list)
 
print("")
print("secret: ",end='')

#循环一次就处理一个字母
while times < secret_list_len:
	times=times+1
 
#num实际上就是最终字母的移位量。
    #这分为几步：www.iplaypy.com
    #第一步：取出plain这个列表的第某个对象，times为循环次数。第一次循环就处理第一个字母哦！但由于列表从0开始，因此-1。
    #第二步：alphabet.index用来将用户输入在plain列表的字母，查到alphabet列表对应的位置。
    #第三步：在这个位置上加上value这个用户设置的移位量。最终的变量将是一个已经移动位置的alphabet列表对象顺序。
 
    #这个try...except实际上就是：
	try:
	#如果这个try完全正常，则说明这是一个小写字母(能在alphabet中找到该字母)，同时不存在列表超出范围(list index out of range)的问题。那么，将密文保存到output。
		num=int(alphabet.index(plain[times-1])+int(value))
		output=alphabet[num]
	except ValueError:
	#如果发生了ValueError，则说明这不是一个小写字母(不能在alphabet中找到该字母)。
		try:
		#如果这个try完全正常，则说明这是一个大写字母(能在alphabet_upper中找到该字母)，同时不存在列表超出范围的问题。那么，将密文保存到output。
			num=int(alphabet_upper.index(plain[times-1])+int(value))
			output=alphabet_upper[num]
		except IndexError:
		#如果发生了IndexError，则说明这是一个大写字母，但是列表超出范围。那么，如果列表是向前超出范围的，将回到后面；亦而反之。这是通过修改num实现的。修正之后，将密文保存
2000
到output。
			if num>25:
				num=int(num%26)
			if num<-25:
				num=int(-(-num%26))
			output=alphabet_upper[num]
		except ValueError:
		#如果发生了ValueError，则说明这不是一个英文字母(无论是alphabet或alphabet_upper都不存在该字母)。那么，这个字符将不会被加密，直接保存到output。
			output=plain[times-1]
	except IndexError:
	#如果发生了IndexError，则说明这是一个小写字母，但是列表超出范围。那么，如果列表是向前超出范围的，将回到后面；亦而反之。这是通过修改num实现的。修正之后，将密文保存到output。
		if num>25:
			num=int(num%26)
		if num<-25:
			num=int(-(-num%26))
		output=alphabet[num]
 
    #最终，将保存在output中的密文输出。
	print(output,end='')
    #由于是循环输出，每次都会换行，将导致输出的密文难以阅读。因此用end=''选项不换行。
 
#由于不换行，最后一行看着很难受，故换一行。
print("")
import sys
times=0
plain=input("Please input your plain text: ")
value=input("Please input your key(included negatives): ")
secret_list=list(plain)
secret_list_len=len(secret_list)

try:
	value=int(value)
except ValueError:
	print("Please input an integer.")
	sys.exit()


#a的ANSI码是97, z的ANSI码是122。
#A的ANSI码是65, Z的ANSI码是90。

print("")
print("secret: ",end='')

while times < secret_list_len:
	times=times+1
	#ansi_raw即没有经过任何处理的原始ANSI。
	ansi_raw=ord(secret_list[0+times-1])
	
	#ansi是经过移位加密的ANSI。
	ansi=ansi_raw+int(value)

	#word是用户输入的原始字符。
	word=(secret_list[0+times-1])

	#如果ansi_raw小于65或大于90，而且还不是小写字母，那么则说明它根本就不是字母。不加密，直接输出原始内容。
	if (ansi_raw < 65 or ansi_raw > 90) and word.islower() == False :
		print(word,end='')

	#如果ansi_raw小于97或大于122，而且还不是大写字母，那么则说明它根本不是字母。不加密，直接输出原始内容。
	elif (ansi_raw < 97 or ansi_raw > 122) and word.isupper() == False:
		print(word,end='')

	#否则，它就是字母。
	else:
		#如果它是大写字母，而且ANSI码大于90，则说明向后出界。那么通过这个公式回到开头，直到不出界为止。
		while word.isupper() == True and ansi > 90:
			ansi = -26 + ansi 

		#如果它是大写字母，而且ANSI码小于65，则说明向前出界。那么通过这个公式回到结尾，直到不出界为止。
		while word.isupper() == True and ansi < 65:
			ansi = 26 + ansi

		#如果它是小写字母，而且ANSI码大于122，则说明向后出界。那么通过这个公式回到开头，直到不出界为止。
		while word.isupper() == False and ansi > 122:
			ansi = -26 + ansi

		#如果它是小写字母，而且ANSI码小于97，则说明向前出界。那么通过这个公式回到结尾，直到不出界为止。
		while word.isupper() == False and ansi < 97:
			ansi = 26 + ansi
	
		#将处理过的ANSI转换为字符，来输出密文。
		print(chr(ansi),end='')

print("")