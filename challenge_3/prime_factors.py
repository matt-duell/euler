import math
from sets import Set


def approach1(target):

	currentNumber = 3;
	#Cut the numbers we have to search through in half, there won't be any over half way that are prime factors.
	cur_max_pos_factor= math.floor(target /2)

	#start main processing
	while currentNumber < cur_max_pos_factor:
		#first check if it is a factor THEN check if it is prime
		modulus = target % currentNumber
		if modulus == 0: #is a factor
			if DEBUG==True:
				print str(currentNumber) + " is a factor. Checking primeness";
			#check if it is prime
			if isPrime(currentNumber):
			#insert if it is 
				prime_factors.add(currentNumber);

		#resize the cur_max_pos_factor, since the maximum possible is now lowered, I want to save time by not
		# checking factors that I know won't match.
		if DEBUG==True:
			print"Factor found:" + str(currentNumber);
			print"Resizing ceiling factor to check. Old value: " + str(cur_max_pos_factor);

		cur_max_pos_factor = math.floor(target/currentNumber);

		if DEBUG==True:
			print"Resizing ceiling factor to check. New value: " + str(cur_max_pos_factor);
		
		#increment by 2, to avoid unneccesary processessing of non-prime evens.
		currentNumber +=2;


def approach2(target):

	#Cut the numbers we have to search through in half, there won't be any over half way that are prime factors.
	cur_max_pos_factor= math.floor(target /2)
	foundGreatestPrimeFactor=False
	currentNumber=cur_max_pos_factor
	#ensure we are starting at an odd number
	if cur_max_pos_factor %2 == 0:
		currentNumber -=1

	while foundGreatestPrimeFactor==False:
		#first check if it is a factor
		#THEN check if it is prime
		modulus = target % currentNumber
		if modulus == 0: #is a factor
			if DEBUG==True:
				print str(currentNumber) + " is a factor. Checking primeness";
	
			#check if it is prime now
			if isPrime(currentNumber):
				#insert if it is 
				foundGreatestPrimeFactor=True
				prime_factors.add(currentNumber);
	
		#resize the cur_max_pos_factor, since the maximum possible is now lowered, I want to save time by not
		# checking factors that I know won't match.
		if DEBUG==True:
			print"Resizing ceiling factor to check. Old value: " + str(cur_max_pos_factor);
	
		cur_max_pos_factor = math.floor(target/currentNumber);
		
		if DEBUG==True:
			print"Resizing ceiling factor to check. New value: " + str(cur_max_pos_factor);
		
		#decrement by 2, to avoid unneccesary processessing of non-prime evens.
		#trying to go backwards now
		currentNumber=cur_max_pos_factor

		#ensure we are starting at an odd number
		if cur_max_pos_factor %2 == 0:
			currentNumber -=1



def isPrime(number):
	return brute_force_isPrime(number);


#brute force method	
def brute_force_isPrime(number):

	if (number == 1):
		return False;
	if (number == 2): 
		return True;
	if(number > 2):
	#only consider the bottom half of the numbers to start. 
	#if it doesn't have a factor in the first half, it won't have one in the second half.
	# readjust the upper limit as we find which numbers are not factors, and we get
	# more assured that the number is a prime.
	# i.e. if 3 is not a factor, then if there ARE factors then it will be in the first
	#	third section of the numbers. if there are factors it will be with numbers
	#	in that new segment. 
	#	This repeats as we go up until we get smaller and smaller windows of opportunity
	#	to find a factor, until we don't find one anymore, at which point we have 
	#	concluded it is a prime
	#step by 2 (avoid evens)
		print "Checking primeness of "+str(number)
		limit = number/2
		i = 3
		while i < limit:
			if number %i == 0:
				return False
			else:
				limit = number/i
			i+=2
		
	return True;



#### Main below

target=600851475143
DEBUG=False

#cur_max_pos_factor= math.floor(target /2)

# our set of prime factors
prime_factors = Set();
print "Target=" + str(target)

approach1(target)
#approach2(target) # did not flesh out approach 2 enough, is too slow.

print "The prime factors of the number: " + str(target) + " is/are: " + str(prime_factors);




