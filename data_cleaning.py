import pandas as pd
import csv



def clean_transactions_data(data):

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Normalize date format
    data['date'] = pd.to_datetime(data['date'], errors='coerce').dt.strftime('%Y-%m-%d')

    # Drop rows with invalid dates
    data = data[data['date'].notnull()]

    # Ensure amount is a non-negative float
    data['amount'] = pd.to_numeric(data['amount'], errors='coerce')
    data = data[data['amount'] >= 0]

    # Convert 'type', 'category', 'payment_method' to category type
    text_cols = ['type', 'category', 'payment_method']
    for col in text_cols:
        data[col] = data[col].astype('category')
    
    data.to_csv('cleaned_transaction_data.csv', index=False)
    



