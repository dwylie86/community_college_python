# David Wylie
# PA 4
# This program calculates the amount of tax from user input. Execise directions were for three separate functions.

# Set constant tax variables
CITY_TAX_RATE = 0.06125
COUNTY_TAX_RATE = 0.0475
STATE_TAX_RATE = 0.01625

# Create tax calclation functions
def calculate_city_tax(sales_amount):
	"""Calculates the amount of city sales tax.
	
		Keyword argument:
		sales_amount -- the amount to calculate tax based off
	"""
	tax_amount = round(sales_amount * CITY_TAX_RATE, 2)	
	return tax_amount
	
def calculate_county_tax(sales_amount):
	"""Calculates the amount of county sales tax.
	
		Keyword argument:
		sales_amount -- the amount to calculate tax based off
	"""
	tax_amount = round(sales_amount * COUNTY_TAX_RATE, 2)	
	return tax_amount
	
def calculate_state_tax(sales_amount):
	"""Calculates the amount of state sales tax.
	
		Keyword argument:
		sales_amount -- the amount to calculate tax based off
	"""
	tax_amount = round(sales_amount * STATE_TAX_RATE, 2)	
	return tax_amount
	
# It's PROGRAM time!
print("This program will calculater the amount of sales tax you owe.")
sales_amount = float(input("Enter sales amount: "))

city_tax = calculate_city_tax(sales_amount)
county_tax = calculate_county_tax(sales_amount)
state_tax = calculate_state_tax(sales_amount)

print(f"""
The city tax amount is: ${city_tax:.2f}
The county tax amount is: ${county_tax:.2f}
The state tax amount is: ${state_tax:.2f}
The total tax amount is: ${city_tax + county_tax + state_tax:.2f}
""")
