#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



#idea: don't have to check all numbers, since they are mostly multiples of each other
#
# divisible by 20 => divisible by 20's factors: 2,4,5,10
# divisible by 19 => is prime so no other numbers we can get away without checking
# divisible by 18 => divisible by 2,3,6,9
# divisible by 17 => is prime so no other numbers we can get away without checking
# divisible by 16 => divisible by 2,4,8
# divisible by 15 => divisible by 3,5
# divisible by 14 => divisible by 2,7
# divisible by 13 => is prime so no other numbers we can get away without checking
# divisible by 12 => divisible by 2,3,4,6
# divisible by 11 => is prime so no other numbers we can get away without checking

# so by checking 20,19,18,17,16,14,13,11 we can cover all the numbers from 1 through 20

# Iterate to MAX of 3724680960 to just set an upper limit. 
#(this number is 20*19*18*17*16*14*13*11 and so of course is evenly divisible)
# 
# Start at 40, since it's the next number up that is divisible by 20 evenly, good a starting point as any

lowestDivisible =0
#Go by steps of 20, anything less and it won't be divisible by 20 so there's no point in checking
for i in range(20,3724680960,20):
	if (i%20 == 0) and (i%19 == 0) and (i%18 == 0) and (i%17 == 0) and (i%16 == 0) and (i%14 == 0) and (i%13 == 0) and (i%11 == 0):
		lowestDivisible = i
		break

print(lowestDivisible)



#Smarter way would've just been to collect the prime factors of each of the numbers 11 - 20 (already done above)
# and multiply the biggest prime factors from the list and that would be the answer.
