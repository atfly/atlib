
from ConfigParser import RawConfigParser as rcp 
 
if __name__ == "__main__": 
    cfg = rcp() 
    cfg.add_section("Info") 
    cfg.set("Info", "ImagePath", "f:/whu") 
    cfg.set("Info", "foo", "cd's information") 
    cfg.write(open("f:/Whu/try.ini","w")) 

#www.iplaypy.com 
#[Info] 
#imagepath = f:/whu 
#foo = cd's information 