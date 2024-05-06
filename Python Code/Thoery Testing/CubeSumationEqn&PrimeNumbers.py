import math


def CubedSumationTerm(n):
    return 3*pow(n,2) + 3*(n) + 1

def isPrime(n,bucket=[2,3,5]):
    for item in bucket:
        if not n%item: return (False,bucket,item)
    
    test_num = max(bucket) + 1
    while test_num < n:
        if QuickPrime(test_num): 
            bucket.append(test_num)
        if not n%test_num: 
            return (False,bucket,test_num)
        test_num += 1
    return (True,bucket,1)

def QuickPrime(n):
    if not n%2: return False
    if not n%3: return False
    if not n%5: return False
    m = 7
    root = math.sqrt(n)
    while m <= root:
        if not n%m: return False
        m += 1
    return True

prime = CubedSumationTerm(9)
result = isPrime(prime)
print("Testing:",prime,"\nis Prime:",result[0],"\nPrime Count:", len(result[1]) + 1,"\nMultiple:",result[2])   