
import os
import xlrd,sys

# input the excel file
Filename=raw_input('input the file name&path:')
if not os.path.isfile(Filename):
    raise NameError,"%s is not a valid filename"%Filename

#open the excel file
bk=xlrd.open_workbook(Filename)

#get the sheets number
shxrange=range(bk.nsheets)
print shxrange

#get the sheets name
for x in shxrange:
    p=bk.sheets()[x].name.encode('utf-8')
    print "Sheets Number(%s): %s" %(x,p.decode('utf-8'))

# input your sheets name
sname=int(raw_input('choose the sheet number:'))

try:
    sh=bk.sheets()[sname]
except:
    print "no this sheet"
    #return None

nrows=sh.nrows
ncols=sh.ncols
# return the lines and col number
print "line:%d  col:%d" %(nrows,ncols)

#www.iplaypy.com
#input the check column
columnnum=int(raw_input('which column you want to check pls input the num(the first colnumn num is 0):'))
while columnnum+1>ncols:
    columnnum=int(raw_input('your num is out of range,pls input again:'))

# input the searching string and column
testin=raw_input('input the string:')

#find the cols and save to a txt
outputfilename=testin + '.txt'
outputfile=open(outputfilename,'w')

#find the rows which you want to select and write to a txt file
for i in range(nrows):
    cell_value=sh.cell_value(i, columnnum)
    if testin in str(cell_value):
        outputs=sh.row_values(i)
        for tim in outputs:
            outputfile.write('%s    ' %(tim))
        outputfile.write('%s' %(os.linesep))  
outputfile.close()