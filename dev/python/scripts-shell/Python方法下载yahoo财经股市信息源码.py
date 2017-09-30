
import urllib

def getURL(url):
	socket = urllib.urlopen(url)
	readSocket = socket.read()
	socket.close()
	return readSocket

def printInfo(listInfo):
	print "Stock Symbol: " , listInfo[0]
	print "Last Trade Price: " , listInfo[1]
	print "Last Trade Date: " , listInfo[2]
	print "Last Trade Time: " , listInfo[3]
	print "Change: " , listInfo[4]
	print "Open: " , listInfo[5]
	print "Day's High: " , listInfo[6]
	print "Day's Low: " , listInfo[7]
	print "Volume: " , listInfo[8]

stockSymbol = raw_input("Enter the stock symbol: ")
stockURL = "http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=sl1d1t1c1ohgv&e=.csv" % stockSymbol
#www.iplaypy.com

stockInfoStr = getURL(stockURL)
stockInfoStr = stockInfoStr.rstrip()
stockInfoStr = stockInfoStr.split(",")

print Info(stockInfoStr)
