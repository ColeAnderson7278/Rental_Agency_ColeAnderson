from bcca.test import fake_file


@fake_file({
    'inventory.txt':
    '''
Type,Name,Rental Price,Replacement Price,Status
movie, Jaws, 2.50, 7.50, in
game, Resident Evil 4, 5.00, 40.00, in
book, House of the Scorpion, 1.50, 12.00, in
'''
})
def test_renting():
    assert disk.load_inventory() == ...
