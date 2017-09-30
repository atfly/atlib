
import urllib2
import re

# get page html
page = urllib2.urlopen("http://photography.nationalgeographic.com/ngs_pod_ext/searchPOD.jsp?
month=06&day=10&year=2009&page=")

txt = page.read()

#txt2 = page.read()
page.close()

# define a regex to get the img src
imgre = '<img alt="(?P<alt>[^"]*)" src="(?P<src>/staticfiles/NGS/Shared/StaticFiles/Photography/
Images/POD/.+?-ga.jpg)">'

# define a regex to get summary
summaryre = '<div class="summary">\s*<h1 class="podsummary">(?P<podsummary>[^<h>]*)</h1>\s*<p class="credit">
(?P<credit>[^</>]*)</p>\s*<div class="description">(?P<desc>.*?)<div style="float:right'


# get img alt and source

#www.iplaypy.com

m2 = re.search(imgre, txt)
if m2 is not None:
    print "get picture alt is '%s', src is 'http://photography.nationalgeographic.com%s'" % \
          (m2.group("alt"), m2.group("src"))


# get description
m3 = re.search(summaryre, txt, re.I|re.M|re.S)
if m3 is not None:
    print "photo desc: summary is '%s', credit by '%s', desciption is '%s'" % \
          (m3.group("podsummary"), m3.group("credit"), m3.group("desc"))

