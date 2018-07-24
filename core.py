def create_dictionary(file_info):
    dictionary = {}
    for lines in file_info:
        info = lines.split(',')
        key = info[0].strip()
        value = {
            'rent price': int(info[1]),
            'replacement price': int(info[2]),
            'amount': int(info[3])
        }
        dictionary[key] = value
    return dictionary
