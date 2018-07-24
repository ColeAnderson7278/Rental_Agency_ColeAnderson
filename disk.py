def read_file(filename):
    with open(filename) as file:
        file.readline()
        file_info = file.readlines()
        return file_info


def write_file(string_inventory):
    with open(filename, 'w') as file:
        file.write(string_inventory)
