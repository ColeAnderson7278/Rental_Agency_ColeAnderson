import disk
import core


def intro(inventory):
    while True:
        user = input(
            'Welcome to the Rental Store\n1) Customer\n2) Employee\nWho may I help today: '
        )
        if user == '1':
            while True:
                choice = input(
                    '\n1) Rent\n2) Return\nWhat can I help you with: ')
                if choice == '1':
                    renting(inventory)
                if choice == '2':
                    returning()
                else:
                    print('Invalid Response. Please enter a valid number.')

        if user == '2':
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
        else:
            print('Invalid Response. Please enter a valid number.')


def renting(inventory):
    print(f'''
1) {inventory['bikes']['name']} - Rent Price: ${inventory['bikes']['rent price']} Replacement Price: ${inventory['bikes']['replacement price']} In-Stock: {inventory['bikes']['amount']}

2) {inventory['skateboards']['name']} - Rent Price: ${inventory['skateboards']['rent price']} Replacement Price: ${inventory['skateboards']['replacement price']} In-Stock: {inventory['skateboards']['amount']}

3) {inventory['scooters']['name']} - Rent Price: ${inventory['scooters']['rent price']} Replacement Price: ${inventory['scooters']['replacement price']} In-Stock: {inventory['scooters']['amount']}
    ''')
    while True:
        choice = input('What would you like to rent: ')
        if choice == '1':
            core.rent_item(inventory, 'bikes')
        if choice == '2':
            core.rent_item(inventory, 'skateboards')
        if choice == '3':
            core.rent_item(inventory, 'scooters')
        else:
            print('Please choose a valid option.')


def main():
    inventory = core.create_inventory(disk.read_file('inventory.txt'))
    intro(inventory)


if __name__ == '__main__':
    main()
