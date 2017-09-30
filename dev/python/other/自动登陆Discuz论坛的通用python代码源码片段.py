
	user='xxx'
	pwd='xxx'
	dom='http://www.disscuz.net/'
	try:
	   flag = login_dz(username=user,password=pwd,domain=dom)
	   print(flag)
	except Exception,e:
	   print('Error:',e)