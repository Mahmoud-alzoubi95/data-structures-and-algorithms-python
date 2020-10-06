class Node:
    def __init__(self,value):
        self.value=value
        self.right=self.left=None

class Tree:
    def __init__(self):
        self.root=None
MIN=-1000000000
MAX=1000000000
def is_BST(node):
    return is_BST_result(node,MIN,MAX)

def is_BST_result(node,min,max):
    if not node:
        return True

    if node.value <min or node.value>max:
        return False
    return (is_BST_result(node.left,min,node.value -1) and is_BST_result(node.right,node.value +1,max))
    #  return (isBSTUtil(node.left, mini, node.data -1) and
    #     #   isBSTUtil(node.right, node.data+1, maxi)) 
    
if __name__ == "__main__":
    t1=Tree()
    # t1.root = Node(1) 
    # t1.root.left = Node(2) 
    # t1.root.right = Node(3) 
    # t1.root.left.left = Node(4) 
    # t1.root.left.right = Node(5) 
    # print(max_depth(t1.root))
    MIN=-1000000000
    MAX=1000000000
    root = Node(4) 
    root.left = Node(2) 
    root.right = Node(5) 
    root.left.left = Node(1) 
    root.left.right = Node(3)
    # print(is_BST(root))
    # print(root)
    print(dir(float('-inf')))