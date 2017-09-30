
#!/usr/bin/python
#coding=gbk

import datetime
import subprocess
import codecs
import reportlab.pdfbase.ttfonts
reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('song', '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'))
import reportlab.lib.fonts

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def disk_report():
 p = subprocess.Popen("df -h ",shell=True,stdout=subprocess.PIPE)
 return p.stdout.readlines()

#www.iplaypy.com

def create_pdf(input,output="disk.pdf"):
 now = datetime.datetime.today()
 date = now.strftime("%h %d %Y %H:%M:%S")
 c = canvas.Canvas(output)
 c.setFont('song',10)
 textobject = c.beginText()
 textobject.setTextOrigin(inch,11*inch)
 textobject.textLines('''Disk Capacity Report: %s ''' % date )
 for line in input:
  line=line.decode("gbk")
  textobject.textLine(line.strip())
 c.drawText(textobject)
 c.showPage()
 c.save()
report = disk_report()
create_pdf(report)