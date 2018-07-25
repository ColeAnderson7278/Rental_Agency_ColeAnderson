def read_file(filename):
    with open(filename) as file:
        file.readline()
        file_info = file.readlines()
        return file_info


def write_file(string_inventory, filename):
    with open(filename, 'w') as file:
        file.write(string_inventory)


def append_file(transaction, filename):
    with open(filename, 'a') as file:
        file.write(transaction)
