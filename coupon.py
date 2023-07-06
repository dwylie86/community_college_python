# David Wylie
# PA 6
# This program determines the discount you'll get on your groceries.

def apply_coupon(amount):
    """Calculates the amount of discount on groceries.

    	Keyword argument:
    	amount -- the amount to base coupon discount on
    """
    discount = 0.0
    if amount <= 0:
        print("You entered an invalid cost of groceries.")
        exit()
    elif amount > 210:  # More than $210
        discount = 0.14
    elif 150 < amount <= 210:  # More than $150 to $210
        discount = 0.12
    elif 60 < amount <= 150:  # More than $60 to $150
        discount = 0.10
    elif 10 <= amount <= 60:  # From $10 to $60
        discount = 0.08
    elif amount < 10:  # Less than $10
        discount = 0.0
    return discount


# Get cost of groceries from user input
groceries_cost = float(input("Enter the cost of your groceries: "))
coupon = apply_coupon(groceries_cost)

# Print the results
print(f"""Your coupon percentage is: {coupon * 100:.0f}%
You win a discount of ${groceries_cost * coupon:,.2f}.""")
