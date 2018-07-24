def create_inventory(file_info):
    inventory = {}
    for lines in file_info:
        info = lines.split(',')
        key = info[0].strip()
        value = {
            'rent price': int(info[1]),
            'replacement price': int(info[2]),
            'amount': int(info[3])
        }
        inventory[key] = value
    return inventory
