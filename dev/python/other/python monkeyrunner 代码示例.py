
'''from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice'''
import sys
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By

device=MonkeyRunner.waitForConnection(1.0,'d1d4c874')
device.startActivity(component='com.broadvision.myvmoso.phone.myvmoso.enterprise/com.broadvision.myvv.MyVV_Splash')
'''easy_device=EasyMonkeyDevice(device)'''

MonkeyRunner.sleep(5)
result=device.takeSnapshot()
result.writeToFile('./shotbegin.png','png')
'''
for i in range(15):
 device.touch(134,145,"DOWN")
 MonkeyRunner.sleep(5)
 device.touch(134,145,"DOWN_AND_UP")
 MonkeyRunner.sleep(5)
 device.touch(134,145,"UP")
 MonkeyRunner.sleep(5)
'''
'''easy_device.touch(By.id('id/focus_create_priority_no'),"DOWN_AND_UP")'''
'''device.press('KEYCODE_BACK',"DOWN_AND_UP")'''
device.touch(380,800,"DOWN_AND_UP")

MonkeyRunner.sleep(5)
result=device.takeSnapshot()
result.writeToFile('./shotend.png','png')
