import math


# so what is the diffenrence between repeat() and repeatSquares()?
# we can use that difference to generalise the repitions
def repeat(count, val):
    if count <= 0:
        return val
    if count%2 == 0:
        return repeat(count//2,val) + repeat(count//2,val)
    else:
        return repeat((count - 1)//2,val) + val

def repeatSquares(a,b): 
    # "a" and "b" are the same as "count" and "val" from before, the name doesn't matter 
    # just as long as they do the same thing
    if a <= 0:
        return b
    if a%2 == 0:
        return repeatSquares(a//2,b) * repeatSquares(a//2,b)
    else:
        return repeatSquares((a-1)//2,b) * b
    
  
def repeatSquares2(a,b):
    # we can use the fact that the "operation" ("+" in repeat and "*" in repeatSquares) is the 
    # only change to or advantage. 
    
    # we can generalise them into two fucntions: a repeator and an opperator
    
    # if you want to change the order of a and be in the code you just which them, whenever you see them
    # so whenever you see an "a" replace it with a "b" and vise versa
    def repeator(n,m):
        if n <= 0:
            return m
        if n%2 == 0:
            return opperator(repeator(n//2,m),repeator(n//2,m))
        else:
            return opperator(repeator((n-1)//2,m),m)
        
    def opperator(n,m):
        return n * m 
    
    return repeator(b,a)       
    
# this function should return a*b in a very short time
print(repeat(10,4))

# alright now it working!
# this will print 4^10, i.e: the fucntione return b^a
# you get it?
print(repeatSquares(10,4))

# now let's test it
print(repeatSquares2(10,4))
# since repeatedSquares and repeatedSquares2 gave the same answer we can assume they work the same
# side note they currently take (a,b) and return b^a, from now on i will code it so that it returns a^b 
# instead, It seems more intuitive to me 


# so this means we can do this with more complex functions, like Matirx Multiplication...

# in your hackerrank sir needs you to track the final values of co-ordinate (x,y) after some amount of 
# moves

# but they don't move normally...
# x(i+1) = a*x(i) - y(i) the next x value is the a * the current x value minus the current y
# y(i+1) = x(i) + b*y(i) the next y value is the current x plus b* the current y value.
# you get that? 


def repeatDoublesMatrix(matrix,n, mod):
    # to make life easier, lets write 2x2 matrices as [r1c1,r1c2,r2c1,r2c2]
    # i might need a diagram for that one....

    def repeator(matrix,n, mod):
        # we don't really need to change how this part works
        if n <= 0:
            return matrix
        if n%2 == 0:
            return opperator(repeator(n//2,matrix, mod),repeator(n//2,matrix, mod), mod)
        else:
            return opperator(repeator((n-1)//2,matrix, mod),matrix, mod)
        
    def opperator(m1,m2,mod):
        # just need to fix this up for matrix multiplications
        # also Prof. Core wants you to mod the values so i'll try to work that in...
        
        # so i'm just gonna give this one wihtout explanation, cause it a bunch of math that doesn't really 
        # matter to the lession. 
        # this is 2x2 matrix multiplication:
        
        # remember: matrix in the form = [r1c1,r1c2,r2c1,r2c2]
        
        new_r1c1 = (m1[0] * m2[0] + m1[1] * m2[2])%mod
        new_r1c2 = (m1[0] * m2[1] + m1[1] * m2[3])%mod
        new_r2c1 = (m1[2] * m2[0] + m1[3] * m2[2])%mod
        new_r2c2 = (m1[2] * m2[1] + m1[3] * m2[3])%mod
        # that should be right...
        
        return [new_r1c1,new_r1c2,new_r2c1,new_r2c2]
    
    return repeator(matrix,n, mod) 

# And that should be it...
# the last Repeated Doubling should work
# Ironic, i said i would only show you how it works but here i am did every thing but debug the code...

# the last thing you need is the final multiplication to get the x(i+n) y(i+n) [where n is the number of steps]
def xy_shifter(matrix, current_x, current_y):
    return [(matrix[0]*current_x + matrix[1]*current_y),(matrix[2]*current_x + matrix[3]*current_y)]
    
