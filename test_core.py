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


def test_rent_item():
    assert core.rent_item(({
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
    }), 'bikes') == ({
        'bikes': {
            'name': 'bike',
            'rent price': 25,
            'replacement price': 150,
            'amount': 9
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

    def test_return_item():
        assert core.return_item(({
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
        }), 'bikes') == ({
            'bikes': {
                'name': 'bike',
                'rent price': 25,
                'replacement price': 150,
                'amount': 11
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


def test_sales_tax():
    assert core.sales_tax(10) == 10.7
    assert core.sales_tax(0) == 0.0
    assert core.sales_tax(5) == 5.35


def test_replacement_tax():
    assert core.replacement_tax(10) == 1.0
    assert core.replacement_tax(0) == 0.0
    assert core.replacement_tax(5) == .5


def test_add_to_history():
    assert core.add_to_history(({
        'bike': {
            'name': 'bike',
            'rent price': 25,
            'replacement price': 150,
            'amount': 10
        },
        'skateboard': {
            'name': 'skateboard',
            'rent price': 10,
            'replacement price': 80,
            'amount': 6
        },
        'scooter': {
            'name': 'scooter',
            'rent price': 15,
            'replacement price': 65,
            'amount': 8
        }
    }), 'rent', 'bike') == '''15.0,bike,rent,\n'''

    assert core.add_to_history(({
        'bike': {
            'name': 'bike',
            'rent price': 25,
            'replacement price': 150,
            'amount': 10
        },
        'skateboard': {
            'name': 'skateboard',
            'rent price': 10,
            'replacement price': 80,
            'amount': 6
        },
        'scooter': {
            'name': 'scooter',
            'rent price': 15,
            'replacement price': 65,
            'amount': 8
        }
    }), 'return', 'scooter') == '''9.55,scooter,return,\n'''


def test_find_total():
    assert core.find_total([[['15.0', 'bike', 'rent',
                         '\n'], ['15.0', 'bike', 'rent', '\n'],
                        ['6.5', 'scooter', 'rent', '\n']]]) == 36.5

def test_dictionary_to_file():
    assert core.dictionary_to_file({'bike': {'name': 'Bike', 'rent price': 25, 'replacement price': 150, 'amount': 10}, 'skateboard': {'name': 'Skateboard', 'rent price': 10, 'replacement price': 80, 'amount': 6}, 'scooter': {'name': 'Scooter', 'rent price': 15, 'replacement price': 65, 'amount': 8}}
) == '''bike,Bike,25,150,10
skateboard,Skateboard,10,80,6
scooter,Scooter,15,65,8'''
