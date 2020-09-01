from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation


def test_one():

    expected=True
    actual=multi_bracket_validation("{}(){}")
    assert actual == expected



def test_two():
    expected=True
    
    actual=multi_bracket_validation("()[[Extra Characters]]")
    assert actual == expected



def test_three():
    expected='error unmatched opening ( remaining.'
    
    actual=multi_bracket_validation("[({}]")
    assert actual == expected



def test_four():
    expected=True
    
    actual=multi_bracket_validation("{(})")
    assert actual == expected


def test_five():
    
    expected="error closing ) arrived without corresponding opening."
    actual=multi_bracket_validation(")")
    assert actual == expected

