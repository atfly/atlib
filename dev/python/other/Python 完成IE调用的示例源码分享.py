
#导入方法，模块
import win32com.client   
import time   

ie6=win32com.client.Dispatch("InternetExplorer.Application")   

ie6.Navigate("http://localhost/skyenet/")   

ie6.Visible=1  

while ie6.Busy:   
  time.sleep(1)  

#www.iplaypy.com 
  
document=ie6.Document   

document.getElementById("username").value="alibaba"  

document.getElementById("password").value="zhimakamen"  

document.forms[0].submit()  