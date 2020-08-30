from data_structures_and_algorithms.challenges.stacks_and_queues.stacks_and_queues import Node,Stack
s1=Stack()
s2=Stack()
class PseudoQueue:
    """
    This class create a queue with 2 stacks
    Has two method -till now- enqueue and dequeue
    """
    def __init__(self):
        self.s1=Stack()
        self.s2=Stack()
        

    def enqueue(self,value):
        """
        do enqueue with push and pop methods from Stack
        """
        if self.s1.top==None:
            
            self.s1.push(value)
           
        else:
            current=self.s1.top
            while current:
                # a=self.s1.pop()
                # print("from else",a)
                a=self.s1.pop()
                if a=="All Nodes have been poped":
                    break
                self.s2.push(a)
                print("How many Times",a)
                # current=current.next
               
                
            self.s1.push(value)
            current_2=self.s2.top
            while current_2:
                # print("push")
                # print(self.s2.peek())
                b=self.s2.pop()
                if b=="All Nodes have been poped":
                    break
                print("This is B: ",b)
                # print("this is b",b)
                self.s1.push(b)
                # current_2=current_2.next
            


    def dequeue(self):
        """
        do dequeue with push and pop methods from Stack using FIFO
        """
        if self.s1.top:
            temp=self.s1.top
            self.s1.top=self.s1.top.next
            temp.next=None
            return temp.value

    def __str__(self):
        """
        return string of Queue
        output-{string}
        """
        output=''
        current=self.s1.top
        while current:
            output+=f"{current.value} -> "
            current=current.next
        output+= "None"
        return output
            
            
if __name__=='__main__':
    q=PseudoQueue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.enqueue("D")


    # # print(q.dequeue())
    print(q,"queue")
    # # print(q.s2.top.value)
    print("dequeue",q.dequeue())

    print("dequeue",q.dequeue())
    print("dequeue",q.dequeue())
    print("dequeue",q.dequeue())
    print("dequeue",q.dequeue())




