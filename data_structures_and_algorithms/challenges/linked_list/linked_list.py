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

    def insertAfter(self, prev_node, data):
        if not prev_node:
            print("not")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertBefore(self,data,new_data):
        new_node=Node(new_data)
        before=self.head
        # if before==Node:
        #     print("You should use pre_pend method !!!!")
        #     return
        old=before
        while before:
            if before.data==data:
                new_node.next=before
                old.next=new_node
                return
            else:
                old=before
            before=before.next
                

            









    
if __name__=='__main__':
    bird=LinkedList()
    a=bird.append_data("Eagle")
    # bird.append_data("Eagle")
    bird.append_data("Dov")
    bird.append_data("Hawk")
    bird.append_data("Haaaaawk")
    bird.insertBefore("Eagle","before")
    # bird.insertAfter("Hawk",'newOne')
    print(f""" "{bird}" """)
    # bird.includes("awk")
    bird.insert_btw("Hawk","Woody_Packer") # this for handle the error
    