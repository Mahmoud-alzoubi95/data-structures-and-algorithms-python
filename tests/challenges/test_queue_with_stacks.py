from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks import PseudoQueue,Stack

def test_connection():
    pass

def test_one():
    q=PseudoQueue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.enqueue("D")

    expected="A -> B -> C -> D -> None"
    actual=q.__str__()
    assert expected==actual

def test_two():
    q=PseudoQueue()
    q.enqueue("1")
    q.enqueue("2")
    q.enqueue("3")
    q.enqueue("4")
    expected="1 -> 2 -> 3 -> 4 -> None"
    actual=q.__str__()
    assert expected==actual


def test_three():
    q=PseudoQueue()
    q.enqueue("1")
    q.enqueue("2")
    q.enqueue("3")
    q.enqueue("4")
    q.dequeue()
    q.dequeue()
    expected="3 -> 4 -> None"
    actual=q.__str__()
    assert expected==actual


