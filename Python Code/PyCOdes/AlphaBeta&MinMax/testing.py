import random

def shuffleLst(_lst = []):
    lst = _lst.copy()
    shuffle = []
    while len(lst) > 0:
        shuffle.insert(random.randint(0,len(shuffle)),lst.pop(0))
    return shuffle

dict = {"num":0,"term":0}
num = 10

dList = []

for i in range(num):
    dict = {"num":i,"term":num -i }
    dList.append(dict)
