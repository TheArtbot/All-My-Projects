import math


def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = math.ceil(len(arr)/2)
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
    
    i = 0
    j = 0
    merge = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merge.append(left[i])
            i += 1
            continue
        merge.append(right[j])
        j += 1
    
    if i < len(left):
        merge.extend(left[i:])
    elif j < len(right):
        merge.extend(right[j:])
    
    return merge


    