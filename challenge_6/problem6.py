#The sum of the squares of the first ten natural numbers is,
#
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#
#(1 + 2 + ... + 10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.



#Square of sum section
#
# Quick one liner observation that the sum of 1 to 100 is (1 + 100 = 101) + (2+99 = 101) + ... etc 50 times.
# Can be calculated in one line
sqSum = (101*50)**2

sumOfSquare = 0;

#one line using summation function
sumOfSquare = sum( i**2 for i in range(1,101))

#for i in range(1,101):
	#sumOfSquare += i**2

print(sqSum-sumOfSquare)
