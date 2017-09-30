
username='madan'
password='******'
urldict={}
connect(username,password,'t3://kyarpt5q:9001')
serverlist=adminHome.getMBeansByType('Server')
for svr in serverlist:
urldict[svr.getName()]='t3://'+svr.getListenAddress()+':'+str(svr.getListenPort())
disconnect()

for svr,url in urldict.items():
try:
connect(username,password,url)
jvmrtlist=home.getMBeansByType('JVMRuntime')
print ' '
print ' ' 
print 'The Runtime Stats of Server: '+svr 
print ' '
print 'JVM'
print ' '
print 'FreeJVM TotalJVM UsedJVM' 
print ' '
for jvmRT in jvmrtlist:
freejvm = jvmRT.getAttribute("HeapFreeCurrent")
totaljvm = jvmRT.getAttribute("HeapSizeCurrent")
usedjvm = (totaljvm - freejvm)
print freejvm,' ',totaljvm,' ',usedjvm
print ' '


eqrtlist=home.getMBeansByType('ExecuteQueueRuntime')
print ' '
print ' '
print 'EXECUTE QUEUES'
print ' '
print 'ExecuteQueueName TotalCount CurrIdleCount PendRequestCurrCount ServicedRequestTotalCount'
print ' '
for eqRT in eqrtlist:
eqname = eqRT.getAttribute("Name")
eqtthreads = eqRT.getAttribute("ExecuteThreadTotalCount")
eqithreads = eqRT.getAttribute("ExecuteThreadCurrentIdleCount")
eqqc = eqRT.getAttribute("PendingRequestCurrentCount")
eqthrougp = eqRT.getAttribute("ServicedRequestTotalCount")
print eqname,' ',eqtthreads,' ',eqithreads,' ',eqqc,' ',eqthrougp
print ' '

poolrtlist=home.getMBeansByType('JDBCConnectionPoolRuntime')
print ' '
print ' '
print 'JDBC CONNECTION POOLS'
print ' '
print 'Name Maxcapacity ActiveCurrent ActiveHighCount WaitSecondsHighCount WaitingCurrentCount State'
print ' '
for poolRT in poolrtlist:
pname = poolRT.getName()
pmaxcapacity = poolRT.getAttribute("MaxCapacity")
paccc = poolRT.getAttribute("ActiveConnectionsCurrentCount")
pachc = poolRT.getAttribute("ActiveConnectionsHighCount")
pwshc = poolRT.getAttribute("WaitSecondsHighCount")
pwfccc = poolRT.getAttribute("WaitingForConnectionCurrentCount")
pstate = poolRT.getAttribute("State")
print pname,' ',pmaxcapacity,' ',paccc,' ',pachc,' ', pwshc,' ',pwfccc,' ',pstate
print ' '



jmsrtlist=home.getMBeansByType('JMSDestinationRuntime')
print ' '
print ' '
print 'JMS DESTINATIONS'
print ' '
print 'Name ByteCurr Pending Received High MsgCurr Pending High Received ConsumersTotal' 
print ' '
for jmsRT in jmsrtlist:
jmsname = jmsRT.getAttribute("Name")
jmsbcc = jmsRT.getAttribute("BytesCurrentCount")
jmsbpc = jmsRT.getAttribute("BytesPendingCount")
jmsbrc = jmsRT.getAttribute("BytesReceivedCount")
jmsbhc = jmsRT.getAttribute("BytesHighCount")
jmsmcc = jmsRT.getAttribute("MessagesCurrentCount")
jmsmpc = jmsRT.getAttribute("MessagesPendingCount")
jmsmhc = jmsRT.getAttribute("MessagesHighCount")
jmsmrc = jmsRT.getAttribute("MessagesReceivedCount")
jmsctc = jmsRT.getAttribute("ConsumersTotalCount")
print jmsname,' ',jmsbcc,' ',jmsbpc,' ',jmsbrc,' ',jmsbhc,' ',jmsmcc,' ',jmsmpc,' ',jmsmhc,' ', jmsmrc,' ',jmsctc
print ' '
#www.iplaypy.com

disconnect()
except:
print "Skipping "+svr
continue
