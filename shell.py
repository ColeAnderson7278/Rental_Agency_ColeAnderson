import disk
import core


def customer_choices(inventory):
    while True:
        choice = input(
            '\n1) Rent\n2) Return\n3) Exit\nWhat can I help you with: ')
        if choice == '1':
            renting(inventory)
        if choice == '2':
            returning(inventory)
        if choice == '3':
            exit()


def employee_choices(inventory, history):
    while True:
        choice = input(
            '\n1) Check Stock\n2) Transactions\n3) Revenue\n4) Exit\nWhat can I help you with: '
        )
        if choice == '1':
            check_stock(inventory)
        elif choice == '2':
            transaction_history(history)
        elif choice == '3':
            total_revenue(history)
        elif choice == '4':
            exit()
        else:
            print('Invalid Response. Please enter a valid number.')


def check_stock(inventory):
    print(f'''
---------------------------------------------------------------------------
{inventory['bike']['name']} -In-Stock: {inventory['bike']['amount']}

{inventory['skateboard']['name']} -In-Stock: {inventory['skateboard']['amount']}

{inventory['scooter']['name']} -In-Stock: {inventory['scooter']['amount']}

---------------------------------------------------------------------------
    ''')


def renting(inventory, history):
    print(f'''
---------------------------------------------------------------------------
{inventory['bike']['name']} - Rent Price: ${inventory['bike']['rent price']} Replacement Price: ${inventory['bike']['replacement price']} In-Stock: {inventory['bike']['amount']}

{inventory['skateboard']['name']} - Rent Price: ${inventory['skateboard']['rent price']} Replacement Price: ${inventory['skateboard']['replacement price']} In-Stock: {inventory['skateboard']['amount']}

{inventory['scooter']['name']} - Rent Price: ${inventory['scooter']['rent price']} Replacement Price: ${inventory['scooter']['replacement price']} In-Stock: {inventory['scooter']['amount']}

Please enter "exit" to leave the program.
---------------------------------------------------------------------------
    ''')
    while True:
        choice = input('What would you like to rent: ')
        choice = choice.lower().strip()
        if choice in inventory:
            if inventory[choice]['amount'] <= 0:
                print('\nSorry, that item is not avaliable.')
            else:
                print(
                    '\nThe cost for the {} will be ${} when you return it. As for now your deposit price is ${}\n'.
                    format(
                        inventory[choice]['name'],
                        core.sales_tax(inventory[choice]['rent price']),
                        core.replacement_tax(
                            inventory[choice]['replacement price'])))
                return inventory
        if choice == 'exit':
            exit()
        elif choice not in inventory:
            print('\nPlease choose a valid option.\n')


def returning(inventory, history):
    print(f'''
---------------------------------------------------------------------------
{inventory['bike']['name']} - Rent Price: ${inventory['bike']['rent price']} Replacement Price: ${inventory['bike']['replacement price']} In-Stock: {inventory['bike']['amount']}

{inventory['skateboard']['name']} - Rent Price: ${inventory['skateboard']['rent price']} Replacement Price: ${inventory['skateboard']['replacement price']} In-Stock: {inventory['skateboard']['amount']}

{inventory['scooter']['name']} - Rent Price: ${inventory['scooter']['rent price']} Replacement Price: ${inventory['scooter']['replacement price']} In-Stock: {inventory['scooter']['amount']}

Please enter "exit" to leave the program.
---------------------------------------------------------------------------
    ''')
    while True:
        choice = input('What item are you returning: ')
        if choice in inventory:
            inventory = core.return_item(inventory, choice)
            print(
                '\nYou\'ve returned 1 {}. Here is your deposit of ${}.'.format(
                    inventory[choice]['name'],
                    core.replacement_tax(
                        inventory[choice]['replacement price'])))
            return inventory
        if choice not in inventory:
            print('\nSorry, but that\'s not an item you can return.\n')


def main():
    inventory = core.create_inventory(disk.read_file('inventory.txt'))
    history = core.create_inventory(disk.read_file('inventory.txt'))
    while True:
        user = input(
            'Welcome to the Rental Store\n1) Customer\n2) Employee\n3) Exit\nWho may I help today: '
        )
        if user == '1':
            customer_choices(inventory, history)
        elif user == '2':
            employee_choices(inventory, history)
        elif user == '3':
            exit()


if __name__ == '__main__':
    main()
