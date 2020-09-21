# Merge sort
Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

# Psudocode
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
           
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Trace :

Sample array : `[8,4,23,42,16,15]`

### Pass 1 :

<img src="/assets/merge_sort/Slide1.JPG">

The mid point is 3, left part is [8,4,23] and the right part is [42,16,15] Then the recursive function will call for each part.
This is illustrated in steps `1` & `2` in the following picture

### Pass 2 :
<img src="/assets/merge_sort/Slide2.JPG">



The mid point is 1 and the left is `[8]` and the right are `[4,23]` the left part cant be go to the recursion function because its one element but the second will.

### Pass 3 :

<img src="/assets/merge_sort/Slide3.JPG">


the mid point is 1 and left is `[4]` and right is `[23]` and remainnig recursion

### Pass 4 :

<img src="/assets/merge_sort/Slide4.JPG">


8 , 4 , 23 will enter while loop to be sorted and the result is `[4,8,23]` as illustrated in step # `7`

### Pass 5 :

<img src="/assets/merge_sort/Slide5.JPG">


Its the earlier right part turn which is `[42,16,15]`, the mid point is 1 and left is `[42]` and the right is `[16,15]`

### Pass 6 :

<img src="/assets/merge_sort/Slide6.JPG">


the left side is `[16]` and the right is `[15]`

### Pass 7 :

<img src="/assets/merge_sort/Slide7.JPG">


the elements 42,16,15 will be sorted in the while loop as `[15,16,42]` as illustrated in step `13`

### Pass 8 :

<img src="/assets/merge_sort/Slide8.JPG">


the two eralier parts will also be sorted as illustrated in step `15`, **ANd**  the resulting array is **`[4, 8, 15, 16, 23, 42]`**
