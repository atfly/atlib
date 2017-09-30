
 # coding=UTF-8  
 import wx;  
 from com.download import download;  
 import os;  

 class Downloadfile(wx.Frame):  
     def __init__(self):  
         #save file url;  
         self.saveURL = ""  
         wx.Frame.__init__(self,None,-1,"download",size=(400,150));  
         panel = wx.Panel(self,-1);  
         self.topLabel = wx.StaticText(panel,-1,"1,enter url 2, click save 3, start down")  
         self.topLabel.SetFont(wx.Font(18,wx.SWISS,wx.NORMAL,wx.BOLD))  
         self.label1 = wx.StaticText(panel,-1,"  url:  ");  
         self.label1.SetFont(wx.Font(14,wx.SWISS,wx.NORMAL,wx.BOLD))  
         self.input1 = wx.TextCtrl(panel,-1);  
         #self.input1.SetInsertionPoint(0);  
         self.input1.Value = "http://.....mp3"  
         self.saveBtn = wx.Button(panel,-1,"save");  
         self.Bind(wx.EVT_BUTTON,self.save,self.saveBtn)  
         self.button = wx.Button(panel,-1,"down");  
         self.Bind(wx.EVT_BUTTON,self.startDown,self.button);  
         self.gauge = wx.Gauge(panel,-1,100,(20,90),(350,25));  
         self.gauge.SetBezelFace(3);  
         self.gauge.SetShadowWidth(3);  
         self.gaugeLB = wx.StaticText(panel,-1,"0%");  
         self.gaugeLB.SetFont(wx.Font(14,wx.SWISS,wx.NORMAL,wx.BOLD))  
         self.multText = wx.TextCtrl(panel,-1,"",size=(400,100),style=wx.TE_MULTILINE)  
         #Add(window, proportion=0, flag=0, border=0, userData=None)  
         mainSize = wx.BoxSizer(wx.VERTICAL);  
         mainSize.Add(wx.StaticLine(panel),0,wx.EXPAND);  
         mainSize.Add(self.topLabel);  
         mainSize.Add(wx.StaticLine(panel),0,wx.EXPAND);  
         urlSizer = wx.FlexGridSizer(cols=2,hgap=5,vgap=5);  
         urlSizer.AddGrowableCol(1);  
         urlSizer.Add(self.label1,0,wx.Left);  
         urlSizer.Add(self.input1,0,wx.EXPAND);  
         btnSizer = wx.BoxSizer(wx.HORIZONTAL)  
         btnSizer.Add((20,20), 1)  
         btnSizer.Add(self.saveBtn)  
         btnSizer.Add((20,20), 1)  
         btnSizer.Add(self.button)  
         btnSizer.Add((20,20), 1)  
         progressSizer = wx.BoxSizer(wx.HORIZONTAL);  
         progressSizer.Add(self.gauge);  
         progressSizer.Add((20,20), 0)  
         progressSizer.Add(self.gaugeLB);  
         textSizer = wx.FlexGridSizer(cols=2,hgap=5,vgap=5);  
         textSizer.AddGrowableCol(0);  
         textSizer.Add(self.multText,0,wx.EXPAND);  
         mainSize.Add(urlSizer,0,wx.EXPAND|wx.ALL,10);  
         mainSize.Add(btnSizer,0,wx.EXPAND|wx.ALL,10);  
         mainSize.Add(progressSizer,0,wx.EXPAND|wx.ALL,10);  
         mainSize.Add(textSizer,0,wx.EXPAND|wx.ALL,10);  
         panel.SetSizer(mainSize);  
         mainSize.Fit(self);  
         mainSize.SetSizeHints(self);  
         self.addLog("---------please select save file-------");  

     def addLog(self,t):  
         self.multText.AppendText(t+'\n');  

     def startDown(self,event):  
         self.addLog("---start download file");  
         down = download(self.input1.Value,self.saveURL,self.changeProgress,self.downComplete)  

     def getNameFromURL(self,url = ""):  
         ls = str(url).split("/");  
         return ls[len(ls)-1];  

     def save(self,event):  
         self.addLog("---start select save file");  
         woldcard= "All files(*.*)|*.*";  
         dialog = wx.FileDialog( None , "save file" , os.getcwd() , 
                  self.getNameFromURL(self.input1.Value) , woldcard , wx.SAVE);  
         if dialog.ShowModal() == wx.ID_OK:  
             self.saveURL = dialog.GetPath();  
             self.addLog("---selected file: " + self.saveURL )  
         dialog.Destroy();  

     def changeProgress(self,n=0):  
         self.gauge.SetValue(n);  
         self.gaugeLB.SetLabel( str(n)+'%')  

     def downComplete(self,event):  
         self.addLog("---------down complete ! ---------");  
         dlg = wx.MessageDialog(None,"download complete! " , "complete" , style = wx.OK)  
         code = dlg.ShowModal();  
         dlg.Destroy();  #www.iplaypy.com

 if __name__ == "__main__":  
     app = wx.PySimpleApp();  
     frame = Downloadfile();  
     frame.Show();  
     app.MainLoop(); 
# coding=UTF-8  
import urllib;  
import wx;  
def dow
2000
nload(url,filename="" , fun="" ,completeF=""):  
    def myreporthook(block_count,block_size,file_size):  
         if file_size == -1 :  
            print "can't download file";  
         else:  
            percentage = int( (block_count*block_size*100)/file_size );  
            fun(percentage);  
            if percentage > 100 :  
                print "100%";  
            else:  
              print "%d%%" % (percentage);  
    filehandler,m = urllib.urlretrieve(url,filename,reporthook = myreporthook );  
    print "done";  
    completeF();  
    return filehandler;  
#if __name__ == "__main__":  
#  http = download("http://....mp3" , "e:/1.mp3");  