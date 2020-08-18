import random
# Returns index of x in arr if present, else -1 
def binary_search(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
# Test array 
# arr = [ 1,2,5,6,8,9,10,11,13,14,50,60,70,80,100 ] 
arr=[25, 120, 156, 167, 217, 263, 327, 377, 768, 855, 991, 1123, 1267, 1315, 1366, 1397, 1593, 1612, 1790, 1923, 1938, 1940, 2037, 2293, 2301, 2552, 2678, 2691, 2741, 2837, 2915, 2956, 3051, 3067, 3311, 3384, 3512, 3696, 3731, 3786, 3820, 4253, 4310, 4312, 4527, 4642, 4730, 4865, 4903, 4922] 
x=25
# x = 2
  
# Function call 
result = binary_search(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is exixt at ", str(result)) 
else: 
    print("The does not exist ") 
# print(len(list))

# def long_arr(l,x,a=0):
#     list=["obj"]*l





def long_arr(l,x): # x is the desired number we want to search on
  list=[1]*l # make a list with length L
  print("mmm")
  for i in range(0,l):
    
    list[i]=i
#   list.sort()
  print(list, 0, len(list)-1,x)
  return binary_search(list, 0, len(list)-1,x )
print(long_arr(100,50))