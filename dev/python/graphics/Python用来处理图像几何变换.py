
import Image

try:
    im=Image.open('test.jpg')
    #out = im.resize((128, 128)) #改变大小
    #out = im.rotate(45) #45°旋转
    #out = im.transpose(Image.FLIP_LEFT_RIGHT) #水平翻转
    #out = im.transpose(Image.FLIP_TOP_BOTTOM) #垂直翻转
    #out = im.transpose(Image.ROTATE_90) # 90
    #out = im.transpose(Image.ROTATE_180) #180°顺时针翻转
    out = im.transpose(Image.ROTATE_270) #270°顺时针翻转
    out.save('test2.jpg')
    
except IOError:
    
    print 'No File!'
