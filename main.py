import database
import sys
from faker import Faker
import random

USER_PROMPT = """

Personal-Finance Tracker

Choose an option:

1) Add a new Transaction
2) Add multiple new transactions
3) Get total amount monthly
4) Get total amount for given type
5) Exit

Your choice: 

"""

def main():
    connection = database.connect()
    database.create_transaction_table(connection)
    fake = Faker()

    while True:
        user_input = int(input(USER_PROMPT))

        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            pass
        elif user_input == 5:
            sys.exit()
        else:
            print(f"Invalid user input. Please enter valid input.")

def insert_transaction_data(connection, fake):
    start_year = int(input("Enter start year for data: "))
    end_year = int(input("Enter end year for data: "))

    transactions_data = [(get_fake_date(fake, start_year, end_year), get_random_type(), get_random_category(), get_fake_amount(fake), get_random_paymentmethod(), get_random_recurring())]

def get_fake_date(fake, start_year, end_year):
    return fake.date_between(start_date = datetime(start_year, 1, 1), end_date = datetime(end_year, 1, 1))

def get_random_type():
    return random.choice(('Income', 'Expense'))

def get_random_category():
    return random.choice(('Groceries', 'Dining Out', 'Rent/Mortgage', 'Utilities', 'Internet', 'Phone', 'Transportation', 'Insurance', 'Healthcare', 'Education', 'Childcare', 'Entertainment', 'Shopping', 'Travel', 'Debt Repayment', 'Subscriptions', 'Gifts/Donations'))

def get_fake_amount(fake):
    return fake.pyfloat(positive=True, max_value=5000)

def get_random_paymentmethod():
    return random.choice(('Cash', 'Credit Card', 'Debit Card', 'Bank Transfer', 'Other'))

def get_random_recurring():
    return random.choice((0, 1))

if __name__ == "__main__":
    main()
