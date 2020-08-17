def reverse_array(arr):
    """Reverses a list

    Args:
        arr (list): python list

    Returns:
        [list]: list in reversed form
    """
    # put your function implementation here
    return arr



print("challenge")

arrayone=[1,2,3,4,5,6,7,8,9]
list=[]
for i in range(len(arrayone),-1,-1):
    list.append(i)
print(list)
