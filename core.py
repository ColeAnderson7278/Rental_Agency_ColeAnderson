def create_inventory(file_info):
    inventory = {}
    for lines in file_info:
        info = lines.split(',')
        key = info[0].strip()
        value = {
            'name': info[1].strip(),
            'rent price': int(info[2]),
            'replacement price': int(info[3]),
            'amount': int(info[4])
        }
        inventory[key] = value
    return inventory


def rent_item(inventory, item_type):
    name = inventory[item_type]['name']
    inventory[item_type]['amount'] = inventory[item_type]['amount'] - 1
    return inventory


def return_item(inventory, item_type):
    name = inventory[item_type]['name']
    inventory[item_type]['amount'] = inventory[item_type]['amount'] + 1
    return inventory


def sales_tax(number):
    return round(number + (number * .07), 2)


def replacement_tax(number):
    return round((number * .1), 2)


def add_to_history(inventory, type_, choice, price):
    if type_ == 'rent':
        return f'''{replacement_tax(
                        inventory[choice]['replacement price'])},{choice},{type_},\n'''
    elif type_ == 'return':
        return f'''{price},{choice},{type_},\n'''


def create_history(file_info):
    if file_info == '':
        history = 'None'
        return history
    else:
        further = []
        list_of = []
        history = []
        for line in file_info:
            line = line.split('-')
            for part in line:
                part = part.split(',')
                further.append(part)
        list_of.append(further)
        return list_of


def find_total(history):
    total = 0
    for line in history[0][0:]:
        total += float(line[0])
    return round((total), 2)


def dictionary_to_file(dictionary):
    string = 'type,name,rent price,replacement price,amount'
    for key in dictionary:
        string += f"\n{dictionary[key]['name'].lower()},{dictionary[key]['name']},{dictionary[key]['rent price']},{dictionary[key]['replacement price']},{dictionary[key]['amount']},"

    return string


def price_by_days(inventory, choice, days):
    price = inventory[choice]['rent price'] * (round(days))
    return price


def make_employee_list(file_info):
    employees = []
    for lines in file_info:
        employees.append(lines.lower().replace('\n', ''))
    return employees


def employee_check(employees, name):
    if name.lower() in employees:
        return True
    else:
        return False
