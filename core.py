def create_dictionary(file_info):
    dictionary = {}
    for lines in file_info:
        info = lines.split(',')
        key = info[0].strip()
        value = info[1:]
        dictionary[key] = value
    return dictionary
