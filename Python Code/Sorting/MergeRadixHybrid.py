import MergeSort
import RadixSort_Int

import random
import time
import math

def HybridSort(arr,n,k):
    print()
    if len(arr) <= 1:
        return arr
    
    x = n - (math.pow(2,k)/math.e)
    a = math.ceil(x)
    print("[Sorting] split: " + str(a))
    
    if a  <= 0:
        print("[Sorting] no split")
        return MergeSort.MergeSort(arr)
    
    left = RadixSort_Int.RadixSort(arr[:a])
    right = MergeSort.MergeSort(arr[a:])
    merge = []
    
    #print("[Sorting] Radix: " + str(left))
    #print("[Sorting] Merge: " + str(right))
    
    i = 0
    j = 0
    
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
    
    print()
    return merge
    
def ErrorCheck(arr):
    erroPairs = []
    error = False
    for i,a in enumerate(arr):
        if i == len(arr) - 1:
            break
        if arr[i] > arr[i+1]:
            erroPairs.append((arr[i],arr[i+1]))
            error = True
    return (error,erroPairs)
        

n = random.randint(math.pow(10,2),math.pow(10,5))
k = random.randint(1,5)
arr = []
for _ in range(n):
    arr.append(random.randint(0,math.pow(10,k)))

#print("[Main] Here is the array/list: " + str(arr))
print()

st1 = time.process_time()
print("[Main] starting Hybrid...")
arr2 = HybridSort(arr,n,k)
print("[Main] Hybrid finished.")
et1 = time.process_time()
er = ErrorCheck(arr2)
if er[0]:
    print("[Main] Errors found: " + str(er[1]))
else:
    print("[Main] no errors in Hybrid")
print()

st2 = time.process_time()
print("[Main] starting Merge...")
arr2 = MergeSort.MergeSort(arr)
print("[Main] Merge finished.")
et2 = time.process_time()
er = ErrorCheck(arr2)
if er[0]:
    print("[Main] Errors found: " + str(er[1]))
else:
    print("[Main] no errors in Merge")
print()

st3 = time.process_time()
print("[Main] starting Radix...")
arr2 = RadixSort_Int.RadixSort(arr)
print("[Main] Radix finished.")
et3 = time.process_time()
er = ErrorCheck(arr2)
if er[0]:
    print("[Main] Errors found: " + str(er[1]))
else:
    print("[Main] no errors in Radix")
print()

T = et1 - st1
print("[Sorting] n: " + str(n) + "| k: " + str(k))
print("[Main] Aproximate Time of Hybrid: " + str(T))
T = et2 - st2
print("[Main] Aproximate Time of Merge: " + str(T))
T = et3 - st3
print("[Main] Aproximate Time of Radix: " + str(T))

