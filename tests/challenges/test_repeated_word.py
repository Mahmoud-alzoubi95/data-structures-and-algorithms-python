from data_structures_and_algorithms.challenges.repeated_word.repeated_word import lengthy_string
import pytest


def test_conn():
    pass
#------First Text-----------#

def test_repeat_txtOne(pre):
    expected ='a'
    actual = lengthy_string(pre[0])[4]
    assert expected==actual

def test_how_many_words_txtOne(pre):
    expected = 10
    actual = lengthy_string(pre[0])[1]
    assert expected==actual


def test_most_five_most_common_txtOne(pre):
    expected=[('a', 2), ('Once', 1), ('upon', 1), ('time', 1), ('there', 1)]
    actual=lengthy_string(pre[0])[3]
    assert expected==actual



#------Second Text-----------#

def test_repeat_txtTwo(pre):
    expected ='it'
    actual = lengthy_string(pre[1])[4]
    assert expected==actual

def test_how_many_words_txtTwo(pre):
    expected = 120
    actual = lengthy_string(pre[1])[1]
    assert expected==actual


def test_most_five_most_common_txtTwo(pre):
    expected=[('the', 14), ('of', 12), ('was', 11), ('it', 9), ('we', 4)]
    actual=lengthy_string(pre[1])[3]
    assert expected==actual


#------3rd Text-----------#

def test_repeat_txtThree(pre):
    expected ='summer'
    actual = lengthy_string(pre[2])[4]
    assert expected==actual

def test_how_many_words_txtThree(pre):
    expected = 23
    actual = lengthy_string(pre[2])[1]
    assert expected==actual


def test_most_five_most_common_txtThree(pre):
    expected=[('was', 2), ('summer', 2), ('the', 2), ('I', 2), ('It', 1)]
    actual=lengthy_string(pre[2])[3]
    assert expected==actual



@pytest.fixture
def pre():
    txt_one= "Once upon a time, there was a brave princess who..."
    txt_two = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only"
    txt_three = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York.."

    return txt_one, txt_two, txt_three