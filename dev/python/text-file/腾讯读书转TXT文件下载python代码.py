
import re, os, urllib2

url = 'http://book.qq.com/s/book/0/22/22707/'
page_re = re.escape(url) + r'\d+\.shtml'
data = urllib2.urlopen(url).read()
pages = re.findall(page_re, data)
count = 1

txt = []
for page in pages:
    html = urllib2.urlopen(page).read()
    print "downloading [%d/%d], %s" % (count, len(pages), page)
    m = re.findall(re.escape('<div id="content"') + '.*?' + re.escape('</div>'), html, re.DOTALL)
    if m:
        m = m[0]
    txt.append(m)
    count += 1

f=open('downqq.html', 'wb')#www.iplaypy.com
f.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
             "http://www.w3.org/TR/html4/loose.dtd"><html lang="en">
           <head><meta http-equiv="Content-Type" content="text/html;charset=GBK"><title></title></head><body>""")
f.write('\r\n\r\n\r\n'.join(txt))
f.write('</body></html>')
f.close()

print("DONE!")
os.system("downqq.html")


