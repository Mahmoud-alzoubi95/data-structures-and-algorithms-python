# Quick Sort

QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

1. Always pick first element as pivot.
2. Always pick last element as pivot (implemented below)
3. Pick a random element as pivot.
4. Pick median as pivot.

# Psudocode

```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```


# Steps

The sample : `[8,4,23,42,16,15]`

<img src ="/assets/q_sort/sample.PNG">

## Step 1 :

Select the pivot : 

<img src ="/assets/q_sort/pi.PNG">

then move it to the end

<img src ="/assets/q_sort/pi_to_end.PNG">


## step 2 :

Partition the subarray whre the left point to index `0` and the right point to index `4`

## step 3 :

Move the left bound to the right until it reaches a value greater than or equal to the pivot. in this case it will be `42`

<img src ="/assets/q_sort/elem42.PNG">

## step 4 :
Move the right bound to the left until it crosses the left bound or finds a value less than the pivot. Swape the left bound (42) with the right bound (16)

<img src ="/assets/q_sort/swap42_16.PNG">

## step 5 :

When the right bound crosses the left bound, all elements to the left of the left bound are less than the pivot and all elements to the right are greater than or equal to the pivot.

<img src ="/assets/q_sort/swap42_23.PNG">

## step 6 :
Select the pivot (4) and move the puvot to the end. Then Move the left bound to the right until it reaches a value greater than or equal to the pivot. it will reach (8). Move the right bound to the left until it crosses the left bound or finds a value less than the pivot. Bound have crossed.
**When** the right bound crosses the left bound, all elements to the left of the left bound are less than the pivot and all elements to the right are greater than or equal to the pivot.


<img src ="/assets/q_sort/8.PNG">

Move the pivot to its final location. at index 3

<img src ="/assets/q_sort/index_3.PNG">

## step 7 :

Select the pivot (15)

<img src ="/assets/q_sort/pi15.PNG">

And move it to the end,then partition the subarray.

<img src ="/assets/q_sort/partionwith15.PNG">

## step 8 :

Move the left bound to the right until it reaches a value greater than or equal to the pivot. It will reach index `1`.

Move the right bound to the left until it crosses the left bound or finds a value less than the pivot. It will reach index `2`.

then swap the selected values

<img src ="/assets/q_sort/swap6_8.PNG">


## step 9 :

Move the bound untill they crossed,

<img src ="/assets/q_sort/16_15.PNG">

Then swap 16 with 15 

<img src ="/assets/q_sort/swap15_16.PNG">

## step 10 :

Left sublist contains a single element which means it is sorted. And right sublist contains a single element which means it is sorted.
Which means **Done sorting!**

<img src ="/assets/q_sort/done_sorting.PNG">



Efficency
Time: O(n log n)
The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.

Space: O(1)
No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).

Worst case : O(n2)















