
start_1=1
start_2=1
maximum_fib=4000000

def fibonacci_evens(prev1,prev2,maximum):
	even_sums=0
	theSum = prev1 + prev2
	while theSum < maximum :
		if (theSum %2 == 0):
			even_sums += theSum
		prev1 = prev2
		prev2 = theSum
		theSum = prev1+prev2
	print(even_sums)



fibonacci_evens(start_1,start_2,maximum_fib)
	
