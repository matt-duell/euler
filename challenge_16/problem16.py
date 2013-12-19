#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 2^1000?

exp = 2**1000

strExp = str(exp)

digitSum = sum( int(strExp[i]) for i in range(len(strExp)))

print(digitSum)

#another idea suggested in the thread of project euler
#iterates through the number directly, apply this with previous summation style
# and get the below
digitSum = sum( int(n) for n in str(2**1000))
print (digitSum)
