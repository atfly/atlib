
import sys
import os

from Tkinter import *


def quit_B():

    sys.exit()

#www.iplaypy.com

def RD():

    insert=e.get()

    pre='CreateObject("SAPI.SpVoice").Speak"'

    later='"'

    vbs=pre+insert+later

    f=open('Englishreader.vbs','w')

    f.write(vbs)

    f.close()

    os.system('Englishreader.vbs')

G=Tk()

G.title('English Reader 1.0'）

e=StringVar()

Entry(G,width=40,textvariable=e).pack()

e.set('Input your word')

Button(G,text='Reader',width=15,height=2,command=RD).pack()

Button(G,text='Exit',width=15,height=2,command=quit_B).pack()

G.mainloop()

