
# -*- coding: cp936 -*-

import Tkinter
import urllib

class Window:

    def __init__(self,root):
        self.root = root
        self.entryUrl=Tkinter.Entry(root)
        self.entryUrl.place(x=5,y=15)
        self.get=Tkinter.Button(root,text='download',command=self.Get)
        self.get.place(x=120,y=15)
        self.edit=Tkinter.Text(root)
        self.edit.place(y=50)

    def Get(self):
        url = self.entryUrl.get()
        page=urllib.urlopen(url)
        data=page.read()
        self.edit.insert(Tkinter.END,data)
        page.close()

root=Tkinter.Tk()

window=Window(root)

root.minsize(600,480)
root.mainloop()
    
