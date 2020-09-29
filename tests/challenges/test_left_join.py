from data_structures_and_algorithms.challenges.left_join.left_join import left_join
import pytest
def test_conn():
    pass

def test_dict_type_input1(pre):
    expected = "<class 'dict'>"
    actual = f"{type(pre[0])}"
    assert expected == actual

def test_dict_type_input2(pre):
    expected = "<class 'dict'>"
    actual = f"{type(pre[1])}"
    assert expected == actual

def test_left_join(pre):
    expected = [
                ['fond', 'enamored', 'averse'],
                ['wrath', 'anger', 'delight'],
                ['diligent', 'employed', 'idle'],
                ['outfit', 'garb', None],
                ['guide', 'usher', 'follow']
                ]
    actual= left_join(pre[0],pre[1])
    assert expected == actual




@pytest.fixture
def pre():
    dict_one = {'fond':'enamored','wrath':'anger','diligent':'employed','outfit':'garb','guide':'usher'}
    dict_two = {'fond':'averse','wrath':'delight','diligent':'idle','guide':'follow','flow':'jam'}
    return dict_one,dict_two