

#-----------------------------------------------------------LinkedList -----------------#

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self,key):
        self.head=None
        self.name=key
        # print(self.name)

    def add(self,data):
        """
        Method to append data
        """
        
        node=Node(data[1])

        if not self.head:
            self.head = node

        else:
            current = self.head
            while current.next:
                current = current.next
        
        
            current.next = node

    def __str__(self):

        """
        To make format for printing the whole data
        """
        
        current=self.head
        output=""
        while current:
           
            output+=f"{ current.data } -> "
            current=current.next
        output+=f"{current}"

        return output
    def replace(self,data):
        """
        To replace old data with new one
        """
        current=self.head
        while current:
            print(data)
            if data[1]==current.data:
                current.data=data
                
                break
        
       
    def includes(self,data):
        """
        Searching method
        """
        
        current=self.head
        # print("this is current",current)
        # if data[0]==self.name:
        while current:
            
            print(data,current.data)
            if data==current.data:
                print("True")
                return True
            else:
                current=current.next
        # print("False")
        return False


#-----------------------------------------------------------LinkedList -----------------#
