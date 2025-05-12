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

    
    data.to_csv('cleaned_transaction_data.csv', index=False)

    dtypes = {
        'id': 'int64',
        'type': 'category',
        'category_type': 'category',
        'amount': 'float64',
        'payment_method': 'category',
        'recurring': 'category'
    }

    df_cleaned = pd.read_csv('cleaned_transaction_data.csv', dtype=dtypes, parse_dates=['date'])

    cols = ['type', 'category_type', 'payment_method', 'recurring']

    for col in cols:
        df_cleaned[col] = df_cleaned[col].astype('category')
    
    return df_cleaned
    



