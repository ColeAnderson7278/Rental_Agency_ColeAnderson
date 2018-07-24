def read_file(filename):
    with open(filename) as file:
        file_info = file.readlines()
        return file_info
