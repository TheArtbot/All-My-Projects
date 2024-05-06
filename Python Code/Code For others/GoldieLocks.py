#!/bin/python

import math
import os
import random
import re
import sys

def cons(x, y):
    return [x, y]

def car(p):
    return p[0]

def cdr(p):
    return p[1]

nil = []

def makeBinTree(root, left, right):
    return cons(left, cons(root, right))

emptyTree = nil

## ----- Place your code in this section -----


## Complete the binary tree ADT below 
def isEmpty(tree):
    return tree == nil

def root(tree):
    if isEmpty(tree):
        return nil
    return car(cdr(tree)) # implement this.

def left(tree):  
    if isEmpty(tree):
        return nil
    return car(tree) # implement this.

def right(tree):
    if isEmpty(tree):
        return nil
    return cdr(cdr(tree))

def isLeaf(tree):
    return isEmpty(left(tree)) and isEmpty(right(tree)) # implement this.

#
# Complete the 'findNumSpecialPaths' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. BINARY_TREE tree The tree of all links connecting the islands
#  2. INTEGER secret The secret modulus
#  3. INTEGER low The minimum number of treasures on a desirable path
#  4. INTEGER high The maximum number of treasures on a desirable path
#
def findNumSpecialPaths(tree, secret, low, high):
    # Determine the number of paths in tree on which the number of treasures is between low and high

    def ChartPaths(tree, stack, t_count, treasure_paths):
        if isEmpty(tree):
            return treasure_paths
        
        stack.append(root(tree))
        path_sum = sum(stack)
        
        if path_sum % secret == 0: t_count += 1
        
        if isLeaf(tree):
            if t_count <= high and t_count >= low: treasure_paths.append(1)
            else: treasure_paths.append(0)
            #print(treasure_paths)
            return treasure_paths
        
        if not isEmpty(left(tree)):
            treasure_paths = ChartPaths(left(tree),stack,t_count,treasure_paths)
            stack.pop()
        if not isEmpty(right(tree)):
            treasure_paths = ChartPaths(right(tree),stack,t_count,treasure_paths)
            stack.pop()
        return treasure_paths
    
    Medium_Paths = sum(ChartPaths(tree,[],0,[]))
    return Medium_Paths
## ---- End of Section containing your answer -----

def buildTreeAndSearch(connections, s, l, h):
    n = len(connections)
    nodes = [None] * (n+1)
    nodes[0] = emptyTree
    for (i, v, j, k) in connections:
        nodes[i] = makeBinTree(v, nodes[j], nodes[k])
    r = findNumSpecialPaths(nodes[1], s, l, h)
    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = raw_input().rstrip().split()

    n = int(first_multiple_input[0])

    s = int(first_multiple_input[1])

    l = int(first_multiple_input[2])

    h = int(first_multiple_input[3])

    connections = []

    for _ in xrange(n):
        connections.append(map(int, raw_input().rstrip().split()))

    result = buildTreeAndSearch(connections, s, l, h)

    fptr.write(str(result) + '\n')

    fptr.close()
