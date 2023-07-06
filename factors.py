def find_factors(integer):
	"""Loops and finds all factors of the integer entered
	
	Keyword argument:
		integer -- the number to find factors for, also how many loop iterations
	"""
	for i in range(integer):
		if integer % (i+1) == 0:
			print(f"{i+1} is a factor of {integer}")
	return integer

number = int(input("Enter a positive integer: "))
find_factors(number)

