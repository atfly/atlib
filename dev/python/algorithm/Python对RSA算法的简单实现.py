
#!/usr/bin/env python  
#-*-coding: utf-8-*-  
 
import math  

def isPrime(number):  
    i=2  
    sqrtNumber=int(math.sqrt(number))  
    for i in range(2, sqrtNumber+1):  
        if number%i == 0:  
            return False  
        i = i+1  
    return True  
  
if __name__=="__main__":  
    print "*"*77  
    Flag = False  

    while Flag == False:  
        p = int(raw_input("Please input a prime(P): "))  
        Flag = isPrime(p)  
        if Flag == False:  
            print "What you input is not a prime!"  
    print "The P is: ", p  
      
    Flag = False  

    while Flag == False:  
        q = int(raw_input("Please input a prime(Q): "))  
        if p == q:  
            continue  
        Flag = isPrime(q)  
        if Flag == False:  
            print "What you input is not a prime!"  
    print "The Q is: ", q  
    n = p*q  

    print "The N is: ", n  
    t = (p-1)*(q-1)  

    print "The T is: ", t  
      
    print "*"*77  

    Flag = False  

    while Flag == False:  
        e = int(raw_input("Please input a number(E): "))  
        if (e<1 or e>t):  
            continue  
        d=0  
        while (((e*d)%t) != 1):  
            d+=1  
        Flag = True  
    print "The E is: ", e  
    print "The D is: ", d  
    print "The Public Key(E, N) is:", e, n  
    print "The Private Key(D, N) is:", d, n  
  
#www.iplaypy.com

    print "*"*77  
    Flag = False  

    while Flag == False:  
        plainText = int(raw_input("Please input a plaintext: "))  
        if (plainText < n):  
            Flag = True  
    print "The plaintext is: ", plainText  
    print "Encrypt"+"."*7  

    cipherText = (plainText**e)%n   

    print "cipherText is: ", cipherText   
    print "Decrypt"+"."*7  
    plain = (cipherText**d)%n  
    print "The plain is: ", plain  
  
    print "*"*77  

    if plainText == plain:  
        print "RSA Test success."  
    else:  
        print "RSA Test unsuccess!" 