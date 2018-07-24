def intro():
    while True:
        user = input(
            'Welcome to the Rental Store\n1) Customer\n2) Employee\nWho may I help today: '
        )
        if user == '1':
            rent_return()
        if user == '2':
            employee_check
        else:
            print('Invalid Response. Please enter a valid number.')


def rent_return():
    while True:
        choice = input('1) Rent\n2) Return\nWhat can I help you with: ')
        if choice == '1':
            renting()
        if choice == '2':
            returning()
        else:
            print('Invalid Response. Please enter a valid number.')


def employee_check():
    while True:
        choice = input(
            '1) Check Stock\n2) Transactions\n3) Revenue\nWhat can I help you with: '
        )
        if choice == '1':
            check_stock()
        if choice == '2':
            transaction_history()
        if choice == '3':
            total_revenue()
        else:
            print('Invalid Response. Please enter a valid number.')
