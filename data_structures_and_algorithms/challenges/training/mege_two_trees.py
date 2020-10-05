#code
import copy 
print("GfG")
class Node :
    def __init__(self,value):
        
        self.value=value
        self.left=self.right=None
        
        
class Tree:
    
    def __init__(self):
        self.root=None
        
    def pre_order(self):
        output=[]
        
        def _walk(node):
            
            if not node:
                return 
            output.append(node.value)
            _walk(node.left)
            _walk(node.right)
        _walk(self.root)
        return output

    def in_order(self):
        output=[]
        
        def _walk(node):
            
            if not node:
                return 
            _walk(node.left)
            output.append(node.value)
            _walk(node.right)
        _walk(self.root)
        return output
        
    def post_order(self):
        output=[]
        
        def _walk(node):
            
            if not node:
                return 
            _walk(node.left)
            _walk(node.right)
            output.append(node.value)
        _walk(self.root)
        return output       
        
    def merge(self,t1,t2):
        if not t1 :
            return t2

        if not t2:
            return t1
        node_1=copy.deepcopy(t1)
        node_2=copy.deepcopy(t2)
        node_1.value += node_2.value
        
        node_1.left=self.merge(node_1.left,node_2.left)
        node_1.right=self.merge(node_1.right,node_2.right)
        print("from class method",node_1)

        return node_1   

def mergeTree(t1,t2):
    if not t1 :
        
        return t2

    if not t2:
        return t1
    node_1=copy.deepcopy(t1)
    node_2=copy.deepcopy(t2)
    node_1.value += node_2.value
    node_1.left=mergeTree(node_1.left,node_2.left)
    node_1.right=mergeTree(node_1.right,node_2.right)
    print("from function",node_1)
    return node_1     
        

def inorder(node): 
	if (not node): 
		return

	# first recur on left child 
	inorder(node.left) 

	# then print the data of node 
	print(node.value, end = " ") 

	# now recur on right child 
	inorder(node.right) 

if __name__=='__main__':
    t1=Tree()
    t1.root=Node(2)
    t1.root.left=Node(1)
    t1.root.left.left=Node(5)
    t1.root.right=Node(4)
    # print(t1.pre_order())
    t2=Tree()
    t2.root=Node(3)
    t2.root.left=Node(6)
    t2.root.right=Node(1)
    t2.root.left.right=Node(2)
    t2.root.right.right=Node(7)
    
    # t3=Tree()
    # t3.merge(t1,t2)
    # print(t3.pre_order())
    # print(t3.root)
    t3=mergeTree(t1.root,t2.root)
    # t3=Tree()
    # t3.merge(t1.root,t2.root)
    # print(t3.root)
    # print(t3.pre_order())
    inorder(t3)
    # t3.root=t1.root=Node(100)
    # print(t3.root.value)
        
        
        