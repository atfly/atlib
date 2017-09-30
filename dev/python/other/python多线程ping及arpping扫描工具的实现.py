
#/usr/bin/env python
#--encoding=UTF-8--

import subprocess
from threading import Thread
from Queue import Queue
import re

num_ping_threads = 3
num_arp_threads = 3
in_queue = Queue()
out_queue = Queue()

#ips = ["10.65.10.50","10.65.10.80"]
ips = ["你要扫描的ip范围"]

def ping_scan(i,iq,oq):
	while True:
		ip = iq.get()
		print "[*]Thread %s: Pinging %s" % (i,ip)
		ret = subprocess.call("ping -c 1 %s" % ip,shell = True,stdout = open('/dev/null','w'),stderr = subprocess.STDOUT)
		if ret == 0:
			print "[*]%s: is alive." % ip
			oq.put(ip)
		else:
			print "[*]%s: did not respond" % ip
		iq.task_done()

def arping_scan(i,oq):
	while True:
		ip = oq.get()
		p = subprocess.Popen("arping -c 1  %s" % ip,shell = True,stdout = subprocess.PIPE)
		out = p.stdout.read()
		result = out.split()
		pattern = re.compile(".*:.*:.*")
		macaddr = None
		for item in result:
			if re.search(pattern,item):
				macaddr = item
			print "[*]IP Address: %s | Mac Address: %s" % (ip,macaddr)
		oq.task_done()

#www.iplaypy.com
for ip in ips:
	in_queue.put(ip)

for i in range(num_ping_threads):
	worker = Thread(target = ping_scan,args = (i,in_queue,out_queue))
	worker.setDaemon(True)
	worker.start()

for i in range(num_arp_threads):
	worker = Thread(target = arping_scan,args = (i,out_queue))
	worker.setDaemon(True)
#        worker.Daemon = True
	worker.start()

print "[*]Main Thread Waiting."
in_queue.join()
out_queue.join()

print "[*]Done!"
