import pandas as pd

def csv_to_dataframe():
    file_name = input("Enter csv file name: ")
    data = pd.read_csv(file_name)
    return data

def sample_data(data):
    return data.head(10)

def information_about_data(data):
    print(data.info())
