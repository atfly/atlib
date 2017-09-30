
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
输入文件格式:
107.0381,29.1470;
107.0429,29.1880;
107.0654,29.2076;
107.1492,29.1774;
107.1767,29.1532;
107.1518,29.1260;
107.0822,29.1201;
107.0743,29.1248;
107.0566,29.1338;
107.0381,29.1470;
文件最后没有空行。
不要求度形式的坐标小数点后面一定是四位。

python num_convert.py [-o outputfilename] inputfilename
python num_convert.py -v 打印版本信息
python num_convert.py -h 打印帮助信息
"""

import sys
import getopt

def datafromfile(f):
    ret = []

    for line in f:
        if line:
            line = line[:-2]
            num1,num2 = line.split(r',')
            ret1,ret2 = conv(num1),conv(num2)
            ret.append([ret1,ret2])
        else:
            ret='\n'
    return ret

def conv(num):
    '''
    bef0: 小数点前面的值
    aft012: 转换后小数点后面第一二位数
    aft034: 转换后小数点后面第三四伴数
    '''
    num = eval(num)

    bef0, aft0 = int(num), num-int(num)

    aft012, aft034_t = int(aft0*60), aft0*60-int(aft0*60)

    aft034 = int(round(aft034_t*60))

    if aft034 < 10:
        aft034 = '0'+str(aft034)

    elif aft034 == 60:
        aft034='00'
        aft012 += 1

    elif aft034 > 60:
        print "error:%s"%aft034

    if aft012<10:aft012 = '0' + str(aft012)

    sys.stderr.write("bef0:%s,aft012:%s,aft034:%s;"%(bef0, aft012, aft034)
)
    return "%s.%s%s"%(bef0, aft012, aft034)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:],"ho:v")

    except getopt.GetoptError, err:
        print str(err)
        sys.exit(2)

    version = False

    help_ = False

    output_t = ''

    for o,a in opts:
        if o == '-v':
            version = True
        elif o == '-h':
            help_ = True
        elif o == '-o':
            output_t = a
        else:
            assert False, "unhandled option"

    if help_:
        sys.stdout.write('''

#-------www.iplaypy.com------------
num_convert.py

basic usage:
python num_convert.py [-o outputfilename] inputfilename
python num_convert.py -v print version information
python num_convert.py -h print this help.
        ''')
        sys.exit(0)
    if version:
        sys.stdout.write("version 0.1")
        sys.exit(0)
    if len(args) == 0:
        sys.stderr.write("NEED INPUT FILE!!!")
        sys.exit(2)
    else:
        file_in = args[0]
    if len(output_t) == 0:
        output = sys.stderr
    else:
        try:
            output = open(output
966
_t,'w')
        except:
            raise

    with open(file_in,'r') as f:
        datas = datafromfile(f)

    #sys.stderr.write(str(datas))
    for data in datas:
        packed_data = ','.join(data)+';\n'
        output.write(packed_data)

if __name__ == "__main__":
    main()
