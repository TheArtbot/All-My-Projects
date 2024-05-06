
def BinearySearch(tr,lst, index):
    if len(lst) <= 1:
        print(index)
        return index
    
    mid = len(lst)//2
    
    if lst[mid] == tr:
        print(index)
        return index
    if lst[mid] > tr:
        index += mid//2
        return BinearySearch(tr,lst[mid:],index)
    index -= mid//2
    return BinearySearch(tr,lst[:mid],index)

def BinearySort(Arr):
    if len(Arr) <= 1:
        return Arr
    
    p = BinearySearch(Arr[0],Arr,0)
    temp = Arr[p]
    Arr[p] = Arr[0]
    Arr[0] = temp
    
    left = []
    right = []
    
    if (p > 0): 
        left = BinearySort(Arr[:p - 1])
    if (p < len(arr)-1): 
        right = BinearySort(Arr[p + 1:])
    
    m = []
    m.extend(left)
    m.extend(right)
    
    return m

arr = [12,1,41,52,12,63,812,47,93,3,27,47,0,53,14]
lst =[]
lst.extend(arr)

print(lst)
lst = BinearySort(lst) 
print(lst) 