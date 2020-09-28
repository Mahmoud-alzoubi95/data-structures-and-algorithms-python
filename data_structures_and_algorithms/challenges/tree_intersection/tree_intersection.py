    # Python3 program of iterative traversal based 
    # method to find common elements in two BSTs. 

    # A utility function to create a new node 
class newNode: 
    def __init__(self, key): 
        self.key = key 
        self.left = self.right = None

    # Function two print common elements 
    # in given two trees 
def tree_intersection(root1, root2): 

    
    s1 = [] 
    s2 = [] 
    arr = []
    while True: 
      
        if root1: 
            
            s1.append(root1) 
            root1 = root1.left 

        elif root2: 
            s2.append(root2) 
            root2 = root2.left 

        
        elif len(s1) != 0 and len(s2) != 0: 
            root1 = s1[-1] 
            root2 = s2[-1] 

            
            if root1.key == root2.key: 
                # print(root1.key, end = " ") 
                arr.append(root1.key)
                s1.pop(-1) 
                s2.pop(-1) 

               
                root1 = root1.right 
                root2 = root2.right 

            elif root1.key < root2.key: 
               
                s1.pop(-1) 
                root1 = root1.right 

                root2 = None
            elif root1.key > root2.key: 
                s2.pop(-1) 
                root2 = root2.right 
                root1 = None

        else: 
            break
    return arr

    
# def inorder(root): 
#     if root: 
#         inorder(root.left) 
#         print(root.key, end = " ") 
#         inorder(root.right) 

def insert(node, key): 

   
    if node == None: 
        return newNode(key) 

    if key < node.key: 
        node.left = insert(node.left, key) 
    elif key > node.key: 
        node.right = insert(node.right, key) 
 
    return node 

 
if __name__ == '__main__': 

  
    root1 = None
    root1 = insert(root1, 150) 
    root1 = insert(root1, 100) 
    root1 = insert(root1, 75) 
    root1 = insert(root1, 160) 
    root1 = insert(root1, 250) 
    root1 = insert(root1, 200) 
    root1 = insert(root1, 350)
    root1 = insert(root1, 300) 
    root1 = insert(root1, 500)
    root1 = insert(root1, 125) 



    root2 = None
    root2 = insert(root2, 42) 
    root2 = insert(root2, 100) 
    root2 = insert(root2, 15) 
    root2 = insert(root2, 600) 
    root2 = insert(root2, 160)
    root2 = insert(root2, 200) 
    root2 = insert(root2, 350) 
    root2 = insert(root2, 4)
    root2 = insert(root2, 500) 
    root2 = insert(root2, 175)
    root2 = insert(root2, 125) 




    print(tree_intersection(root1, root2) )



