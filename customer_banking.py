# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    #Define a line used in printing output
    line = "-" * 50

    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    print(line)
    print("""Hello there!!
We are going to create a savings account for you.
All you need to do is enter the
    beginning balance for the savings account, 
    the interest rate as a percentage, 
    and the number of months for the savings account to mature""")
    print(line)
    print()

    savings_balance = float(input("Please enter the starting balance: $"))
    savings_interest = float(input("Now, enter the interest rate for the account as a percentage: ").strip('%'))
    savings_maturity = int(input("Finally, enter the number of months it will take the account to mature: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    print(savings_balance, savings_interest, savings_maturity)
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print()
    print(line)
    print(f"The interest you will earn will be ${interest_earned: ,.2f}")
    print(f"Your new balance for the savings account will be ${updated_savings_balance: ,.2f}")
    print(line)
    print()
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    print(line)
    print("""We are now going to create a CD account for you.
All you need to do is enter the
    beginning balance for the CD account, 
    the interest rate as a percentage, 
    and the number of months for the savings account to mature""")
    print(line)
    print()

    cd_balance = float(input("Please enter the starting balance: $"))
    cd_interest = float(input("Now, enter the interest rate for the account as a percentage: ").strip('%'))
    cd_maturity = int(input("Finally, enter the number of months it will take the account to mature: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print()
    print(line)
    print(f"The interest you will earn will be ${interest_earned: ,.2f}")
    print(f"Your new balance for the savings account will be ${updated_cd_balance: ,.2f}")
    print(line)
    print()

if __name__ == "__main__":
    # Call the main function.
    main()
