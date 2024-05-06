def waterjugs(jugs_sizes, goal_state, hueristics = False, debug = False):
    
    if not(len(jugs_sizes) == len(goal_state)):
        print("goal state does not have the same amount of entries as jugs\n Its as if you expect to fill a jug that is not mentioed or remove a jug without cause")
        return None
    
    visited = []
    queue = [([],0)]
    for i in range(len(jugs_sizes)): queue[0][0].append(0) #initailize the first set to be the zero set.
    paths = [[queue[0]]]
    while len(queue) > 0:
        C_node = queue.pop(0)
        state = C_node[0] 
        visited.append(state)
        current_path = paths.pop(0)
        # Check if the current state is the goal state 
        if state == goal_state:
            reached = True  #target has been reached
            cost = C_node[1]
            print("Target Found: ", C_node)
            print("path cost: ", cost)
            if debug:
                print("Path :",current_path) 
                print("Nodes expanded: ", visited)
            else:
                print("length of path: ", len(current_path))
                print("number of nodes expaned: ",len(visited)) 
            return None
        # This will iterate through every jug, filling it, poring it into anouther jug and empting it.
        for i,j1 in enumerate(state): 
            # Filling jugs
            if j1 < jugs_sizes[i]:
                next_state = state.copy()
                next_state[i] = jugs_sizes[i]
                if next_state not in current_path:
                    N_node = (next_state,(PathCost(next_state,state)))
                    if hueristics: N_node = (N_node[0],N_node[1] + HueristicCost(next_state,goal_state))
                    insert = InsertSort(queue,N_node)
                    if insert[0]: 
                        queue.insert(insert[1],N_node)
                        paths.insert(insert[1],current_path + [N_node]) 
                    else:
                        queue.append(N_node)
                        paths.append(current_path + [N_node]) 
            
            # Pouring it into another
            for t,j2 in enumerate(state):
                if i == t:
                    continue
                if j1 > 0 and j2 < jugs_sizes[t]:
                    next_state = state.copy()
                    amount = min( j1, jugs_sizes[t] - j2)
                    next_state[i] = j1 - amount
                    next_state[t] = j2 + amount
                    if next_state not in current_path:
                        N_node = (next_state,(PathCost(next_state,state)))
                        if hueristics: N_node = (N_node[0],N_node[1] + HueristicCost(next_state,goal_state))
                        insert = InsertSort(queue,N_node)
                        if insert[0]: 
                            queue.insert(insert[1],N_node)
                            paths.insert(insert[1],current_path + [N_node]) 
                        else:
                            queue.append(N_node)
                            paths.append(current_path + [N_node]) 
            
            # Empting jugs:
            if j1 > 0:
                next_state = state.copy()
                next_state[i] = 0
                if next_state not in current_path:
                    N_node = (next_state,(PathCost(next_state,state)))
                    if hueristics: N_node = (N_node[0],N_node[1] + HueristicCost(next_state,goal_state))
                    insert = InsertSort(queue,N_node)
                    if insert[0]: 
                        queue.insert(insert[1],N_node)
                        paths.insert(insert[1],current_path + [N_node]) 
                    else:
                        queue.append(N_node)
                        paths.append(current_path + [N_node]) 
        
        if debug:
            print( C_node , ":", queue ) # The Tranking Print statement
        
    if(not(reached)): #if while loop ends and the target hasn't been reached.
        print("Path couldn't be found.")
        print("Nodes expanded: ", visited)
    return None            
                    
                    
def PathCost(nState, cState):
    nCost = sum(nState)
    cCost = sum(cState)
    if nCost > cCost: return nCost
    else: return cCost

def HueristicCost(nState, gState):
    gCost = sum(gState)
    nCost = sum(nState)
    return abs(gCost - nCost)    

def InsertSort(queue,value):
    for i,q in enumerate(queue):
        if(q[1] >= value[1]): return (True,i)
    return (False,len(queue))



waterjugs([3,2,1],[1,1,1])