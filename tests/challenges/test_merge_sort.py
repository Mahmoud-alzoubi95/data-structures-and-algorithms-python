from data_structures_and_algorithms.challenges.merge_sort.merge_sort import merge_sort
import pytest



def test_conn():
    pass

def test_Reverse_sorted(pre_data):
    sample=pre_data[0]
    expected=[-2,5,8,12,18,20]
    actual=merge_sort(sample)
    assert expected==actual

def test_Few_uniques(pre_data):
    sample=pre_data[1]
    expected=[5,5,5,7,7,12]
    actual = merge_sort(sample)
    assert expected==actual

def test_Nearly_sorted(pre_data):
    sample=pre_data[2]
    expected=[2,3,5,7,11,13]
    actual = merge_sort(sample)
    assert expected==actual


def test_last_arr(pre_data):
    sample=pre_data[3]
    expected=[4,8,15,16,23,42]
    actual = merge_sort(sample)
    assert expected==actual



@pytest.fixture
def pre_data():
    a=[20,18,12,8,5,-2]
    b=[5,12,7,5,5,7]
    c=[2,3,5,7,13,11]
    d=[8,4,23,42,16,15]
    return a,b,c,d