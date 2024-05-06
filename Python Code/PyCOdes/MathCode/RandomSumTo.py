import math
import queue
import random

def targetFinder(target,_numSet = []):
    
    def Utility(l, target):
        return target*l
    
    def Hueristic(value, target):
        return abs(target - value)
    
    def SortedInsert(value, lst):
        for i,q in enumerate(lst):
            if(q[1] >= value[1]): return (True,i)
        return (False,len(queue))
    
    numSet = _numSet.copy()
    
    reached = False
    queue = [(0,0)]
    visited = [[queue[0][0]]]
    actions = [[]]

    while len(queue) > 0:
        #breakpoint()
        state = queue.pop(0)
        current_visited = visited.pop(0)
        current_actions = actions.pop(0)
        
        #Checks if the current state is our target
        if state[0] == target:
            reached = True
            return (reached,current_actions)
        
        #Cycle through moves
        for num in numSet:
            # Add the value:
            next_value = state[0] + num
            #breakpoint()
            if next_value not in current_visited:
                next_state = (next_value, Utility(len(current_visited),target) + Hueristic(next_value,target))
                pos = SortedInsert(next_state,queue)
                if pos[0]:
                    queue.insert(pos[1],next_state)
                    visited.insert(pos[1],current_visited + [next_value]) 
                    actions.insert(pos[1],current_actions + [num])
                else:
                    queue.append(next_state)
                    visited.append(current_visited + [next_value])
                    actions.append(current_actions + [num])
            
            #Subtract a value:
            next_value = state[0] - num
            if next_value not in current_visited:
                next_state = (next_value, Utility(len(current_visited),target) + Hueristic(next_value,target))
                pos = SortedInsert(next_state,queue)
                if pos[0]:
                    queue.insert(pos[1],next_state)
                    visited.insert(pos[1],current_visited + [next_value]) 
                    actions.insert(pos[1],current_actions + [-num])
                else:
                    queue.append(next_state)
                    visited.append(current_visited + [next_value])
                    actions.append(current_actions + [-num])
    return (False,[])      
    
lst = [12,10,7,2,5]
target = 35

#print(targetFinder(target,lst))     
for i in range(1): print(i)   
    
    