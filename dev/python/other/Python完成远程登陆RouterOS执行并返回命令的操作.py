
import telnetlib,time,os

#config_user_password_port_etc.
HOST='192.168.1.1'
PORT='23'

user= 'test'

password= '1'

command_1='ping 8.8.8.8 c 10'

command_2='quit'

tn=telnetlib.Telnet(HOST,PORT)
tn = telnetlib.Telnet(HOST)

#input user

tn.read_until(b"Login: ")

tn.write(user.encode('UTF-8') + b"\n")

#input password

tn.read_until(b"Password: ")

tn.write(password.encode('UTF-8') + b"\n")

#run command

tn.read_until(b'>')

tn.write(command_1.encode('UTF-8')+b"\r\n")

time.sleep(10)

tn.read_until(b'>')

tn.write(command_2.encode('UTF-8')+b"\r\n")


#write result in files

#print(tn.read_all)

result=tn.read_all()

file_object=open('result.txt','wb')

file_object.write(result)

file_object.close()

print ('Finish')

tn.close()

