class Node:
    def __init__(self,value):
        self.value=value
        self.right=self.left=None

class Tree:
    def __init__(self):
        self.root=None

def max_depth(node):
    if not node:
        return 0
    # else:
    lDepth=max_depth(node.left)
    rDepth=max_depth(node.right)

    if lDepth>rDepth:
        return lDepth+1
    else:
        return rDepth+1

if __name__ == "__main__":
    t1=Tree()
    t1.root = Node(1) 
    t1.root.left = Node(2) 
    t1.root.right = Node(3) 
    t1.root.left.left = Node(4) 
    t1.root.left.right = Node(5) 
    print(max_depth(t1.root))