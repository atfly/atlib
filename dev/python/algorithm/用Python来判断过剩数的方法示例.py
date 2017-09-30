
#Checks if a number is abundant or not
#An abundant number is the number of which sum of factors(including itself) is greater than twice the number
#www.iplaypy.com

def abundant(n):
    sum_factors=0
    for i in range(1,n+1):
        if n%i==0:      #finds out the factors
            f=i
            sum_factors += f            
    if sum_factors>2*n:                #condition for abundant number
        print "This is an Abundant Number!"
    else:
        print "This is not an Abundant Number!"
