import sqlite3 # Built-in module to interact with SQLite database

# SQL Statements

CREATE_TABLE_TRANSACTIONS = """
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('Income', 'Expense')),
    category TEXT NOT NULL CHECK(category IN (
        'Groceries', 'Dining Out', 'Rent/Mortgage', 'Utilities', 'Internet', 
        'Phone', 'Transportation', 'Insurance', 'Healthcare', 'Education', 
        'Childcare', 'Entertainment', 'Shopping', 'Travel', 'Debt Repayment', 
        'Subscriptions', 'Gifts/Donations'
        )),
    amount REAL NOT NULL CHECK(amount>=0),
    payment_method TEXT NOT NULL CHECK(payment_method IN (
        'Cash', 'Credit Card', 'Debit Card', 'Bank Transfer', 'Other'
        )),
    recurring INTEGER NOT NULL DEFAULT 0 CHECK(recurring IN (0, 1))
);
"""

INSERT_TRANSACTION = """
INSERT INTO transactions (date, type, category, amount, payment_method, recurring)
VALUES (?, ?, ?, ?, ?, ?);
"""

FETCH_ALL_TRANSACTIONS = """
SELECT * FROM transactions;
"""

FETCH_TRANSACTIONS_BY_SORTED_DATE ="""
SELECT * FROM transactions
ORDER BY date;
"""


FILTER_TRANSACTIONS_TO_ANALYSE_MONTHLY_AMOUNT = """
SELECT STRFTIME('%m-%Y', date) AS transaction_month_year, type, category, ROUND(SUM(amount), 2) AS total_amount
FROM transactions
GROUP BY transaction_month_year, type, category;
"""

FILTER_TRANSACTIONS_AMOUNT_FOR_GIVEN_TYPE = """
SELECT type, ROUND(SUM(amount), 2) AS total_amount
FROM transactions
WHERE type = ?;
"""

# ----------------------------------------
# Database Functions
# ----------------------------------------

# Connect to the database (creates database if it doesn't exist)
def connect():
    return sqlite3.connect("finance.db")

# Create transactions table 
def create_transaction_table(connection):
    with connection:
        connection.execute(CREATE_TABLE_TRANSACTIONS)

def insert_transaction(connection, transaction_data):
    with connection:
        connection.execute(INSERT_TRANSACTION, transaction_data)

def insert_many_transactions(connection, transaction_data):
    with connection:
        connection.executemany(INSERT_TRANSACTION, transaction_data)

def see_all_data(connection):
    with connection:
        return connection.execute(FETCH_ALL_TRANSACTIONS).fetchall()

def analyze_monthly_amount(connection):
    with connection:
        return connection.execute(FILTER_TRANSACTIONS_TO_ANALYSE_MONTHLY_AMOUNT).fetchall()

def analyze_total_amount_by_type(connection, type1):
    with connection:
        return connection.execute(FILTER_TRANSACTIONS_AMOUNT_FOR_GIVEN_TYPE, (type1,)).fetchall()



