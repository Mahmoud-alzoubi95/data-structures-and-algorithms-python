from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import Queue

def test_connection():
    pass

def test_one():
    q=Queue()
    q.enqueue("Sherry","Cat")
    q.enqueue("Oliver","Cat")
    q.enqueue("Oscar D","Dog")
    q.enqueue("Simba","Cat")

    expected="Sherry"
    actual=q.dequeue_animal("Cat")
    assert expected==actual

def test_two():
    q=Queue()
    q.enqueue("Sherry","Cat")
    q.enqueue("Oliver","Cat")
    q.enqueue("Oscar D","Dog")
    q.enqueue("Archie","Dog")
    q.enqueue("Simba","Cat")

    expected="Oscar D"
    actual=q.dequeue_animal("Dog")
    assert expected==actual

def test_three():
    q=Queue()
    q.enqueue("Sherry","Cat")
    q.enqueue("Oliver","Cat")
    # q.enqueue("Oscar D","Dog")
    # q.enqueue("Archie","Dog")
    q.enqueue("Simba","Cat")
    expected=None
    actual=q.dequeue_animal("Dog")
    assert expected==actual

def test_four():
    q=Queue()
    # q.enqueue("Sherry","Cat")
    # q.enqueue("Oliver","Cat")
    q.enqueue("Oscar D","Dog")
    q.enqueue("Archie","Dog")
    q.enqueue("Molly","Dog")

    # q.enqueue("Simba","Cat")
    expected=None
    actual=q.dequeue_animal("Cat")
    assert expected==actual