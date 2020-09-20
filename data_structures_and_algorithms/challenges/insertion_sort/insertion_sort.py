def InsertionSort(arr):
    n=len(arr)
    for i,elem in enumerate(arr):
        temp= elem
        j=i-1
        while j>=0 and temp < arr[j]:
            arr[j+1]=arr[j]
            j -=1

        arr[j+1]=temp
    return arr


a= [4 ,7 ,9, 40, 11, 10]
b= [20,18,12,8,5,-2]
c=[5,12,7,5,5,7]
d= [2,3,5,7,13,11]
InsertionSort(a)
InsertionSort(b)
InsertionSort(c)
InsertionSort(d)


print(a)
print(b)

print(c)

print(d)
