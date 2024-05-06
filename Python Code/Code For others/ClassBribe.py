import math
import random

def ListMethod(lst,k):
    counter = 0
    for index, value in enumerate(lst): 
        for index2, value2 in enumerate(lst[index+1:]): # (n) + (n-1) + (n-2) +...+ 1 = (n^2 + n)/2
            sum = (value + value2) % k
            if sum == 0: counter += 1
    # this takes O(n^2) time.
    return counter

def DictionaryMethod(pieces, k):
    # the only way you can add a p_2 to p_1 and get m*k is if p_2 is the k-moduler inverse of p.
    # i.e: p_2%k + p_1%k = k => p_2%k = (k - p_1%k)%k
    
    # if we then group the pieces by their %k then to get the # of p_2 that are inverses of p_1
    # would be the number of elements in the p_2%k group. (excluding the when p_1 is it own inverse)
    
    groups = {}
    for index, value in enumerate(pieces): # run through all the values once. takes O(n) time
        key = value % k
        if key in groups.keys(): groups[key].append(value)
        else: groups[key] = [value]
    
    counter = 0
    for index, p in enumerate(pieces): # runs through all the values once again takes O(n) time
        mod = p%k
        counter += len(groups[(k-mod)%k]) # count all the elements that are p's inverse. 
        if mod == (k-mod)%k: counter -= 1 # account for when the p is it's own inverse.
        groups[mod].remove(p)
    
    return counter
        


k = 5
lst = [75,95,3,38,99,45,28,17,46,5,34,79,44,50,58,22,7,85,62,45] # n is the length of the lst

print(ListMethod(lst,k))
print(DictionaryMethod(lst,k))

