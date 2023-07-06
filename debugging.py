# David Wylie
# DA_1

# This program reads an unspecified number of integers, determines how many even 
# and odd values have been read, and displays the count for the number of even and
# odd integers. If a 0 or negative number is initially inputted it displays the following
# message: No numbers were entered except a zero or a negative number.
# The program ends when a zero or a negative integer is inputted.

# Prompt user to enter an integer
number = int(input("Enter an integer, the input ends if a zero or a a negative number is entered: "))  # Corrected int

count_even = 0
count_odd = 0  # Changed variable to zero

# While loop to read and count numbers
while number > 0:  # Changed operator
    if number % 2 == 0:  # Changed modulus to 2
        count_even += 1
    else:
        count_odd += 1

# Prompt user to enter another integer
    number = int(input("Enter an integer, the input ends if a zero or a a negative number is entered: "))  # Indented

# Display output
if count_even + count_odd == 0:  # Corrected condition
    print("No numbers were entered except a zero or a negative number")
else:
    print(f"The number of even numbers is {count_even}")
    print(f"The number of odd numbers is {count_odd}")
