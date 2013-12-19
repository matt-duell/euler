import math

####Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
####If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
####
####For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
####The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
####
####Evaluate the sum of all the amicable numbers under 10000.


#gets the divisors of n, returns their sum
def divisorsSum(n):

    limit = math.floor(math.sqrt(n)) #won't need to go past sqrt(n)
    # 1 is trivially a divisor, so start there
    curDivisorsSum = 1; 
    # Start our division at 2
    for i in range(2,limit):
        if n%i==0:            
            #1/n divides evenly (because i%n==0) so adding to the running count
            # both the divisor and the quotient, since both are divisors of n
            curDivisorsSum += n/i
            curDivisorsSum += i
            
    return curDivisorsSum
    

amicableSum =0
alreadyProcessed = set()

for i in range(2,10000):    
    if i in alreadyProcessed:
        continue
    
    a = divisorsSum(i)
    b = divisorsSum(a)
    
    #i and a are amicable numbers if d(i)=a and d(a)=b=i
    if i == b:
        if i != a: #condition that it can't evaluate to itself
            print("Found amicable i=",i," b=",b," a=",a)
        
            amicableSum += (i+a)
            alreadyProcessed.add(a) #since it is amicable, we don't want to count it again
        
    
print("sum of all amicable numbers < 10000 = ",amicableSum)





