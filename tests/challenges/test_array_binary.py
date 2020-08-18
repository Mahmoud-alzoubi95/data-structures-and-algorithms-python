from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import binary_search,long_arr





def test_one():
    expected=50
    actual=long_arr(100,50)
    assert expected==actual


def test_two():
    expected=-1
    actual=long_arr(100,150)
    assert expected==actual


def test_three():
    expected=10
    actual=long_arr(150,10)
    assert expected==actual


def test_four():
    expected=5
    actual=long_arr(5000,5)
    assert expected==actual


def test_five():
    expected=5000
    actual=long_arr(1000000,5000)
    assert expected==actual












