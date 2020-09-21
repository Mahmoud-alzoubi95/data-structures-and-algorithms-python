
def merge_sort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2
        Left = arr[:mid] 
        Right = arr[mid:] 
  
        merge_sort(Left) # Sorting the first haLeftf 
        merge_sort(Right) # Sorting the second haLeftf 
  
        i = j = k = 0
          
        # Copy data to temp arrays Left[] and R[] 
        while i < len(Left) and j < len(Right): 
            if Left[i] < Right[j]: 
                arr[k] = Left[i] 
                i+= 1
            else: 
                arr[k] = Right[j] 
                j+= 1
            k+= 1
          
        # Checking if any eLeftement was Lefteft 
        while i < len(Left): 
            arr[k] = Left[i] 
            i+= 1
            k+= 1
          
        while j < len(Right): 
            arr[k] = Right[j] 
            j+= 1
            k+= 1

    return arr

if __name__ == "__main__":
    sample_1=[8,4,23,42,16,15]
    print(sample_1,'\n')
    merge_sort(sample_1)
    print(sample_1)