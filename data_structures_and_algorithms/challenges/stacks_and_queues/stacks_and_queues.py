class Node:
    def __init__(self,value):
        self.value=value
        self.next=None





class Stack:
    """
    A stack is used to fitch the data from the top
    where the first in , last out 
    """
    
    def __init__(self):
        self.max=10000
        self.top=None
        pass

    def push(self, value):
        """
        This method to pusg ( store data ) at the top of stack
        No return in this method
        """
        
        new_node=Node(value)
        temp=self.top
        self.top=new_node
        self.top.next=temp

    def pop(self):
        """
        return the top value in the stack
        and delete it the n move the pointer to the next top value
        """

        temp=self.top
        try:
            self.top=self.top.next
        except:
            return "All Nodes have been poped"
           
        temp.next=None
        return temp.value
        

    def peek(self):
        """
        return the top value with deletion 
        """
        try:
            return self.top.value
        except AttributeError as e:
            return "Stack is empty"

    def is_empty(self):
        """
        examin the stack if it has values or not
        return True Or False
        """
        return self.top == None

    def __str__(self):
        """
        This method to print the stack
        It return a concatenation string which can be formatted 
        output : {string}
        return output
        """
        output=''
        current=self.top
        while current:
            print(current.value)
            output+=f"{current.value} -> "
            current=current.next
        output+= f"{current}"
        return output


        



class Queue:
    

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        # Special case: if empty queue
        # f -> 1 <- r
        if not self.front and not self.rear:
            self.front = node
            self.rear = node

        old_rear = self.rear
        self.rear = node
        old_rear.next = self.rear
        # front -> 1 -> 2 -> 3 <- rear


    def dequeue(self):
        """
        dequeue(extract) Node that fristly entered
        """
        if self.front:
            temp=self.front
            self.front=temp.next
            temp.next=None
            if self.rear.value==temp.value:
                """
                if statment to check if the last node was dequeued
                then make the self.front point to None
                """
                
                self.front=None
            return temp.value
        else:
            return "The queue is Empty"

        

    def peek(self):
        try:
            return self.front.value
        except AttributeError as e:
            return f"Empty Queue!!!\nDevs Details: {e}"
        except Exception as e:
            return f"Some other exception happened!!! {e}"

    def is_empty(self):
        return self.front==None

    def __str__(self):
        """
        This method to print the queue
        It return a concatenation string which can be formatted 
        output : {string}
        return output
        """
        output=''
        current=self.front
        while current:
            print(current.value)
            output+=f"{current.value} -> "
            current=current.next
        output+= f"{current}"
        return output



        






if __name__=='__main__':
    stack=Stack()
    queue=Queue()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.pop()

    print(stack.pop().__str__())
    print(stack.peek())
    print(stack.is_empty())
    print(stack)

    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    queue.enqueue("d")
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.is_empty())
    print(queue)




