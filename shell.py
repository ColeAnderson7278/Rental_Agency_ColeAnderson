import disk
import core


def print_inventory(inventory):
    for key in inventory:
        print(
            f"\n{inventory[key]['name']} - Rent Price Per Day: {inventory[key]['rent price']} Replacement Price: {inventory[key]['replacement price']} In-Stock: {inventory[key]['amount']}"
        )


def customer_choices(inventory, history):
    while True:
        choice = input(
            '\n1) Rent\n2) Return\n3) Exit\nWhat can I help you with: ')
        if choice == '1':
            renting(inventory, history)
        if choice == '2':
            returning(inventory, history)
        if choice == '3':
            print('\nGoodbye')
            exit()


def employee_choices(inventory, history):
    while True:
        choice = input(
            '\n1) Check Stock\n2) Transactions\n3) Revenue\n4) Exit\nWhat can I help you with: '
        )
        if choice == '1':
            check_stock(inventory)
        elif choice == '2':
            transaction_history()
        elif choice == '3':
            total_revenue(history)
        elif choice == '4':
            print('\nGoodbye')
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


def transaction_history():
    print('\nTransaction List:\n----------------------------------')
    for transactions in disk.read_file('history.txt'):
        print(transactions)
    print('----------------------------------')


def total_revenue(history):
    print(f'\nThe store\'s total revenue is: ${core.find_total(history)}')


def renting(inventory, history):
    print_inventory(inventory)
    while True:
        choice = input('\nWhat would you like to rent: ')
        choice = choice.lower().strip()
        if choice in inventory:
            if inventory[choice]['amount'] <= 0:
                print('\nSorry, that item is not avaliable.')
            else:
                print(
                    '\nThe cost for the {} will be ${} when you return it . As for now your deposit price is ${}'.
                    format(
                        inventory[choice]['name'],
                        core.sales_tax(inventory[choice]['rent price']),
                        core.replacement_tax(
                            inventory[choice]['replacement price'])))
                inventory = core.rent_item(inventory, choice)
            return write_in_rent(inventory, choice, None)
        if choice == 'exit':
            print('\nGoodbye')
            exit()
        elif choice not in inventory:
            print('\nPlease choose a valid option.\n')


def returning(inventory, history):
    print_inventory(inventory)
    while True:
        choice = input('\nWhat item are you returning: ')
        if choice in inventory:
            return return_item_type(inventory, history, choice)
        if choice not in inventory:
            print('\nSorry, but that\'s not an item you can return.\n')
        if choice == 'exit':
            print('\nGoodbye')
            exit()


def return_item_type(inventory, history, choice):
    while True:
        return_type = input(
            '\n1) Return Item\n2) Replace Item\n3) Exit\nPlease choose what you would like to do: '
        )
        if return_type == '1':
            price = return_days(inventory, choice)
            inventory = core.return_item(inventory, choice)
            print(
                '\nYou\'ve returned 1 {}. Here is your deposit of ${} and your total is ${}'.
                format(
                    inventory[choice]['name'],
                    core.replacement_tax(
                        inventory[choice]['replacement price']), price))
            return write_in_return(inventory, choice, price)
        elif return_type == '2':
            inventory = core.return_item(inventory, choice)
            print('\nYou\'ve replaced 1 {}. The total price while be ${}.'.
                  format(inventory[choice]['name'],
                         (inventory[choice]['replacement price'] -
                          core.replacement_tax(
                              inventory[choice]['replacement price']))))
            return write_in_return(inventory, choice,
                                   inventory[choice]['replacement price'])
        elif return_type == '3':
            print('\nGoodbye')
            exit()
        else:
            print('\nPlease enter a correct response.')


def write_in_return(inventory, choice, price):
    disk.append_file(
        core.add_to_history(inventory, 'return', choice, price), 'history.txt')
    disk.write_file(core.dictionary_to_file(inventory), 'inventory.txt')
    return inventory


def write_in_rent(inventory, choice, price):
    disk.append_file(
        core.add_to_history(inventory, 'rent', choice, price), 'history.txt')
    disk.write_file(core.dictionary_to_file(inventory), 'inventory.txt')
    return inventory


def return_days(inventory, choice):
    while True:
        days = input('\nHow many days have you had this item: ')
        days = str(days.strip())
        if days.isdigit() == True:
            return core.price_by_days(inventory, choice, float(days))
        if days.isdigit() == False:
            print('\nPlease enter a valid number of days.')


def main():
    inventory = core.create_inventory(disk.read_file('inventory.txt'))
    history = core.create_history(disk.read_file('history.txt'))
    while True:
        user = input(
            'Welcome to the Rental Store\n\n1) Customer\n2) Employee\n3) Exit\nWho may I help today: '
        )
        if user == '1':
            customer_choices(inventory, history)
        elif user == '2':
            employee_choices(inventory, history)
        elif user == '3':
            print('\nGoodbye')
            exit()


if __name__ == '__main__':
    main()
