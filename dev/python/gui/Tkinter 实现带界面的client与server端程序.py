
import Tkinter
import socket

# www.iplaypy.com 
class window:
    def __init__(self,root):
        label1=Tkinter.Label(root,text='IP')
        label2=Tkinter.Label(root,text='PORT')
        label3=Tkinter.Label(root,text='DATA')
        label1.place(x=5,y=5)
        label2.place(x=30,y=5)
        label3.place(x=35,y=5)
        self.entryIP=Tkinter.Entry(root)
        self.entryIP.insert(Tkinter.END,'127.0.0.1')
        self.entryport=Tkinter.Entry(root)
        self.entryport.insert(Tkinter.END,'1051')
        self.entrydata=Tkinter.Entry(root)
        self.entrydata.insert(Tkinter.END,'hello')
        self.Recv=Tkinter.Text(root)
        self.entryIP.place(x=40,y=5)
        self.entryport.place(x=40,y=30)
        self.entrydata.place(x=40,y=55)
        self.Recv.place(y=115)
        self.send=Tkinter.Button(root,text='send',command=self.send)
        self.send.place(x=40,y=80)
    def send(self):
        try:
            self.entryIP.get()
            port=int(self.entryport.get())
            data=self.entrydata.get()
            client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client.send(data)
            rdata=client.recv(1024)
            self.Recv.insert(Tkinter.END,rdata.decode())
            client.close()
        except:
            self.Recv.insert(Tkinter.END,'error')
root=Tkinter.Tk()
window=window(root)
root.mainloop()

import threading
import Tkinter
import socket
class ListenThread(threading.Thread):
    def __init__(self,edit,server):
        threading.Thread.__init__(self)
        self.edit=edit
        self.server=server
        def run(self):
            while 1:
                try:
                    client,addr=self.server.accept()
                    self.edit.insert(Tkinter.END,'connect from:%s:%d\n' % addr)
                    data=client.recv(1024)
                    self.edit.insert(Tkinter.END,'receive data:%s \n' % data)
                    client.send(str('i get:%s' % data).encode())
                    client.close()
                    self.edit.insert(Tkinter.END,'close client\n')
                except:
                    self.edit.insert(Tkinter.END,'close connect\n')
                    break
class control(threading.Thread):
    def __init__(self,edit):
        threading.Thread.__init__(self)
        self.edit=edit
        self.event=threading.Event()
        self.event.clear()
    def run(self):
        server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        server.bind(('',1051))
        server.listen(2)
        self.edit.insert(Tkinter.END,'connect...\n')
        self.lt=ListenThread(self.edit,server)
        self.lt.setDaemon(True)
        self.lt.start()
        self.event.wait()
        server.close()
    def stop():
        self.event.set()
class window:
    def __init__(self,root):
        self.root=root
        self.butlisten=Tkinter.Button(root,text='start',command=self.listen)
        self.butlisten.place(x=20,y=15)
        self.butclose=Tkinter.Button(root,text='colse',command=self.close)
        self.butclose.place(x=120,y=15)
        self.edit=Tkinter.Text(root)
        self.edit.place(y=50)
    def listen(self):
        self.ctr=control(self.edit)
        self.ctr.setDaemon(True)
        self.ctr.start()
    def close(self):
        self.ctr.stop()

root=Tkinter.Tk()
window=window(root)
root.mainloop()
