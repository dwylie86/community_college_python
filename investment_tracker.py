# This program takes user inputs and displays the yearly ROI.

def invest(amount, rate, years):
	""" This calculates and prints the annual rate of return and growth.
		Returns the return on investment (roi), the total amount of interest accrued.  
		
		Keyword Arguments:
			amount -- The amount the annual rate of return will be applied to
			rate -- The annual rate of return applied per year on the amount 
			years -- The number of years the amount will have a rate of return applied
	"""
	roi = 0
	
	for i in range(years):
		roi += amount * rate 
		amount += amount * rate
		print(f"Year {i+1}: ${amount:,.2f}")
	
	return roi

# Gather inputs from user		
initial_amount = float(input("Enter the initial investment amount: "))
return_rate = float(input("Enter annual rate of return percent: "))
investment_years = int(input("Enter the amount of years to invest: "))
print()	

# Run invest function
return_on_investment = invest(initial_amount,return_rate,investment_years)

# Print return on investment
print(f"\nYour investment earned ${return_on_investment:,.2f} over {investment_years} years.")
