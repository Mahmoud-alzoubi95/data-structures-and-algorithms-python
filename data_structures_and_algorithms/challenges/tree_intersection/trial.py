

# # from data_structures_and_algorithms.challenges.tree.tree import BinarySearchTree
# from data_structures_and_algorithms.challenges.tree.tree import BinarySearchTree




# def inter(tree1,tree2):
    
#     t1=tree1.root
#     t2 = tree2.root
#     # print(t1,t2)
#     s1=[]
#     s2=[]
#     arr=[]
#     while 1:
#         if t1:
#             print(t1.value)
#             s1.append(t1)
#             t1=t1.left
#         elif t2:
#             s2.append(t2)
#             t2 = t2.left
#             print("second if enterd")

#         elif len(s1) != 0 and len(s2) != 0: 
#             t1 = s1[-1]  
#             t2 = s2[-1] 
#             print(t1,t2)

#             if t1.value == t2.value: 
#                 arr.append(t1.value)
#                 print(t1.value,"VAlue")
                
#                 s1.pop(-1)  
#                 s2.pop(-1) 

                
#                 t1 = t1.right  
#                 t2 = t2.right 
            
#             elif t1.value < t2.value: 
            
#                 s1.pop(-1) 
#                 t1 = t1.right  

                
#                 t2 = None
#             elif t1.value > t2.value: 
#                 s2.pop(-1) 
#                 t2 = t2.right  
#                 t1 = None

        
#         else: 
#             break
#         return arr








    
# if __name__ == "__main__":
#     # print(bst1.contains(5))
#     # print(bst1.root.left.value)
#     # print(intersection(bst1,bst2))
#     #-------#
#     bst1=BinarySearchTree()
#     bst1.add(5)
#     bst1.add(1)
#     bst1.add(10)
#     bst1.add(0)
#     bst1.add(4)
#     bst1.add(7)
#     bst1.add(9)


#     bst2=BinarySearchTree()
#     bst2.add(10)
#     bst2.add(1)
#     bst2.add(20)
#     bst2.add(4)
#     bst2.add(9)
#     print(inter(bst1,bst2))









# #--------#
# # 4 7 9 10

# # def intersection(tree1,tree2):
# #     arr=[]
# #     t1 = tree1.root
# #     t2 = tree2.root
# #     if t1.value == t2.value:
# #         arr.append(t1.value)
# #     for i in range(5):
# #         if t1.left:

# #             t1=t1.left
# #             t2=t2.left
# #         if t1 and t2:
# #             print("left")

# #             if t1.value == t2.value:
# #                 arr.append(t1.value)
# #         if t1.right:

# #             t1=t1.right
# #             t2=t2.right
# #         if t1 and t2:
# #             print("right")
# #             if t1.value == t2.value:
# #                 arr.append(t1.value)
# #     return arr
            


# # bst1=BinarySearchTree()
# # bst1.add(23)
# # bst1.add(8)
# # bst1.add(4)
# # bst1.add(42)
# # bst1.add(27)

# # bst2=BinarySearchTree()
# # bst2.add(23)
# # bst2.add(8)
# # bst2.add(4)
# # bst2.add(42)
# # bst2.add(27)


# #  t1 = insert(t1, 5)  
# # t1 = insert(t1, 1)  
# # t1 = insert(t1, 10)  
# # t1 = insert(t1, 0)  
# # t1 = insert(t1, 4)  
# # t1 = insert(t1, 7)  
# # t1 = insert(t1, 9) 


# # t2 = None
# # t2 = insert(t2, 10)  
# # t2 = insert(t2, 7)  
# # t2 = insert(t2, 20)  
# # t2 = insert(t2, 4)  
# # t2 = insert(t2, 9) 