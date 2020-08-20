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
    return{"a":a,"b":b,"c":c,"d":d,"e":e,"bird":bird}

    
def test_one():
    # bird=LinkedList()
    bird=LinkedList()
    bird.append_data("Eagle")
    bird.append_data("Dov")
    bird.append_data("Hawk")
    

    expected="Eagle -> Dov -> Hawk -> None"
    actual=bird.__str__()
    assert expected==actual


def test_two(prep_data):
    prep_data['bird']
    prep_data['a']
    prep_data['b']
    prep_data['c']
   
    expected=True
    actual=prep_data['bird'].includes("Hawk")
    assert expected==actual


def test_three(prep_data):
    prep_data['bird']
    prep_data['a']
    prep_data['b']
    prep_data['c']
   
    expected=False
    actual=prep_data['bird'].includes("Woody")
    assert expected==actual
    



def test_four(prep_data):
    prep_data['bird']
    prep_data['a']
    prep_data['b']
    prep_data['c']
    expected='This function Does not been established yet'
    actual=prep_data['bird'].insert_btw("Hawk","Woody_Packer")
    assert expected==actual



def test_five(prep_data):
    new_bird=prep_data['bird'].insert("Bateleur Eagle")
    

    expected="Bateleur Eagle -> Eagle -> Dov -> Hawk -> None"
    actual=prep_data['bird'].__str__()
    assert expected==actual