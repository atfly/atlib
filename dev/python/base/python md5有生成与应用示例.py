
    #导入方法模块 
    import md5  
    import hashlib   
      
    src = 'this is a test.'   

    m1 = md5.new()   

    m1.update(src)   

    dest1 = m1.hexdigest()   
      
    m2 = hashlib.md5()   

    m2.update(src)   

    dest2 = m2.hexdigest()   
      
    print 'source string: ', src   

    print 'destination string1: ', dest1   

    print 'destination string2: ', dest2   

