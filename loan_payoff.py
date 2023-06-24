# David Wylie
# PA 5
# This program calculates how many payments it will take to pay off a loan.

def calculate_payments(balance, payment_amount, interest_rate):
    """Calculates the number of payments it will take to pay off a loan with interest.

        Keyword arguments:
        balance -- the amount owed on the loan
        payment_amount -- the amount to be paid and applied to the starting balance per payment
        interest_rate -- interest that will be applied to the loan balance initially and before each payment
    """
    payment_number = 0  # Iteration counter for while loop
    starting_balance = balance  # Variable to check for infinite loop

    # Conditional check for infinite loop aka payment not high enough to cover interest
    if starting_balance <= (balance + (balance * interest_rate)) - payment_amount:
        print("This loan cannot be paid off with this payment amount and interest rate.")
        exit()
    # Loop to determine how many payments it will take to pay off loan
    else:
        while balance >= 0:
            balance = (balance + (balance * interest_rate)) - payment_amount
            payment_number += 1
    return payment_number


# Declaring variables and assigning user inputs to them
loan_balance = float(input("Enter the loan balance: "))
loan_payment = float(input("Enter the loan payment: "))
loan_interest = float(input("Enter the interest rate: "))

# Run the calculate_payments function to calculate number of payments based on this user input then print the result
number_of_payments = calculate_payments(loan_balance, loan_payment, loan_interest)
print(f"The number of payments required is: {number_of_payments}")
