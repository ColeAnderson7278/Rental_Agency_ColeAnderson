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


#def dictionary_to_file(dictionary):
#    l = []
#    for items in dictionary.keys():
#        l.append(items)
#    x = ''
#    for items in l:
#        x.add(dictionary[l]['amount'])
#    return x
