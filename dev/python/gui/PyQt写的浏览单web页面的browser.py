
#!/usr/bin/env python

import sys

from PyQt4 import QtCore, QtGui
from browser import Ui_HttpWidget

class httpWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(httpWidget, self).__init__(parent)
        self.ui = Ui_HttpWidget()
        self.ui.setupUi(self)
        
        L = self.layout()
        L.setMargin(0)
        self.ui.horizontalLayout.setMargin(5)
        
        url = 'http://google.com'
        self.ui.url.setText(url)
        
        self.ui.webView.setUrl(QtCore.QUrl(url))
        
        self.ui.back.setEnabled(False)
        self.ui.next.setEnabled(False)
        
        QtCore.QObject.connect(self.ui.back, QtCore.SIGNAL("clicked()"),\
                        self.back)
        QtCore.QObject.connect(self.ui.next, QtCore.SIGNAL("clicked()"),\
                        self.next)
        QtCore.QObject.connect(self.ui.url, QtCore.SIGNAL("returnPressed()"),\
                        self.url_changed)
        QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("linkClicked(const QUrl&)"),\
                        self.link_clicked)
        QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("urlChanged(const QUrl&)"),\
                        self.link_clicked)
        QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("loadProgress(int)"),\
                        self.load_progress)
        QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("titleChanged(const QString&)"),\
                        self.title_changed)
        QtCore.QObject.connect(self.ui.reload, QtCore.SIGNAL("clicked()"),\
                        self.reload_page)
        QtCore.QObject.connect(self.ui.stop, QtCore.SIGNAL("clicked()"),\
                        self.stop_page)
        
        QtCore.QMetaObject.connectSlotsByName(self)
        
    def url_changed(self):
        page = self.ui.webView.page()
        history = page.history()
        if history.canGoBack():
            self.ui.back.setEnabled(True)
        else:
            self.ui.back.setEnabled(False)
            
        if history.canGoForward():
            self.ui.next.setEnabled(True)
        else:
            self.ui.next.setEnabled(False)
            
        url = self.ui.url.text()
        self.ui.webView.setUrl(QtCore.QUrl(url))
        
    def stop_page(self):
        self.ui.webView.stop()
        
    def title_changed(self, title):
        self.setWindowTitle(title)
        
    def reload_page(self):
        self.ui.webView.setUrl(QtCore.QUrl(self.ui.url.text()))
        
    def link_clicked(self, url):
        page = self.ui.webView.page()        
        self.__setHistButtonState(page, self.ui.back, self.ui.next)
            
        self.ui.url.setText(url.toString())
        
    def load_progress(self, load):
        if load == 100:
            self.ui.stop.setEnabled(False)
        else:
            self.ui.stop.setEnabled(True)
            
    def back(self):
        page = self.ui.webView.page()
        self.__setHistButtonState(page, self.ui.back, None)
        history = page.history()
        history.back()
            
    def next(self):
        page = self.ui.webView.page()
        history = page.history()
        history.forward()
        
        self.__setHistButtonState(page, None, self.ui.next)
          
    #control the navigator buttons enability
    def __setHistButtonState(self, page, back, next):
        history = page.history()
        
        if back is not None:
            if history.canGoBack():
                back.setEnabled(True)
            else:
                back.setEnabled(False)
            
        if next is not None:
            if history.canGoForward():
                next.setEnabled(True)
            else:
                next.setEnabled(False)
        
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = httpWidget()
    myapp.show()
    sys.exit(app.exec_())



        

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_HttpWidget(object):
    def setupUi(self, HttpWidget):
        HttpWidget.setObjectName(_fromUtf8("HttpWidget"))
        HttpWidget.resize(636, 336)
        self.verticalLayout = QtGui.QVBoxLayout(HttpWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.back = QtGui.QPushButton(HttpWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon)
        self.back.setObjectName(_fromUtf8("back"))
        self.horizontalLayout.addWidget(self.back)
        self.next = QtGui.QPushButton(HttpWidget)
        self.next.setEnabled(True)
        self.next.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon1)
        self.next.setObjectName(_fromUtf8("next"))
        self.horizontalLayout.addWidget(self.next)
        self.stop = QtGui.QPushButton(HttpWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon2)
        self.stop.setObjectName(_fromUtf8("stop"))
        self.horizontalLayout.addWidget(self.stop)
        self.reload = QtGui.QPushButton(HttpWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("reload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload.setIcon(icon3)
        self.reload.setObjectName(_fromUtf8("reload"))
        self.horizontalLayout.addWidget(self.reload)
        self.url = QtGui.QLineEdit(HttpWidget)
        self.url.setObjectName(_fromUtf8("url"))
        self.horizontalLayout.addWidget(self.url)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.webView = QtWebKit.QWebView(HttpWidget)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)

        self.retranslateUi(HttpWidget)
        QtCore.QMetaObject.connectSlotsByName(HttpWidget)

    def retranslateUi(self, HttpWidget):
        HttpWidget.setWindowTitle(QtGui.QApplication.translate("HttpWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.back.setToolTip(QtGui.QApplication.translate("HttpWidget", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.back.setText(QtGui.QApplication.translate("HttpWidget", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.next.setToolTip(QtGui.QApplication.translate("HttpWidget", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.next.setText(QtGui.QApplication.translate("HttpWidget", "    Next", None, QtGui.QApplication.UnicodeUTF8))
        self.stop.setToolTip(QtGui.QApplication.translate("HttpWidget", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.stop.setText(QtGui.QApplication.translate("HttpWidget", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.reload.setToolTip(QtGui.QApplication.translate("HttpWidget", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.reload.setText(QtGui.QApplication.translate("HttpWidget", "Reload", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
