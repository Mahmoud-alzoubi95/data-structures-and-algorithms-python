# Python3 program to find maximum 
# and minimum in a Binary Tree 

# A class to create a new node 
class newNode: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None
	
# Returns maximum value in a 
# given Binary Tree 
def findMax(root): 
	
	# Base case 
	if not root:
         
		return float("-inf")

	# Return maximum of 3 values: 
	# 1) Root's data 2) Max in Left Subtree 
	# 3) Max in right subtree 
	res = root.data 
	lres = findMax(root.left) 
	rres = findMax(root.right) 
	if (lres > res): 
		res = lres 
	if (rres > res): 
		res = rres 
	return res 

def find_min(node):
	if not node:
		return float("inf")
	
	to_check=node.data
	to_check_left=find_min(node.left)
	to_check_right=find_min(node.right)
	if to_check > to_check_left:
		to_check=to_check_left
	if to_check > to_check_right:
		to_check=to_check_right
	return to_check

if __name__ == '__main__': 
	root = newNode(2) 
	root.left	 = newNode(7) 
	root.right	 = newNode(5) 
	root.left.right = newNode(6) 
	root.left.right.left=newNode(1) 
	root.left.right.right=newNode(11) 
	root.right.right=newNode(9) 
	root.right.right.left=newNode(4) 

	print("Maximum element is", 
				findMax(root)) 
	print("MINimum", find_min(root))

