
import sys, shelve
def store_person(db):
	'''
	Store your info.
	'''
	pid = raw_input('Enter your ID: ')
	person = {}
	person['name'] = raw_input('Enter your name: ')
	person['age'] = raw_input('Enter your age: ')
	person['phone'] = raw_input('Enter your phone number: ')
	db[pid] = person

#www.iplaypy.com

def lookup_person(db):
	'''
	Lookup your info.
	'''
	pid = raw_input('Enter the ID: ')
	if pid in db.keys():        #检查输入的ID是否存在
		field = raw_input('What do you want to lookup?(Name, Age, Phone)')
		field = field.strip()   #删除field中可能有的空格和换行符
		if field in ('Name', 'Age', 'Phone'):   #检查用户的输入       
			field = field.strip().lower()
                        print field.capitalize() + ':', db[pid][field]
		else:
			print 'The input is error!Please enter: Name, Age or Phone'
	else:
		print "The ID is not exist!"
		#lookup_person(db)



def print_help():
	print '''
	The available commands are:
	store, lookup,quit,?
	'''

def enter_command():
	cmd = raw_input('Enter your command("?" for help): ')
	cmd = cmd.strip().lower()
	return cmd

def main():
	database = shelve.open('D:\\python-test\\test.dat')
	try:
		while True:
			cmd = enter_command()
			if cmd == 'store':
				store_person(database)
			elif cmd == 'lookup':
				lookup_person(database)
			elif cmd == '?':
				print_help()
			elif cmd == 'quit':
				return
	finally:
		database.close()

if __name__ == '__main__': main()