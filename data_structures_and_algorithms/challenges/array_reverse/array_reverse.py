def reverse_array(arr):
    """Reverses a list

    Args:
        arr (list): python list

    Returns:
        [list]: list in reversed form
    """
    # put your function implementation here
    return arr


if __name__=='__main__':

    print("challenge number :1 ( revers array with out built-in function")

arrayone=[1,2,3,4,5,6,7,8,9]
list=[]
for i in range(len(arrayone),0,-1):
    list.append(i)

print(" \n")

print("The input array",arrayone)
print(" \n")
print("The output",list)
