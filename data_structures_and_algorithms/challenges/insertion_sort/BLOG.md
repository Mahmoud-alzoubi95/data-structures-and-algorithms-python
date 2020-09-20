# Selection Sort

Selection Sort is a sorting algorithm that traverses the array multiple times as it slowly builds out the sorting sequence. The traversal keeps track of the minimum value and places it in the front of the array which should be incrementally sorted.

## Pseudocode

```
SelectionSort(int[] arr)
    DECLARE n <-- arr.Length;
    FOR i = 0; i to n - 1  
        DECLARE min <-- i;
        FOR j = i + 1 to n
            if (arr[j] < arr[min])
                min <-- j;

        DECLARE temp <-- arr[min];
        arr[min] <-- arr[i];
        arr[i] <-- temp;
```

## Trace

Sample Array: `[4 ,7 ,9, 40, 11, 10]`

### Pass 1 :

<img src="/assets/insertion_sort/insertion_sort_1.png">

#### In the first pass through of the selection sort, we evaluate if there is a smaller number in the array than what is currently present in index 0. In this case We find this smaller number -which is equal to 5- right away in index 0, So it “swaps” with itself. The minimum value gets updated to remember this index. At the end of the evaluation, the smaller number will be swapped with the current value in index i. This results in our smallest number of our array being placed first.

### Pass 2 :

<img src="/assets/insertion_sort/insertion_sort_5_2.png">

#### The second pass through the array evaluates the remaining values in the array to see if there is a smaller value other than the current position of i. 5 is the 2nd smallest number in the array, so it “swaps” with itself. The minimum value does not change at all during the iteration of this pass.

### Pass 3 :

<img src="/assets/insertion_sort/insertion_sort_3.png">

#### The Third pass through the array evaluates the remaining values in the array to see if there is a smaller value other than the current position of i. 5 is the 3rd smallest number in the array, so it “swaps” with itself. The minimum value does not change at all during the iteration of this pass.

### Pass 4 :

<img src="/assets/insertion_sort/insertion_sort_4.png">

#### The 4th pass through on the array proves that 10 is the next smallest number in the array, and as a result, switches places with the 40.

### Pass 5 :

<img src="/assets/insertion_sort/insertion_sort_5.png">

#### The 5th pass through the array evaluates the remaining values in the array to see if there is a smaller value other than the current position of i. 7 is the 5th smallest number in the array, so it “swaps” with itself. The minimum value does not change at all during the iteration of this pass.


#### On its final iteratation through the array, it will swap places with itself as it evaluates the value against itself.

#### After this iteration, i will increment to 6, forcing it to break out of the outer for loop and leaving our array now sorted.


## Efficency

### Time: O(n^2)
    The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.
### Space: O(1)
    No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).