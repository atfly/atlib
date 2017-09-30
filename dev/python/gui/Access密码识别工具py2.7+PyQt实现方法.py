
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\PyAccess.ui'
# Created: Thu Feb 23 15:07:51 2012
#      by: PyQt4 UI code generator 4.9.1


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class PYAccess(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(397, 91)
        MainWindow.setMaximumSize(QtCore.QSize(397, 91))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Access.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.btnSelectFile = QtGui.QPushButton(self.centralWidget)
        self.btnSelectFile.setGeometry(QtCore.QRect(290, 20, 91, 23))
        self.btnSelectFile.setObjectName(_fromUtf8("btnSelectFile"))
        self.tbFilePath = QtGui.QLineEdit(self.centralWidget)
        self.tbFilePath.setGeometry(QtCore.QRect(20, 20, 261, 20))
        self.tbFilePath.setObjectName(_fromUtf8("tbFilePath"))
        self.tbVersion = QtGui.QLineEdit(self.centralWidget)
        self.tbVersion.setGeometry(QtCore.QRect(20, 50, 111, 20))
        self.tbVersion.setObjectName(_fromUtf8("tbVersion"))
        self.tbPassword = QtGui.QLineEdit(self.centralWidget)
        self.tbPassword.setGeometry(QtCore.QRect(160, 50, 221, 20))
        self.tbPassword.setObjectName(_fromUtf8("tbPassword"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btnSelectFile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.slotselectfile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def slotselectfile(self):
        fname = QtGui.QFileDialog.getOpenFileName(MainWindow, 'Open Access File','/*.mdb')
        if fname=='':
            return
        else:
            self.tbFilePath.setText(fname)
            # 未加密的文件0x42开始至0x61之前的每间隔一字节的数值
            baseByte=[0xbe, 0xec, 0x65, 0x9c, 0xfe,0x28, 0x2b, 0x8a, 0x6c, 0x7b,0xcd, 0xdf, 0x4f, 0x13, 0xf7,0xb1]
            # 标志 0x62 处的数值
            flagByte = 0x0c
            # 定义密码字符串
            password = '';
            # 读取方式打开文件并复制给fs
            fs=open(fname,'r')
            fs.seek(0x14)
            version='unknow'
            ver = ord(fs.read(1))
            if ver==1:
                version='Access2000'
            elif ver==0:
                version='Access97'
            fs.seek(0x42)
            bs=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            integer = 0
            while integer < 33:
                tmpInt=ord(fs.read(1))
                bs[integer]=tmpInt
                integer=integer+1
            #标记
            flag = bs[32] ^ flagByte
            # 开始循环
            i = 0
            while i < 16:
                b = (baseByte[i] ^ bs[i * 2])
                if i % 2 == 0 and ver == 1:
                    b = b^flag;
                if b > 0 :
                    password = password + chr(b)
                i=i+1
            fs.close()
            self.tbVersion.setText(version)
            self.tbPassword.setText(password)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Access 数据库密码破解工具", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectFile.setText(QtGui.QApplication.translate("MainWindow", " 选择文件 ...", None, QtGui.QApplication.UnicodeUTF8))
        self.tbFilePath.setText(QtGui.QApplication.translate("MainWindow", "Access文件路径，请点击右侧“选择文件” ", None, QtGui.QApplication.UnicodeUTF8))
        self.tbVersion.setText(QtGui.QApplication.translate("MainWindow", " 版本信息 ", None, QtGui.QApplication.UnicodeUTF8))
        self.tbPassword.setText(QtGui.QApplication.translate("MainWindow", " Access 文件密码 ",
2000
 None, QtGui.QApplication.UnicodeUTF8))

#www.iplaypy.com

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = PYAccess()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
