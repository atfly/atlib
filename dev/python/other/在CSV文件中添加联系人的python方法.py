
import sys
import os
import time
import csv

def addPerson(filename):
	'''Add a new Person\'s Tel'''
	person = raw_input('Enter the person\'s name: ')
	tel = raw_input('Enter the person\'s tel: ')
	update=time.strftime('%Y-%m-%d %H:%m:%S')
	
	f=csv.writer(file(filename, 'a'))
	f.writerow([person,tel,update])
	#f.close()
	
	print 'New Person\'s tel has been added!'
	
if (os.path.isfile('TelBook.csv'))==False:
		title=['NAME','TEL','TIME']
		f=csv.writer(file('TelBook.csv','w'))
		f.writerow(title)
		#f.close()
		
input=raw_input('Do you wanna Enter a new Person\' tel?(y/n)')

if input=='y':
	flag=True

else:
	flag=False
	print 'Thanks, Bye!'

while flag:		
	addPerson('TelBook.csv')
	t=raw_input('Do you wanna Enter another?(y/n)')
	if t!='y':
		print 'Thanks, Bye!'
		break
#www.iplaypy.com
import sys
import os
import time
import csv

def addPerson(filename):
	'''Add a new Person\'s Tel'''
	person = raw_input('Enter the person\'s name: ')
	tel = raw_input('Enter the person\'s tel: ')
	update=time.strftime('%Y-%m-%d %H:%m:%S')
	
	f=csv.writer(file(filename, 'ab'))
	record=[person,tel,update]
	f.writerow(record)
	#f.close()
	
	print 'New Person\'s tel has been added!'
	
if (os.path.isfile(r'D:\Exercise\Python\TelBook\TelBook.csv'))==False:
		title=['NAME','TEL','TIME']
		#f=csv.writer(file(r'D:\Exercise\Python\TelBook\TelBook.csv','w'))
		f=csv.writer(file(r'D:\Exercise\Python\TelBook\TelBook.csv','wb'))
		f.writerow(title)
		file(r'D:\Exercise\Python\TelBook\TelBook.csv').close()


input=raw_input('Do you wanna Enter a new Person\' tel?(y/n)')
if input=='y':
	flag=True
else:
	flag=False
	print 'Thanks, Bye!'
while flag:		
	addPerson(r'D:\Exercise\Python\TelBook\TelBook.csv')
	t=raw_input('Do you wanna Enter another?(y/n)')
	if t!='y':
		print 'Thanks, Bye!'
		break
	file(r'D:\Exercise\Python\TelBook\TelBook.csv').close()
