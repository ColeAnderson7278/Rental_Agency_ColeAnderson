from bcca.test import fake_file
import core
import disk


@fake_file({
    'inventory.txt':
    '''
movie,Jaws,2.50,7.50,avaliable
game,Resident Evil 4,5.00,40.00,avaliable
book,House of the Scorpion,1.50,12.00,avaliable
'''
})
def test_create_dictionary():
    file_info = disk.read_file('inventory.txt')
    assert core.create_dictionary(file_info) == {
        'movie': ['Jaws', '2.50', '7.50', 'avaliable\n'],
        'game': ['Resident Evil 4', '5.00', '40.00', 'avaliable\n'],
        'book': ['House of the Scorpion', '1.50', '12.00', 'avaliable\n']
    }
