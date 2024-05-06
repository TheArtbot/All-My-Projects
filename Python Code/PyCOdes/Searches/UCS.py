def water_jugs(goal_state): 
    # Original BFS by: Gunjan Mansingh
    # New UCS by: Daniel Wright
    
    # Changes made:
    # All changes unrelated to the actual searching process were carried over from DFS.py
    # The Tracking print statements where changed to also display the Cost value as well.
    #
    # For the UCS, the next_state will be evaluated by the water usage. The cost of the Node is the Additional
    # water used in the process. An an InsertSort function was used to find the position of the 
    # new state or if the queue need to appended.
    #
    # This is simply acheved by finding the total water in the next_state and if it is larger that the current
    # state the the difference is the individual cost.
    # NOTE: This individual cost accumulated with the rest of the cost in the branch to get the cost of
    #       the node.
    #
    # For the UCS, the way to update the path was to use the InsertSort func to find where the current path
    # need to be inserted or appended.
    # NOTE: The current path was appended to the same index in path as the next_state in the queue. 
    
    
    reached = False #keeps check is the target has been reached.
    
    capacity1 = 3
    capacity2 = 1 
    visited = []
    queue = [((0, 0),0)]  # The initial state is (0, 0) 
    paths = [[queue[0]]]
    while len(queue) > 0: 
        C_node = queue.pop(0)
        state = C_node[0] 
        visited.append(state)
        current_path = paths.pop(0)
        # Check if the current state is the goal state 
        if state == goal_state:
            reached = True  #target has been reached
            print("Target Found: ", C_node)
            print("Path :",current_path) 
            print("Nodes expanded: ", visited) 
            return None
        # Generate the next states.
        if state[0] < capacity1: #Fill Jug A 
            next_state = (capacity1, state[1]) 
            if next_state not in visited:
                N_node = (next_state,Utility(next_state,state))
                # decides where the value should go and if the queue will need to be appended, return (bool,int)
                ans = InsertSort(queue,N_node)
                if ans[0]: 
                    queue.insert(ans[1],N_node)
                    paths.insert(ans[1],current_path + [N_node]) 
                else:
                    queue.append(N_node)
                    paths.append(current_path + [N_node]) 
        if state[1] < capacity2: #Fill Jug B
            next_state = (state[0], capacity2) 
            if next_state not in visited:
                N_node = (next_state,Utility(next_state,state))
                # decides where the value should go and if the queue will need to be appended, return (bool,int)
                ans = InsertSort(queue,N_node)
                if ans[0]: 
                    queue.insert(ans[1],N_node)
                    paths.insert(ans[1],current_path + [N_node]) 
                else:
                    queue.append(N_node)
                    paths.append(current_path + [N_node])  
        if state[0] > 0 and state[1]<capacity2: # pour from Jug A into B 
            amount = min(state[0], capacity2 - state[1])
            next_state = (state[0] - amount, state[1] + amount) 
            if next_state not in visited:
                N_node = (next_state,Utility(next_state,state))
                # decides where the value should go and if the queue will need to be appended, return (bool,int)
                ans = InsertSort(queue,N_node)
                if ans[0]: 
                    queue.insert(ans[1],N_node)
                    paths.insert(ans[1],current_path + [N_node]) 
                else:
                    queue.append(N_node)
                    paths.append(current_path + [N_node])  
        if state[1] > 0  and state[0]<capacity1:# pour from Jug B into A 
            amount = min(state[1], capacity1 - state[0])
            next_state = (state[0] + amount, state[1] - amount) 
            if next_state not in visited:
                N_node = (next_state,Utility(next_state,state))
                # decides where the value should go and if the queue will need to be appended, return (bool,int)
                ans = InsertSort(queue,N_node)
                if ans[0]: 
                    queue.insert(ans[1],N_node)
                    paths.insert(ans[1],current_path + [N_node]) 
                else:
                    queue.append(N_node)
                    paths.append(current_path + [N_node])   
        if state[0] > 0: #Empty Jug A
            next_state  = (0,state[1]) 
            if next_state not in visited:
                N_node = (next_state,Utility(next_state,state))
                # decides where the value should go and if the queue will need to be appended, return (bool,int)
                ans = InsertSort(queue,N_node)
                if ans[0]: 
                    queue.insert(ans[1],N_node)
                    paths.insert(ans[1],current_path + [N_node]) 
                else:
                    queue.append(N_node)
                    paths.append(current_path + [N_node])   
        if state[1] > 0: #Empty Jug B
            next_state = (state[0],0) 
            if next_state not in visited:
                N_node = (next_state,Utility(next_state,state))
                # decides where the value should go and if the queue will need to be appended, return (bool,int)
                ans = InsertSort(queue,N_node)
                if ans[0]: 
                    queue.insert(ans[1],N_node)
                    paths.insert(ans[1],current_path + [N_node]) 
                else:
                    queue.append(N_node)
                    paths.append(current_path + [N_node])  
        
        print( C_node , " : [" , queue , "]") # The Tranking Print statement
        
    if(not(reached)): #if while loop ends and the target hasn't been reached.
        print("Path couldn't be found.")
        print("Nodes expanded: ", visited)
    return None

def Utility(nState, pState):
    new = (nState[0] + nState[1])
    old = (pState[0] + pState[1])
    if new > old: return new
    return old
    
def InsertSort(queue,value):
    for i,q in enumerate(queue):
        if(q[1] >= value[1]): return (True,i)
    return (False,len(queue))

print("A classic water jug fill puzzel, Jug A can hold 3 and Jug B can hold 1.")
targetA = int(input("Enter your target value for Jug A: "))
targetB = int(input("Enter your target value for Jug B: "))
print("Target: ", (targetA,targetB))
water_jugs((targetA,targetB))