import math


#radix sort is really useful when comparing things that need to be interated through to be compared.
#for now i will work with radix of integers.
def RadixSort(arr):
    if len(arr) <= 1:
        return arr
    
    m = max(arr)
    size = getOrder(m) + 1
    
    for i in range(size):
        arr = Arrange(arr,i + 1)
    
    return arr

def getOrder(n):
    order = 1
    place = 10
    while n/place > 1:
        order += 1
        place *= 10
    return order

def getFaceValue(n,p):
    val = n//math.pow(10,p-1)
    return int(val%10)

def Arrange(arr,i):
    radix = [[] for _ in range(10)]
    for a in arr:
        #print("a: " + str(a) + " i: " + str(i) + " getFaceValue(a,i): " + str(getFaceValue(a,i)))
        radix[getFaceValue(a,i)].append(a)
    
    #print(radix)
    new = []
    for n in radix:
        new.extend(n)
    return new
    