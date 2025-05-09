import database
import data_analysis
import data_cleaning

import sys
import csv
import random
import pandas as pd
from faker import Faker
from datetime import datetime




USER_PROMPT = """

Personal-Finance Tracker

Choose an option:

1) Insert Transactions
2) Export data to csv file
3) Get details about data using pandas
4) Data Cleaning
5) Exit

Your choice: 

"""

def main():
    connection = database.connect()
    database.create_transaction_table(connection)
    fake = Faker()

    while True:
        try:
            user_input = int(input(USER_PROMPT))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 6")
            continue

        if user_input == 1:
            handle_transaction_insertion(connection, fake)
        elif user_input == 2:
            handle_data_export(connection)
        elif user_input == 3:
            handle_data_insights()
        elif user_input == 4:
            trans_data = data_analysis.csv_to_dataframe()
            data_cleaning.clean_transactions_data(trans_data)
        elif user_input == 5:
            sys.exit()
        else:
            print(f"Invalid user input. Please enter valid input.")

def handle_transaction_insertion(connection, fake):
    insertion_input = input("""
        Choose an option:

        a) Single transaction insertion
        b) Multiple transaction insertion

        Your choice: 
    """)
    if insertion_input == 'a':
        data = generate_transaction_data(connection, fake, 1)
        database.insert_transaction(connection, data)
    elif insertion_input == 'b':
        data = generate_transaction_data(connection, fake, 1000)
        database.insert_many_transactions(connection, data)
    else:
        print("Please enter valid option.")

def handle_data_export(connection):
    transactions = database.see_all_data(connection)
    export_to_csv_file = input("Do you want see the data after exporting data to csv file (yes/no): ").strip().lower()

    if export_to_csv_file == 'yes':
        file_name = input("Enter the file name to export data from sqlite table to csv file: ") 
        export_to_csv(file_name, transactions)
        print(f"Data Exported to {file_name}")
    elif export_to_csv_file == 'no':
        for transaction in transactions:
            print(transaction)
    else:
        print("Please enter valid input.")

def handle_data_insights():
    trans_data = data_analysis.csv_to_dataframe()
    sample_trans_data = data_analysis.sample_data(trans_data)
    print("Sample Transaction records (first 10 records): ", sample_trans_data, sep="\n")
    print()
    print("Information about transactions data: ")
    data_analysis.information_about_data(trans_data)

        

        
def export_to_csv(file_name, transactions):
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['id', 'date', 'type', 'category', 'amount', 'payment_method', 'recurring'])
        csv_writer.writerows(transactions)
    

def generate_transaction_data(connection, fake, number_of_transactions):
    start_year = int(input("Enter start year for data: "))
    end_year = int(input("Enter end year for data: "))

    transactions_data = [(
        get_fake_date(fake, start_year, end_year), 
        get_random_type(), 
        get_random_category(), 
        get_fake_amount(fake), 
        get_random_paymentmethod(), 
        get_random_recurring()
        ) for _ in range(number_of_transactions)]
    return transactions_data

def get_fake_date(fake, start_year, end_year):
    return fake.date_between(start_date = datetime(start_year, 1, 1), end_date = datetime(end_year, 1, 1))

def get_random_type():
    return random.choice(('Income', 'Expense'))

def get_random_category():
    return random.choice(('Groceries', 'Dining Out', 'Rent/Mortgage', 
        'Utilities', 'Internet', 'Phone', 'Transportation', 
        'Insurance', 'Healthcare', 'Education', 'Childcare', 
        'Entertainment', 'Shopping', 'Travel', 'Debt Repayment', 
        'Subscriptions', 'Gifts/Donations'))

def get_fake_amount(fake):
    return fake.pyfloat(positive=True, max_value=5000)

def get_random_paymentmethod():
    return random.choice(('Cash', 'Credit Card', 'Debit Card', 'Bank Transfer', 'Other'))

def get_random_recurring():
    return random.choice((0, 1))

if __name__ == "__main__":
    main()
