from data_structures_and_algorithms.challenges.array_shift.array_shift import (
    insertShiftArray,
)



def test_shift():
    expected=[2,4,5,6,8]
    actual=insertShiftArray([2,4,6,8], 5)
    assert expected==actual

def test_shift_two():
    expected=[4,8,15,16,23,42]
    actual=insertShiftArray([4,8,15,23,42], 16)
    assert expected==actual

def test_shift_three():
    expected=[0,1,2,3,4,5,6,7,8,9,11,15]
    actual=insertShiftArray([0,1,2,3,4,5,6,7,8,9,15], 11)
    assert expected==actual

def test_shift_four():
    expected=[2,4,5,6,8,9,10,12]
    actual=insertShiftArray([2,4,5,6,8,10,12], 9)
    assert expected==actual

def test_shift_five():
    expected=[10,20,30,40,45,50]
    actual=insertShiftArray([10,20,30,40,50], 45)
    assert expected==actual
