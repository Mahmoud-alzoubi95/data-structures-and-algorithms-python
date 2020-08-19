if __name__=='__main__':
    print(" ***** This is Code Challenge :2 this is for array-shift ")

list=[2,4,6,8]
def insertShiftArray(arr,num):
    new_arr=[]

    for i in arr:
        
        if arr.index(i)==len(arr)-1:
                arr.append(num)
                # break
                return f"from first{arr}"
        
        if i>num:
            
            if arr.index(i)==len(arr)-1:
                arr.append(num)
                # break
                return f"from first{arr}"
            else:
                new_arr = arr.copy()[0:arr.index(i):]
                new_arr2=arr.copy()[arr.index(i)::]
                new_arr.append(num)
                for x in new_arr2:
                    new_arr.append(x)
                
                return new_arr
            # return arr.index(i)

    # return num









list2=[4,8,15,23,42]
print(insertShiftArray(list,5))
print(insertShiftArray(list2,16))
print(insertShiftArray([1,2,3],0))

# Welcom message
if __name__=='__main__':
    print(" ***** This is Code Challenge :2 this is for array-shift ")