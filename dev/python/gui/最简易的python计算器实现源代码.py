
#-*- coding:UTF-8-*-

from Tkinter import *

def frame(root, side):
	w = Frame(root)
	w.pack(side=side, expand=YES, fill=BOTH)
	return w
#end of def

def button(root, side, text, command=None):
	w = Button(root, text=text, command=command)
	w.pack(side=side, expand=YES, fill=BOTH)
	return w
#end of def
#www.iplaypy.com

class Calculator(Frame):
	def __init__(self):
		Frame.__init__(self)
		#self.oprion_add('*Font', 'Verdana 12 bold')
		self.option_add('*Font', 'Verdana 12 bold')
		self.pack(expand=YES, fill=BOTH)
		self.master.title('Simple Cal')
		self.master.iconname('calc1')
		
		display = StringVar()
		Entry(self, relief=SUNKEN, textvariable=display).pack(side=TOP, expand=YES, fill=BOTH)
		for key in ('123', '456', '789', '+0.'):
			keyF = frame(self, TOP)
			for char in key:
				button(keyF, LEFT, char, lambda w=display, c=char: w.set(w.get() + c))
		#end of for
		opsF = frame(self, TOP)
		
		for char in '-*/=':
			if char == '=':
				btn = button(opsF, LEFT, char)
				btn.bind('<ButtonRelease-1>', lambda e, s=self, w=display: s.calc(w), '+')
			else:
				btn = button(opsF, LEFT, char, lambda w=display, s='%s '%char: w.set(w.get() + s))

			#end of if
		#end of for	
		clearF = frame(self, BOTTOM)
		button(clearF, LEFT, 'Clr', lambda w=display: w.set(''))
	#end of def
	
	def calc(self, display):
		try:
			display.set(eval(display.get()))
		except:
			display.set('ERROR')
		#end of try and except
	#end of def
#end of class

if __name__ == '__main__':
	Calculator().mainloop()