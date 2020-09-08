# from data_structures_and_algorithms.challenges.tree.tree import BinaryTree
class Node:
    """
    Declare Nodes with its values
    No return
    """
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self):
        self.root=None


    
    # def preOrder(self):
    #     """
    #     Return a collection sorted by pre order
    #     output-{list}
    #     """
    #     output=[]
    #     def _walk(node):
    #         if not node:
    #             return
    #         # print(node.value)
    #         try :
    #             if node.value % 5 ==0 and node.value % 3==0:
    #                 node.value='FizzBuzz'
    #             elif node.value % 5 ==0 :
    #                 node.value='Buzz'
    #             elif noed.value % 3 ==0:
    #                 node.value='Fizz'
    #             else :
    #                 node.value=str(node.value)
    #         except:
    #             print(" Error in this node")

    #         # output.append(node.value)
    #         _walk(node.left)
    #         _walk(node.right)

    #     _walk(self.root)
    #     return output

def FizzBuzzTree(ary_tree):
    """
    Return a collection sorted by pre order
    output-{list}
    """
    output=[]
    def _walk(node):
        if not node:
            return
        # print(node.value)
        try :
            # print(node.value,node.value % 5 ==0 and node.value % 3==0)
            if node.value % 5 ==0 and node.value % 3==0:
                node.value='FizzBuzz'
            elif node.value % 5 ==0 :
                print(node.value,node.value % 5 ==0)
                node.value='Buzz'
                print(node.value)
            elif node.value % 3 ==0:
                node.value='Fizz'
            else :
                node.value=str(node.value)
        except:
            print(f"Error in this node which its value is  : {node.value}")

        output.append(node.value)
        _walk(node.left)
        _walk(node.right)

    _walk(ary_tree.root)
    return output




if __name__ == "__main__":
    # bt = BinaryTree()
    # bt.root = Node(7)
    # bt.root.left = Node(13)
    # bt.root.right = Node(5)
    # bt.root.left.left = Node(8)
    # bt.root.left.right = Node(9)
    # bt.root.right.left = Node(1)
    # bt.root.right.right = Node(-4)
    # bt.root.right.right.right = Node("m")
    # bt=BinaryTree()
    # bt.root=Node(2)
    # bt.root.left=Node(4)
    # bt.root.left.right=Node(30)
    # bt.root.left.left=Node(12)
    # bt.root.right=Node(7)
    # bt.root.right.right=Node(18)
    # bt.root.right.left=Node(10)
    bt=BinaryTree()
    bt.root=Node(2)
    bt.root.left=Node(4)
    bt.root.left.right=Node(30)
    bt.root.left.left=Node(12)
    bt.root.left.left.right=Node("A")
    bt.root.left.left.left=Node("B")
    bt.root.right=Node("m")
    bt.root.right.right=Node(18)
    bt.root.right.left=Node(10)


    print(FizzBuzzTree(bt))