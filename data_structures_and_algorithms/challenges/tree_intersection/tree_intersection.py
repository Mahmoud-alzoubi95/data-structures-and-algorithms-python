# from data_structures_and_algorithms.challenges.tree.tree import BinarySearchTree
from data_structures_and_algorithms.challenges.tree.tree import BinarySearchTree

#-------#
bst1=BinarySearchTree()
bst1.add(5)
bst1.add(1)
bst1.add(10)
bst1.add(0)
bst1.add(4)
bst1.add(7)
bst1.add(9)


bst2=BinarySearchTree()
bst2.add(10)
bst2.add(1)
bst2.add(20)
bst2.add(4)
bst2.add(9)


def inter(tree1,tree2):
    """
    Add elements in form of binray search
    No return. Just sorting
    """
    arr=[]
    t1 = tree1.root
    t2 = tree2.root
    if t1.value == t2.value:
        arr.append(t1.value)

    return arr
    # if not self.root:
    #     self.root = Node(value)
    # else:
    current1 = t1
    current2 = t2

    while (current1 or current2):
                if current1.value==current2.value:
                    arr.append(t1.value)

                    # return True
                elif current.value > value: # Got to left
                    
                    if current.left==value:
                        return True
                    current = current.left
                else:
                    
                    if current.right==value:
                        return True
                    current = current.right
        return False









    while (current1 or current2):
        if current.value > value: # Got to left
            if current.left == None: # if current is a leaf
                current.left = Node(value)
                break
            current = current.left
        else:
            if current.right == None: # if current is a leaf
                current.right = Node(value)
                break
            current = current.right

def intersection(tree1,tree2):
    arr=[]
    t1 = tree1.root
    t2 = tree2.root
    if t1.value == t2.value:
        arr.append(t1.value)
    for i in range(5):
        if t1.left:

            t1=t1.left
            t2=t2.left
        if t1 and t2:
            print("left")

            if t1.value == t2.value:
                arr.append(t1.value)
        if t1.right:

            t1=t1.right
            t2=t2.right
        if t1 and t2:
            print("right")
            if t1.value == t2.value:
                arr.append(t1.value)
    return arr
            

    
if __name__ == "__main__":
    # print(bst1.contains(5))
    # print(bst1.root.left.value)
    # print(intersection(bst1,bst2))
    print(inter(bst1,bst2))
#--------#
# 4 7 9 10


# bst1=BinarySearchTree()
# bst1.add(23)
# bst1.add(8)
# bst1.add(4)
# bst1.add(42)
# bst1.add(27)

# bst2=BinarySearchTree()
# bst2.add(23)
# bst2.add(8)
# bst2.add(4)
# bst2.add(42)
# bst2.add(27)


#  root1 = insert(root1, 5)  
# root1 = insert(root1, 1)  
# root1 = insert(root1, 10)  
# root1 = insert(root1, 0)  
# root1 = insert(root1, 4)  
# root1 = insert(root1, 7)  
# root1 = insert(root1, 9) 


# root2 = None
# root2 = insert(root2, 10)  
# root2 = insert(root2, 7)  
# root2 = insert(root2, 20)  
# root2 = insert(root2, 4)  
# root2 = insert(root2, 9) 