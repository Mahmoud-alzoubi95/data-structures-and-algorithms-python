from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import newNode,insert,tree_intersection
import pytest

def test_conn():
    pass

def test_insert_at_root():
    root1 = None
    root1 = insert(root1, 150) # insert at root
    expected = 150
    actual = root1.key
    assert expected ==actual

def test_insert_at_left():
    root1 = None
    root1 = insert(root1, 150) # insert at root
    root1 = insert(root1, 100) # insert at left because 100 is less than the root value

    expected = 100
    actual = root1.left.key
    assert expected ==actual

def test_insert_at_right():
    root1 = None
    root1 = insert(root1, 150) # insert at root
    root1 = insert(root1, 100) # insert at left  because 100 is less    than the root value
    root1 = insert(root1, 200) # insert at right because 200 is greater then the root value
    expected = 200
    actual = root1.right.key
    assert expected ==actual


def test_intersection(pre):
    expected = [100, 125, 160, 200, 350, 500]
    actual = tree_intersection(pre[0],pre[1])
@pytest.fixture
def pre():
    root1 = None
    root1 = insert(root1, 150) 
    root1 = insert(root1, 100) 
    root1 = insert(root1, 75) 
    root1 = insert(root1, 160) 
    root1 = insert(root1, 250) 
    root1 = insert(root1, 200) 
    root1 = insert(root1, 350)
    root1 = insert(root1, 300) 
    root1 = insert(root1, 500)
    root1 = insert(root1, 125) 



    root2 = None
    root2 = insert(root2, 42) 
    root2 = insert(root2, 100) 
    root2 = insert(root2, 15) 
    root2 = insert(root2, 600) 
    root2 = insert(root2, 160)
    root2 = insert(root2, 200) 
    root2 = insert(root2, 350) 
    root2 = insert(root2, 4)
    root2 = insert(root2, 500) 
    root2 = insert(root2, 175)
    root2 = insert(root2, 125) 

    return root1, root2