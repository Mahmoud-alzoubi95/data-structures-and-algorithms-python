# Python program to swap nodes 

from memory_profiler import profile

#   def func():
#      your function

# A binary tree node 
class Node: 

	# constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

# A utility function swap left node and right node of tree 
# of every k'th level 
# @profile(precision=4)

def swapEveryKLevelUtil(root, level, k): 
	
	# Base Case 
	if (root is None or (root.left is None and
						root.right is None ) ): 
		return

	# If current level+1 is present in swap vector 
	# then we swap left and right node 
	if (level+1)%k == 0: 
		root.left, root.right = root.right, root.left 
	
	# Recur for left and right subtree 
	swapEveryKLevelUtil(root.left, level+1, k) 
	swapEveryKLevelUtil(root.right, level+1, k) 

	
# This function mainly calls recursive function 
# swapEveryKLevelUtil 
def swapEveryKLevel(root, k): 
	
	# Call swapEveryKLevelUtil function with 
	# initial level as 1 
	swapEveryKLevelUtil(root, 1, k) 
def swape_two(root,t1,t2):
    output=[]
    def _walk(root,t1,t2):
        if not root:
            return
        if root.data==t1:
            # print(t1)
            output.append(root)
        if root.data==t2:
            # print(t2)

            output.append(root)
        if len(output)==2:
            output[0].data, output[1].data = output[1].data,output[0].data
			# temp=output[0]
			# output[0]=output[1]
			# output[1]=temp
            # print("output is : ",output[0].data)

            
        _walk(root.left,3,8)
        _walk(root.right,3,8)
    # return output[0].data,output[1].data
    _walk(root,t1,t2)
    return output
     
# Method to find the inorder tree travesal 
def inorder(root): 
	
	# Base Case 
	if root is None: 
		return
	inorder(root.left) 
	print (root.data,) 
	inorder(root.right) 

# Driver code 
""" 
		1 
		/ \ 
	2	 3 
	/	 / \ 
	4	 7 8 
"""
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.right.right = Node(8) 
root.right.left = Node(7) 

k = 1
# print ("Before swap node :")
# inorder(root) 

# swapEveryKLevel(root, k) 

# print ("\nAfter swap Node : ")
# inorder(root) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
inorder(root)
# print(swape_two(root,1,7))
swape_two(root,7,4)
inorder(root)

