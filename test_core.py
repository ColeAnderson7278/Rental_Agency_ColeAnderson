from bcca.test import fake_file
import core
import disk


@fake_file({
    'file.txt': '''
bikes,25,150,10
skates,10,80,6
scooter,15,65,8
'''
})
def test_create_dictionary():
    assert core.create_dictionary(disk.read_file('file.txt')) == ({
        'bikes': {
            'rent price': 25,
            'replacement price': 150,
            'amount': 10
        },
        'skates': {
            'rent price': 10,
            'replacement price': 80,
            'amount': 6
        },
        'scooter': {
            'rent price': 15,
            'replacement price': 65,
            'amount': 8
        }
    })
