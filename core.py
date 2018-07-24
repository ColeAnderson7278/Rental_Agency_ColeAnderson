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
    if inventory[item_type]['amount'] == 0:
        print('Sorry, these are not in stock.')
    else:
        inventory[item_type]['amount'] = inventory[item_type]['amount'] - 1
        print(f'You\'ve rented 1 {inventory[item_type]['name']}.')
        return inventory[item_type]['amount']
