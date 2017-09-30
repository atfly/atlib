
# -*- coding:utf-8 -*-

import sys
import base64
from PyQt4 import QtCore,QtGui

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle(u'专用链接转换')
        self.setFixedSize(300,200)
        vbox=QtGui.QVBoxLayout()
        self.inputbox=QtGui.QTextEdit()
        vbox.addWidget(self.inputbox)
        hbox=QtGui.QHBoxLayout()
        tranbtn=QtGui.QPushButton(u'转换')
        aboutbtn=QtGui.QPushButton(u'关于')
        hbox.addWidget(aboutbtn)
        hbox.addWidget(tranbtn)
        self.connect(aboutbtn,QtCore.SIGNAL('clicked()'),self.OnAbout)
        self.connect(tranbtn,QtCore.SIGNAL('clicked()'),self.OnTran)
        vbox.addLayout(hbox)
        self.outputbox=QtGui.QTextEdit()
        vbox.addWidget(self.outputbox)
        self.setLayout(vbox)
        #www.iplaypy.com
        
    def OnAbout(self):
        QtGui.QMessageBox.about(self,u'关于',u'迅雷、QQ旋风、flashget专用链接转换工具 by ckh')

    def OnTran(self):
        url=self.inputbox.toPlainText()

        if url.isEmpty():
            QtGui.QMessageBox.warning(self,'warning',u'没有输入链接')
            return
        tranurl=url.split('://')

        if tranurl[0].toUpper()=='THUNDER':
            res=base64.decodestring(tranurl[1])
            self.outputbox.setText(unicode(res[2:-2],'cp936'))

        elif tranurl[0].toUpper()=='QQDL':
            res=base64.decodestring(tranurl[1])
            self.outputbox.setText(unicode(res,'cp936'))

        elif tranurl[0].toUpper()=='FLASHGET':
            res=base64.decodestring(tranurl[1])
            self.outputbox.setText(unicode(res[10:-10],'cp936'))

        else:
            QtGui.QMessageBox.warning(self,u'警告',u'输入的地址不是迅雷、QQ旋风或者flashget专用链接')    
               
         
if __name__=='__main__':
    app=QtGui.QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())
