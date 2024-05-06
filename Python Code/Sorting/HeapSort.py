import math

def Swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def parent(index):
    return math.floor(index/2)

def left(index):
    return 2*index

def right(index):
    return 2*index + 1

def BuildHeap(arr):
    heap = [0]
    
    for a in arr:
        heap = HeapInsert(heap,a)
    print("new heap: " + str(heap))
    return heap
        
def HeapInsert(heap, term):
    heap.append(term)
    heap[0] += 1
    
    i = heap[0]
    p = parent(i)
    while i > 1 and heap[i] < heap[p]:
        heap = Swap(heap,i,p)
        i = p
        p = parent(i)
    return heap

def HeapPop(heap):
    if heap[0] < 1:
        return [None,heap]
    
    heap [0] -= 1
    val = heap[1]
    heap[1] = heap[-1]
    heap.pop(-1)
    
    i = 1
    l = left(i)
    r = right(i)
    
    while l <= heap[0] or r <= heap[0]:
        small = i
        if (l <= heap[0]) and (heap[small] >= heap[l]):
            small = l
        if (r <= heap[0]) and (heap[small] >= heap[r]):
            small = r
        if small == i:
            break
        
        heap = Swap(heap,i,small)
        i = small
        l = left(i)
        r = right(i)
            
    return [val, heap]
        
def HeapSort(arr):
    heap = BuildHeap(arr)
    lst = []
    while heap[0] > 0:
        val, heap = HeapPop(heap)
        lst.append(val)
    return lst
    
    

arr = [12,1,41,52,12,63,812,47,93,3,27,47,0,53,14]

print(arr)
arr = HeapSort(arr) 
print(arr)    