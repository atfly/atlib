
#!/usr/bin/env python   

def calGCD(op1, op2):   

    if (op2==0): return op1   

    else: return calGCD(op2, op1%op2)   

def calGCDAndLCM(op1, op2):   

    gcd = calGCD(op1, op2)   

    lcm = op1/gcd*op2   

    return (gcd, lcm)   

#www.iplaypy.com
if __name__=='__main__':   
    op1 = int(raw_input('input the operands: '))   
    op2 = int(raw_input('input the operands: '))   
    result = calGCDAndLCM(op1, op2)   

    print result  
