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
    number = round(number + (number * .07), 2)
    return number


def replacement_tax(number):
    number = round((number * .1), 2)
    return number


def add_to_history(inventory, type_, choice):
    if type_ == 'rent':
        return f'''{replacement_tax(
                        inventory[choice]['replacement price'])},{choice},{type_},\n'''
    elif type_ == 'return':
        payment = round(
            sales_tax(inventory[choice]['rent price']) - replacement_tax(
                inventory[choice]['replacement price']), 2)
        return f'''{payment},{choice},{type_},\n'''


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
    print(total)


#def dictionary_to_file(dictionary):
#    l = []
#    for items in dictionary.keys():
#        l.append(items)
#    x = ''
#    for items in l:
#        x.add(dictionary[l]['amount'])
#    return x
