"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account



    
# Define a function for the Savings Account
def create_savings_account(selbalance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    
    # Create an instance of the `Account` class and pass in the balance and interest parameters
    account = Account(balance, interest)
    
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    interest = 0
    account.set_balance(balance)

    # Calculate interest earned;
    # ADD YOUR CODE HERE
    interest = float((balance * interest_rate * months)/100)
    
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = balance + interest
    
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    account.set_balance(updated_balance)
    
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    account.set_interest(interest)

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    return updated_balance, interest


