# Customer Banking System

The `customer_banking.py` script is part of a customer banking system that allows users to calculate and track interest earned on savings and CD (Certificate of Deposit) accounts. By running this application, users can:

- Enter the initial balance, interest rate, and maturity period for both savings and CD accounts.
- Calculate the interest earned for each account type.
- View interest earned and updated balance after a specified number of months.

This script interacts with additional modules like `Account.py`, `cd_account.py`, and `savings_account.py` to implement the banking system functionality.

---

## Features

- Prompts the user to create both a savings account and a CD account.
- Calculates interest earned based on user input for balance, interest rate, and maturity period.
- Displays the interest earned and new balances for both accounts after interest is applied.

---

## How to Run

1. Ensure you have **Python 3.9 or later** installed on your system.
2. Clone or download this repository to your computer.
3. Open a terminal, navigate to the folder containing `customer_banking.py`, and run the script:

   ```bash
   python customer_banking.py
   ```

---

## Example Output

```plaintext
--------------------------------------------------
Hello there!!
We are going to create a savings account for you.
All you need to do is enter the
    beginning balance for the savings account,
    the interest rate as a percentage,
    and the number of months for the savings account to mature
--------------------------------------------------

Please enter the starting balance: $15000.00
Now, enter the interest rate for the account as a percentage: 1.5%
Finally, enter the number of months it will take the account to mature: 24

--------------------------------------------------
The interest you will earn will be $450.00
Your new balance for the savings account will be $15,450.00
--------------------------------------------------

--------------------------------------------------
We are now going to create a CD account for you.
All you need to do is enter the
    beginning balance for the CD account,
    the interest rate as a percentage,
    and the number of months for the savings account to mature
--------------------------------------------------

Please enter the starting balance: $5000
Now, enter the interest rate for the account as a percentage: 4.5
Finally, enter the number of months it will take the account to mature: 12

--------------------------------------------------
The interest you will earn will be $225.00
Your new balance for the savings account will be $5,225.00
--------------------------------------------------
```

---

## Prerequisites

- Python **3.9 or later**.

---

## Tests

Test manually.

---

## Notes

Additional functionality was added to accommodate if the user enters a percent sign when prompted for the interest rate and still have the program work.

