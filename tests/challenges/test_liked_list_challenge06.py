from data_structures_and_algorithms.challenges.linked_list.linked_list import LinkedList,Node
import pytest

@pytest.fixture
def prep_data():
    bird=LinkedList()
    a=bird.append_data("Eagle")
    b=bird.append_data("Dov")
    c=bird.append_data("Hawk")
    d=bird.includes("awk")
    e=bird.insert_btw("Hawk","Woody_Packer") # this for handle the error
    f=bird.insertBefore("Haaaaawk","before")
    g=bird.insertAfter("Hawk",'newOne')
    return{"a":a,"b":b,"c":c,"d":d,"e":e,"bird":bird,"f":f,"g":g}


def test_one(prep_data):
    bird=LinkedList()
    # prep_data['a']
    # prep_data['b']
    # prep_data['c']
    bird=LinkedList()
    bird.append_data("Eagle")
    bird.append_data("Dov")
    bird.append_data("Hawk")
    expected='Eagle -> Dov -> Hawk -> None'
    actual=bird.__str__()
    assert expected==actual

def test_two():

    """
    This to test inseration at the middle Using insertBefore method
    """
    bird=LinkedList()
    # prep_data['a']
    # prep_data['b']
    # prep_data['c']
    bird=LinkedList()
    bird.append_data("Eagle")
    bird.append_data("Dov")
    bird.append_data("Hawk")
    bird.append_data("Eagle2")
    bird.append_data("Dov2")
    bird.append_data("Hawk2")
    bird.insertBefore("Eagle2","BeeeeeFFFFFooooooRRRRRe")
    expected='Eagle -> Dov -> Hawk -> BeeeeeFFFFFooooooRRRRRe -> Eagle2 -> Dov2 -> Hawk2 -> None'
    actual=bird.__str__()
    assert expected==actual



def test_three():
    
    bird=LinkedList()
    # prep_data['a']
    # prep_data['b']
    # prep_data['c']
    bird=LinkedList()
    bird.append_data("Eagle")
    bird.append_data("Dov")
    bird.append_data("Hawk")
    bird.append_data("Eagle2")
    bird.append_data("Dov2")
    bird.append_data("Hawk2")
    bird.insert("beginning")
    expected='beginning -> Eagle -> Dov -> Hawk -> Eagle2 -> Dov2 -> Hawk2 -> None'
    actual=bird.__str__()
    assert expected==actual


def test_four():
    bird=LinkedList()
    # prep_data['a']
    # prep_data['b']
    # prep_data['c']
    bird=LinkedList()
    bird.append_data("Eagle")
    bird.append_data("Dov")
    bird.append_data("Hawk")
    bird.append_data("Eagle2")
    bird.append_data("Dov2")
    bird.append_data("Hawk2")
    bird.insertAfter("Eagle2","AFTER")
    expected='Eagle -> Dov -> Hawk -> Eagle2 -> AFTER -> Dov2 -> Hawk2 -> None'
    actual=bird.__str__()
    assert expected==actual
