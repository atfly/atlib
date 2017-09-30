
#coding:utf-8
'''
Socket 服务器端
    常见的协议及端口(这些端口是由操作系统管理的)
    ftp-Data:20,
    ftp-Control:21
    SSH:22,
    Telnet:23
    SMTP:25,
    HTTP:80
    POP3:110
    IMAP:143
    HTTPS:443
'''
import socket,threading
import time,Queue

'''
    任务线程
'''
class TaskThread(threading.Thread):

    '''
        初始化
    '''
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    '''
     执行线程
    '''
    def run(self):
        task = self.queue.get() #取出一项任务
        self.doTask(task)
        self.queue.task_done() #完成任务信号
    '''
        做任务
    '''
    def doTask(self,task):
        path = './task/'+task+'.txt'
        fp = open(path,'w')
        fp.write(task)
        fp.close()

'''
www.iplaypy.com
'''
def main():

    #Socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建tcp socket
    s.bind(('localhost',9999))#绑定到9999
    s.listen(5) #监听，但只能挂起5以下链接

    #创建队列
    queue = Queue.Queue()
    
    while True:
        client,addr = s.accept()#连接
        addr = str(addr)
        print("从 %s 获取一个连接"%addr) #直接输出到控制台
        timestr = time.ctime(time.time())+"\r\n" #时间羽化输出
        strs = '现在是：'+timestr
        client.send(strs) #发送输数据
        task = str(client.recv(1024))
        cs = '%s 客户端返回的数据为：%s'%(addr,task) #接收客户端数据
        print(cs)
        client.close()

        #任务
        task = task.split('|')
        #将任务写入到队列中
        for i in task:
            queue.put(i)

        #开始线程   
        for i in task:
            t = TaskThread(queue)
            t.setDaemon(True) #子线程随主线程一起退出
            t.start() #启动线程
            t.join(10) #保证每个线程运行，但只等10s

        queue.join() #等所有任务都处理后，再退出
            
if __name__ =='__main__':
    main()

<?php
/**
 * Socket PHP客户端
 * 
 */
header ( 'Content-type:text/html;charset=utf8' );
$host = 'tcp://localhost:9999';
$fp = stream_socket_client ( $host, $errno, $error, 20 );
if (! $fp)
{
	
	echo "$error ($errno)";
} else
{
	fwrite ( $fp, 'one|two|three' );
	while ( ! feof ( $fp ) )
	{
		echo fgets ( $fp ); #获取服务器返回的内容
	}
	fclose ( $fp );
}
