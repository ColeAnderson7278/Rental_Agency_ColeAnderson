import disk
import core


def customer_choices(inventory):
    while True:
        choice = input(
            '\n1) Rent\n2) Return\n3) Exit\nWhat can I help you with: ')
        if choice == '1':
            renting(inventory)
        if choice == '2':
            returning()
        if choice == '3':
            exit()


def employee_choices(inventory):
    while True:
        choice = input(
            '\n1) Check Stock\n2) Transactions\n3) Revenue\n4) Exit\nWhat can I help you with: '
        )
        if choice == '1':
            check_stock()
        if choice == '2':
            transaction_history()
        if choice == '3':
            total_revenue()
        if choice == '4':
            exit()
        else:
            print('Invalid Response. Please enter a valid number.')


def renting(inventory):
    print(f'''
1) {inventory['bikes']['name']} - Rent Price: ${inventory['bikes']['rent price']} Replacement Price: ${inventory['bikes']['replacement price']} In-Stock: {inventory['bikes']['amount']}

2) {inventory['skateboards']['name']} - Rent Price: ${inventory['skateboards']['rent price']} Replacement Price: ${inventory['skateboards']['replacement price']} In-Stock: {inventory['skateboards']['amount']}

3) {inventory['scooters']['name']} - Rent Price: ${inventory['scooters']['rent price']} Replacement Price: ${inventory['scooters']['replacement price']} In-Stock: {inventory['scooters']['amount']}

4) Exit 
    ''')
    while True:
        choice = input('What would you like to rent: ')
        if choice == '1':
            if inventory['bikes']['amount'] <= 0:
                print('Sorry, this item is not in stock.')
            else:
                inventory = core.rent_item(inventory, 'bikes')
                return inventory
        if choice == '2':
            inventory = core.rent_item(inventory, 'skateboards')
            return inventory
        if choice == '3':
            core.rent_item(inventory, 'scooters')
        if choice == '4':
            exit()
        else:
            print('\nPlease choose a valid option.\n')


def main():
    inventory = core.create_inventory(disk.read_file('inventory.txt'))
    while True:
        user = input(
            'Welcome to the Rental Store\n1) Customer\n2) Employee\n3) Exit\nWho may I help today: '
        )
        if user == '1':
            customer_choices(inventory)
        elif user == '2':
            customer_choices(inventory)
        elif user == '3':
            exit()


if __name__ == '__main__':
    main()
