
  
import xml.parsers.expat  
  
# 控制打印缩进  
level = 0  
  
# 获取某节点名称及属性值集合  
def start_element(name, attrs):  
    global level  

    print '  '*level, 'Start element:', name, attrs  
    level = level + 1  
  
# 获取某节点结束名称  
def end_element(name):  
    global level  
    level = level - 1  

    print '  '*level, 'End element:', name  
      
# 获取某节点中间的值  
def char_data(data):  
    if(data == '\n'):  
        return  

    if(data.isspace()):  
        return  

    global level  
 
   print '  '*level, 'Character data:', data  
  
#www.iplaypy.com
p = xml.parsers.expat.ParserCreate()  
  
p.StartElementHandler = start_element  
p.EndElementHandler = end_element  
p.CharacterDataHandler = char_data  
p.returns_unicode = False  
  
f = file('sample.xml')  

p.ParseFile(f)  

f.close()
