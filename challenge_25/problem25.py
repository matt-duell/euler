import math
####The Fibonacci sequence is defined by the recurrence relation:
####
####Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
####Hence the first 12 terms will be:
####
####F1 = 1
####F2 = 1
####F3 = 2
####F4 = 3
####F5 = 5
####F6 = 8
####F7 = 13
####F8 = 21
####F9 = 34
####F10 = 55
####F11 = 89
####F12 = 144
####The 12th term, F12, is the first term to contain three digits.
####
####What is the first term in the Fibonacci sequence to contain 1000 digits?



def fib(i):
    #needs to be calculated    
    if lookup[i] ==0:    
        lookup[i] = fib(i-1) + fib(i-2)
        lookup.append(0) #add for the next one
    
    #calculated by now, either from recursion or already in lookup
    return lookup[i]



lookup = [0]*4
lookup[1]=1
lookup[2]=1


numDigits = 0
i = 0
while numDigits <1000:    
    i=i+1    
    #floor(log10(x))+1 = number of digits in the number x
    #floor is just to get rid of the decimal portion, the important part is log10(x) +1
    numDigits = math.floor(math.log10(fib(i)))+1
    
    
    
print("i = ",i)
print("fib(i) = ",fib(i))
print("numDigits = ",numDigits)

#could've solved algebraicly using the nth fib number = phi^n / sqrt(5)

















