from data_structures_and_algorithms.challenges.hashtable.linkedlist_assets import LinkedList
# from linkedlist_assets import LinkedList





class Hashtable:


    def __init__(self,size = 1024):
        self.map = [None] * size
        self.size = size

    def hash(self,key):
        hashed_total = 0
        for char in key:
            hashed_total += ord(char)
        return hashed_total * 7 % self.size

    def add(self,key,value):

        hashed_key = self.hash(key)

        if self.map[hashed_key] == None:

            self.map[hashed_key] = LinkedList(key)
            


        elif self.contains(key):
            
            """ 
            Thid method is for the challenging part
            "If duplicate key, replace the old value with new value"

            """
            hash=self.map[hashed_key]
            # print(self.map[hashed_key])
            if hash.includes(value):
                
                # print("Repalce old with new done")
                hash.replace((key,value))
                return "Repalce old with new done"
                
        
        self.map[hashed_key].add((key, value))

        return f"Add method appended {value} to the key {key}"
        

    def get(self,key):
        
        hashed_key=self.hash(key)
        # print(hashed_key)
        if self.map[hashed_key]:
            print("In get method")
            # self.map[hashed_key].head
            print(self.map[hashed_key])
            return self.map[hashed_key]
        else:
            return None
        

    def contains(self, key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            return True
        else:
            return False

    def __str__(self):
        """
        method to format the hash table shap when printing it
        """
       
        arr=[]
        
        for i in self.map:
            # print(i)
            if i:
                arr.append(i.name)
            else:
                arr.append(None)
                

        return 'Hashtable  is  %s' %(arr)
    

        




if __name__ == "__main__":
    t = Hashtable()
    one=t.hash('name')
    two=t.hash('ohm')
    a1=t.add('name','moh')
    a2=t.add('name','moh')
    

    # print(t.contains('name'))
    # # print(t.contains('nhj'))
    # print(t.get('name'))
    # print(t.get('nkj'))

    # print(t.map[871])
    # print(a2)
    # # print(two)
    # for x,i in enumerate(t.map):
    #     print(x,i)
    # print(t)
    # t.add('Fruit','Apple')
    # t.add('Fruit','Apple')

    # assert t.add('Fruit','Apple')=="Repalce old with new done"
    


    
    # expected ="Repalce old with new done"
    # actual = pre.add('Fruit','Apple')
    # assert expected==actual