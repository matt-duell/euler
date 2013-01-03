#imports
from datetime import date

#variables
remainder_3=0
remainder_5=0
total=0
num_digits=1000


#add numbers that are evenly divisible by 3 or 5
for x in range(num_digits):
	remainder_3= x % 3
	remainder_5=x%5
	if remainder_3 == 0 or remainder_5==0:
		total= total + x
	

print (total)


