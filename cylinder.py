# David Wylie
# PA3

import math

# Define pi as a constant
PI = math.pi

# Ask for user inputs, intialize and assign float variables
print("This program will calculate the surface area and volume of a right cylinder: ")
radius = float(input("Enter the radius of the right cylinder: "))
height = float(input("Enter the height of the right cylinder: "))

# Calculate and print the result to four decimal places.
print(f"\nThe surface area of the right cylinder is {(2 * PI * radius * height) + (2 * PI * pow(radius,2)):.4f}")
print(f"The volume of the right cylinder is {PI * pow(radius,2) * height:.4f}")
