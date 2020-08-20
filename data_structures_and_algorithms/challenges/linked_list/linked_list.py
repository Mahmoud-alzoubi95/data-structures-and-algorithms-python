class Node():
    def __init__(self,data):
        self.data=data
        self.next=None






class LinkedList():
    def __init__(self):
        self.head=None

    def append_data(self,data):
        """
        Put docstring here
        """
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            current= self.head
            while current.next:
                current=current.next
            current.next=new_node


    def insert(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def includes(self,data):
        current=self.head
        while current:
            if data==current.data:
                print("True")
                return True
            else:
                current=current.next
        print("False")
        return False

    def __str__(self):

        current=self.head
        output=""
        while current:
            output+=f"{ current.data } -> "
            current=current.next
        output+=f"{current}"
        
        return output

    def insert_btw(self,pre_data,data): # This method to enter new data between existance data
        try:
            do
        except  :

            return ('This function Does not been established yet')






    
if __name__=='__main__':
    bird=LinkedList()
    a=bird.append_data("Eagle")
    # bird.append_data("Eagle")
    bird.append_data("Dov")
    bird.append_data("Hawk")
    print(f""" "{bird}" """)
    # bird.includes("awk")
    bird.insert_btw("Hawk","Woody_Packer") # this for handle the error
    