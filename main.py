import database

USER_PROMPT = """

"""

def main():
    connection = database.connect()
    database.create_transaction_table(connection)

    while True:
        user_input = int(input("E"))


if __name__ == "__main__":
    main()
