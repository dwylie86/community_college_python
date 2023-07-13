# David Wylie
# PA 7
# This program generates and analyzes a list of 20 random integers between 1 and 100

# List generation using list comprehension
import random
random_list = [random.randint(1, 100) for num in range(20)]

# Print the analysis using Python standard functions. Integer division is used to calculate the average.
print(f"""This list contains: {random_list}
The lowest random number is: {min(random_list)}
The highest random number is: {max(random_list)}
The total of the random numbers is: {sum(random_list):,}
The average (rounded down) of the random numbers is: {sum(random_list) // len(random_list)} 

Random numbers > 50""")

# To print integers that are over 50, next to each other on the same line with a space in between.
for num in random_list:
    if num > 50:
        print(f"{num} ", end="")
