def intro():
    while True:
        user = input(
            'Welcome to the Rental Store\n1) Customer\n2) Employee\nWho may I help today: '
        )
        if user == '1':
            rent_return()
        if user == '2':
            employee_check()
        else:
            print('Invalid Response. Please enter a valid number.')


def rent_return():
    while True:
        choice = input('\n1) Rent\n2) Return\nWhat can I help you with: ')
        if choice == '1':
            renting()
        if choice == '2':
            returning()
        else:
            print('Invalid Response. Please enter a valid number.')


def renting():
    while True:
        choice = input('{}\nWhat would you like to rent: ')
        if choice in movies:
            check_out(choice)
        else:
            print('Please choose a valid option.')


def employee_check():
    while True:
        choice = input(
            '\n1) Check Stock\n2) Transactions\n3) Revenue\nWhat can I help you with: '
        )
        if choice == '1':
            check_stock()
        if choice == '2':
            transaction_history()
        if choice == '3':
            total_revenue()
        else:
            print('Invalid Response. Please enter a valid number.')


def main():
    intro()


if __name__ == '__main__':
    main()
