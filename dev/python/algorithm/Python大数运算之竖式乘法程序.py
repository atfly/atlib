
                   123456709
*        1234567890987654321
----------------------------
                   123456709
                  246913418 
                 370370127  
                493826836   
               617283545    
              740740254     
             864196963      
            987653672       
          1111110381        
          000000000         
        1111110381          
        987653672           
       864196963            
      740740254             
     617283545              
    493826836               
   370370127                
  246913418                 
 123456709                  
----------------------------
152415688858406562100289589
Elapsed time: 0.10666831 seconds


         1234567890987654321
*                  123456709
----------------------------
        11111111018888888889
        0000000000000000000 
       8641975236913580247  
      7407407345925925926   
     6172839454938271605    
    4938271563950617284     
   3703703672962962963      
  2469135781975308642       
 1234567890987654321        
----------------------------
152415688858406562100289589
Elapsed time: 0.05573613 seconds

#--------www.iplaypy.com-------------

#! /urs/bin/env python

from mytictoc import tic, toc

# big intiger multiplication
def bigmul(a,b):
    sa = str(a)
    sb = str(b)
    resultline = ' '*(len(sa)+len(sb))

    #   a
    # * b
    print
    print resultline[:-len(sa)]+sa
    print '*'+resultline[:-len(sb)-1]+sb

    # ---
    print '-'*(len(sa)+len(sb))

    #   ###
    #  ###
    # ###
    result_list = []
    cursp = 0
    for db in sb[::-1]:
        if int(db)==0:
            result = '0'*len(sa)
        else:
            result = ''
            carrier = 0
            for da in sa[::-1]:
                #print db,da
                mr = int(db)*int(da)+carrier
                carrier = mr/10
                result += str(mr%10)
            if carrier!=0:
                result += str(carrier)
        result = result[::-1]+' '*cursp
        cursp += 1
        result_list.append(resultline[:-len(result)]+result)
        print result_list[-1]

    # ----
    print '-'*(len(sa)+len(sb))
    
    # result
    print str(sum([int(x.replace(' ','0')) for x in result_list])) 

# unit test
def main():
    a = 1234567890987654321
    b = 123456709

    tic()
    bigmul(b,a)
    toc()
    
    tic()
    bigmul(a,b)
    toc()

if __name__=='__main__':
    main()