from data_structures_and_algorithms.challenges.linked_list.linked_list import LinkedList,Node


def test_connection():
    pass



def test_one():
    bird=LinkedList()
    bird.append_data("Eagle")
    bird.append_data("Dov")
    bird.append_data("Hawk")
    bird.append_data("Haaaaawk")
    bird.insertBefore("Haaaaawk","before")
    
    len=bird.count
    k=len+1 # The index 'k' is greater than the length of the linked -list
    """
    Where k is greater than the length of the linked list
    """
    expected="Out Of range"
    actual=bird[k]
    assert expected==actual

def test_two():
    bird=LinkedList()
    bird.append_data("Eagle")
    bird.append_data("Dov")
    bird.append_data("Hawk")
    bird.append_data("Haaaaawk")
    bird.insertBefore("Haaaaawk","before")
    
    len=bird.count
    k=len # The index 'k' is Equal to the length of the linked -list
    """
    Where k and the length of the list are the same
    """
    expected="Out Of range"
    actual=bird[k]
    assert expected==actual

def test_three():
    """
    Where k is not a positive integer
    """
    bird=LinkedList()
    bird.append_data("Eagle")
    bird.append_data("Dov")
    bird.append_data("Hawk")
    bird.append_data("Haaaaawk")
    bird.insertBefore("Haaaaawk","before")
    
    len=bird.count
    k=-1 # The index 'k' is a negative
    expected="Out Of range"
    actual=bird[k]
    assert expected==actual


def test_four():
    """
    Where the linked list is of a size 1
    """
    bird=LinkedList()
    bird.append_data("Eagle")
    len=bird.count # = 1
    k=len-1 # k =0
    expected='Eagle'
    actual=bird[k]
    assert expected==actual

def test_five_1():
    """
    “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
    """
    bird=LinkedList()
    bird.append_data("Eagle")
    bird.append_data("Dov")
    bird.append_data("Hawk")
    bird.append_data("Haaaaawk")
    bird.insertBefore("Haaaaawk","before")
    
    len=bird.count
    k=2 # The index 'k' is a a happy path
    expected="Hawk"
    actual=bird[k]
    assert expected==actual

def test_five_2():
    """
    “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
    """
    bird=LinkedList()
    bird.append_data("Eagle")
    bird.append_data("Dov")
    bird.append_data("Hawk")
    bird.append_data("Haaaaawk")
    bird.insertBefore("Haaaaawk","before")
    
    len=bird.count
    k=4 # The index 'k' is a a happy path
    expected="Eagle"
    actual=bird[k]
    assert expected==actual