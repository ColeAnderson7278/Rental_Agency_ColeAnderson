from unittest import mock
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
    }), 'rent', 'bike', 15) == '''15.0,bike,rent,\n'''

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
    }), 'return', 'scooter', 9.55) == '''9.55,scooter,return,\n'''


def test_find_total():
    assert core.find_total([[['15.0', 'bike', 'rent',
                              '\n'], ['15.0', 'bike', 'rent', '\n'],
                             ['6.5', 'scooter', 'rent', '\n']]]) == 36.5

    assert core.find_total([[['22.777', 'bike', 'rent',
                              '\n'], ['15.0', 'bike', 'rent', '\n'],
                             ['9.0', 'scooter', 'rent', '\n']]]) == 46.78

    assert core.find_total([[]]) == 0.0


def test_dictionary_to_file():
    assert core.dictionary_to_file({
        'bike': {
            'name': 'Bike',
            'rent price': 25,
            'replacement price': 150,
            'amount': 10
        },
        'skateboard': {
            'name': 'Skateboard',
            'rent price': 10,
            'replacement price': 80,
            'amount': 6
        },
        'scooter': {
            'name': 'Scooter',
            'rent price': 15,
            'replacement price': 65,
            'amount': 8
        }
    }) == '''type,name,rent price,replacement price,amount
bike,Bike,25,150,10,
skateboard,Skateboard,10,80,6,
scooter,Scooter,15,65,8,'''


def test_return_item():
    assert core.return_item({
        'bike': {
            'name': 'Bike',
            'rent price': 25,
            'replacement price': 150,
            'amount': 10
        },
        'skateboard': {
            'name': 'Skateboard',
            'rent price': 10,
            'replacement price': 80,
            'amount': 6
        },
        'scooter': {
            'name': 'Scooter',
            'rent price': 15,
            'replacement price': 65,
            'amount': 8
        }
    }, 'bike') == {
        'bike': {
            'name': 'Bike',
            'rent price': 25,
            'replacement price': 150,
            'amount': 11
        },
        'skateboard': {
            'name': 'Skateboard',
            'rent price': 10,
            'replacement price': 80,
            'amount': 6
        },
        'scooter': {
            'name': 'Scooter',
            'rent price': 15,
            'replacement price': 65,
            'amount': 8
        }
    }


@fake_file({
    'file.txt':
    'Money,Product,Type\n6.5,scooter,rent,\n9.55,scooter,return,\n2.7,skateboard,return,\n15.0,bike,rent,'
})
def test_create_history():
    assert core.create_history('') == 'None'

    assert core.create_history(disk.read_file('file.txt')) == [[[
        '6.5', 'scooter', 'rent', '\n'
    ], ['9.55', 'scooter', 'return',
        '\n'], ['2.7', 'skateboard', 'return',
                '\n'], ['15.0', 'bike', 'rent', '']]]


def test_price_by_days():
    assert core.price_by_days({
        'bike': {
            'name': 'Bike',
            'rent price': 25,
            'replacement price': 150,
            'amount': 10
        },
        'skateboard': {
            'name': 'Skateboard',
            'rent price': 10,
            'replacement price': 80,
            'amount': 6
        },
        'scooter': {
            'name': 'Scooter',
            'rent price': 15,
            'replacement price': 65,
            'amount': 8
        }
    }, 'bike', 2) == 50

    assert core.price_by_days({
        'bike': {
            'name': 'Bike',
            'rent price': 25,
            'replacement price': 150,
            'amount': 10
        },
        'skateboard': {
            'name': 'Skateboard',
            'rent price': 10,
            'replacement price': 80,
            'amount': 6
        },
        'scooter': {
            'name': 'Scooter',
            'rent price': 10,
            'replacement price': 65,
            'amount': 8
        }
    }, 'scooter', 7.2) == 70

    assert core.price_by_days({
        'bike': {
            'name': 'Bike',
            'rent price': 25,
            'replacement price': 150,
            'amount': 10
        },
        'skateboard': {
            'name': 'Skateboard',
            'rent price': 10,
            'replacement price': 80,
            'amount': 6
        },
        'scooter': {
            'name': 'Scooter',
            'rent price': 10,
            'replacement price': 65,
            'amount': 8
        }
    }, 'skateboard', 3) == 30


@fake_file({
    'employee.txt':
    'employee names\nJoeSmith\nBobSmith\nRickRoll\nCharlesSheen\n'
})
def test_make_employee_list():
    assert core.make_employee_list(disk.read_file('employee.txt')) == [
        'joesmith', 'bobsmith', 'rickroll', 'charlessheen'
    ]


@fake_file({
    'employee_list.txt':
    'employee names\nJoe Smith\nBob Smith\nRick Roll\nCharles Sheen\n'
})
def test_employee_check():
    assert core.employee_check(['joe smith', 'bob smith'], 'bob smith') == True
    assert core.employee_check(['joe smith', 'bob smith'], 'bob') == False


@mock.patch('builtins.exit')
def test_employee_check_exit(fake_exit):
    core.employee_check(['joe smith', 'bob smith'], 'exit')
    assert fake_exit.call_args_list == [[]]
