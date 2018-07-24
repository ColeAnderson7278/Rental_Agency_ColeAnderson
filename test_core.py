from bcca.test import fake_file
import core
import disk


@fake_file({
    'file.txt':
    '''
bikes,bike,25,150,10
skateboards,skateboard,10,80,6
scooters,scooter,15,65,8
'''
})
def test_create_inventory():
    assert core.create_inventory(disk.read_file('file.txt')) == ({
        'bikes': {
            'name': 'bike',
            'rent price': 25,
            'replacement price': 150,
            'amount': 10
        },
        'skateboards': {
            'name': 'skateboard',
            'rent price': 10,
            'replacement price': 80,
            'amount': 6
        },
        'scooters': {
            'name': 'scooter',
            'rent price': 15,
            'replacement price': 65,
            'amount': 8
        }
    })
