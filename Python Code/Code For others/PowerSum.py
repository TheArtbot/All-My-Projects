import math

def powerSum(X, N):
    # Write your code here

    def MoreOrLessEqual(x,y):
        # when finding the n'th root of a number you may have small inacuracies in the root func
        # this accounts for that.
        error_account = 0.0000000000001
        return (abs(x-y) < error_account*(x) and abs(x-y) < error_account*(y))
    
    def powerSumHelper(total,n,guess,upper):
        sum_count = 0
        
        while guess <= upper:
            guess_p = guess**n
            sub = total - guess_p
            
            if sub < 0: return 0
            root = sub**(1/n)
            
            # if the sub is a perfect power of n 
            # then (guess_p + sub) is a way to represent total
            
            # So... is sub a perfect power?
            if sub > guess_p and (MoreOrLessEqual(root,math.ceil(root)) or MoreOrLessEqual(root,math.floor(root))): 
                sum_count += 1
            
            # However you have numbers that are made up of perfect powers.
            # Those numbers can be the perfect powers or not...
            
            # So if there is way to represent sub in perfect powers,
            # (regradless of if it itself is a perfect power)
            # then that is another way to represent the whole.
            sum_count += powerSumHelper(sub,n,guess+1,(sub**(1/N)))
            guess += 1
        return sum_count

    upper_lim = ((X**(1/N)))
    powerSumCount = powerSumHelper(X,N,1,upper_lim)
    if MoreOrLessEqual(upper_lim,math.floor(upper_lim)) or MoreOrLessEqual(upper_lim,math.ceil(upper_lim)): 
        return powerSumCount + 1
    return powerSumCount

print(powerSum(64,3))
