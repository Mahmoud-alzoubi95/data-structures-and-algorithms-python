from data_structures_and_algorithms.challenges.insertion_sort.insertion_sort import InsertionSort
import pytest

def test_conn():
    pass


def test_arr_one(pre_arr):
    sample=pre_arr[0] # Point to array a
    expected=[4, 7, 9, 10, 11, 40]
    actual = InsertionSort(sample)
    assert expected ==actual

def test_arr_Reverse_sorted(pre_arr):
    sample=pre_arr[1]
    expected = [-2, 5, 8, 12, 18, 20]
    actual=InsertionSort(sample)
    assert expected== actual

def test_arr_Few_uniques(pre_arr):
    sample=pre_arr[2]
    expected = [5, 5, 5, 7, 7, 12]
    actual=InsertionSort(sample)
    assert expected== actual

def test_arr_Nearly_sorted(pre_arr):
    sample=pre_arr[3]
    expected = [2, 3, 5, 7, 11, 13]
    actual=InsertionSort(sample)
    assert expected== actual


@pytest.fixture
def pre_arr():
    a= [4 ,7 ,9, 40, 11, 10]
    b= [20,18,12,8,5,-2]
    c= [5,12,7,5,5,7]
    d= [2,3,5,7,13,11]

    return a,b,c,d