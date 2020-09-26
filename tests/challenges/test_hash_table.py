from data_structures_and_algorithms.challenges.hashtable.hashtable import Hashtable
import pytest

def test_conn():
    pass


def test_hashing(pre):
    expected = 871
    actual = pre.hash('name')
    assert expected==actual

def test_addTo_table(pre):
    expected = "Add method appended Apple to the key Fruit"
    actual = pre.add('Fruit','Apple')


def test_duplicate(pre):
    pre.add('Fruit','Apple')
    
    expected ="Repalce old with new done"
    actual = pre.add('Fruit','Apple')
    assert expected==actual



    

def test_getfrom_table(pre):
    pre.add('Fruit','Orange')
    expected = 'Orange -> None'
    actual=pre.get('Fruit').__str__()


    assert expected==actual

def test_contain(pre):
    expected = True
    pre.add('Fruit','Apple')
    actucal = pre.contains('Fruit')
    assert expected == actucal





@pytest.fixture
def pre():
    t=Hashtable()
    return t