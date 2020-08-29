from data_structures_and_algorithms.challenges.stacks_and_queues.stacks_and_queues import Node,Stack,Queue

def test_connection():
    pass

def test_stack_one():
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    expected="3 -> 2 -> 1 -> None"
    actual=s.__str__()
    assert expected==actual

def test_stack_two():
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()

    expected="2 -> 1 -> None"
    actual=s.__str__()
    assert expected==actual

def test_stack_three():
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    

    expected=3
    actual=s.peek()
    assert expected==actual

def test_stack_four():
    s=Stack()
    
    

    expected=True
    actual=s.is_empty()
    assert expected==actual

def test_stack_five():
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    

    expected=False
    actual=s.is_empty()
    assert expected==actual


def test_queue_one():
    q=Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")


    

    expected="A -> B -> C -> None"
    actual=q.__str__()
    assert expected==actual

def test_queue_two():
    q=Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.dequeue()


    

    expected="B -> C -> None"
    actual=q.__str__()
    assert expected==actual

def test_queue_three():
    q=Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    


    

    expected="A"
    actual=q.peek()
    assert expected==actual

def test_queue_four():
    q=Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    


    

    expected=False
    actual=q.is_empty()
    assert expected==actual

def test_queue_five():
    q=Queue()
    
    


    

    expected=True
    actual=q.is_empty()
    assert expected==actual







