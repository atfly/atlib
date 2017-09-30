
1.import os,sys,string   
2.import time   
3.  
4.def view_bar(num=1, sum=100, bar_word=":"):   
5.    rate = float(num) / float(sum)   
6.    rate_num = int(rate * 100)   
7.    print '\r%d%% :' %(rate_num),   
8.    for i in range(0, num):   
9.        os.write(1, bar_word)   
10.    sys.stdout.flush()   
11.  
12.if __name__ == '__main__':   
13.    for i in range(0, 100):   
14.        time.sleep(0.1)   
15.        view_bar(i, 100)  
