import math

def Quicksort(Arr,start,end):
    if start > end:
        return Arr
    p,Arr = Partition(Arr,start,end)
    Arr = Quicksort(Arr,start,p-1)
    Arr = Quicksort(Arr,p+1,end)
    return Arr

def Partition(Arr, start, end):
    
    left = start
    right = end
    pivot = start
    
    while (left < pivot) or (right > pivot):
        if (left < pivot):
            if Arr[left] > Arr[pivot]:
                temp = Arr[pivot]
                Arr[pivot] = Arr[left]
                Arr[left] = temp
            else:
                left += 1
        if (right > pivot):
            if Arr[right] < Arr[pivot]:
                temp = Arr[pivot]
                Arr[pivot] = Arr[right]
                Arr[right] = temp
            else:
                right -= 1
    
    return (pivot, Arr)     


arr = [12,1,41,52,12,63,812,47,93,3,27,47,0,53,14]

print(arr)
arr = Quicksort(arr,0,(len(arr) - 1)) 
print(arr)     