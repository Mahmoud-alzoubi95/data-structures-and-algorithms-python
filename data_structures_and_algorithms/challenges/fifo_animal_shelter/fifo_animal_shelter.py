class Cat:
    def __init__(self,name,catagory="Cat"):
        self.name=name
        self.catagory=catagory
        self.next=None


class Dog:
    def __init__(self,name,catagory="Dog"):
        self.name=name
        self.catagory=catagory
        self.next=None

class Queue:
    

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, name,catagory):
        if catagory=="Cat":
            node = Cat(name)
        elif catagory=="Dog":
            node= Dog(name)
        else:
            return "Can't be enqueue"
        # Special case: if empty queue
        # f -> 1 <- r
        if not self.front and not self.rear:
            self.front = node
            self.rear = node

        old_rear = self.rear
        self.rear = node
        old_rear.next = self.rear
        # front -> 1 -> 2 -> 3 <- rear


    # def dequeue(self):
    #     """
    #     dequeue(extract) Node that fristly entered
    #     """
    #     if self.front:
    #         temp=self.front
    #         self.front=temp.next
    #         temp.next=None
    #         if self.rear.value==temp.value:
    #             """
    #             if statment to check if the last node was dequeued
    #             then make the self.front point to None
    #             """
                
    #             self.front=None
    #         return temp.value
    #     else:
    #         return "The queue is Empty"
    def dequeue_animal(self,catagory):
        """
        dequeue(extract) Node that fristly entered
        """

        if self.front:
            temp=self.front
            while temp:
                if temp.catagory==catagory:
                    print("nnnnnnnn")
                    self.front=temp.next
                    temp.next=None
                    if self.rear.name==temp.name:
                        """
                        if statment to check if the last node was dequeued
                        then make the self.front point to None
                        """
                        
                        self.front=None
                    # print(temp.name)
                    return temp.name
                    # else:
                    #     temp=temp.next
                    #     if self.front==self.rear:
                    #         break
                else:
                    # print("qqqqqqqqqqqqqq")
                    temp=temp.next
                    if self.front==self.rear:
                        break
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
            print(current.name)
            output+=f"{current.name} -> "
            current=current.next
            # print(current.__str__())
            if self.front==self.rear:
                break
        output+= f"{None}"
        return output


if __name__=='__main__':
    q_animal=Queue()
    q_animal.enqueue("Sherry","Cat")
    q_animal.enqueue("Sherry","Cat")
    q_animal.enqueue("Sherry","Cat")
    q_animal.enqueue("Sherry","Cat")

    q_animal.enqueue("Oscar D","Dog")
    print(q_animal.dequeue_animal("Dog"))
    # print(q_animal)
    # print(q_animal)