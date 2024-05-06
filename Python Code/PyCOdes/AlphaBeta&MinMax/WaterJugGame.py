# Original Made BFS by: Profesor Gunjan Mansingh
# New DFS design by: Daniel Wright

def water_jugs(target, depth = float("inf"), capacity = [3,1], debug = False): 
    reached = False
    leaves = []
    capCheck = False
    
    if not(len(target) == len(capacity)):
        print("goal state does not have the same amount of entries as jugs\n Its as if you expect to fill a jug that is not mentioed or remove a jug without cause")
        return {"found": reached, "leaves": leaves, "capacity": capCheck}
    
    capCheck = True
    
    visited = []
    branches = []
    queue = [[]]
    for i in range(len(capacity)): queue[0].append(0)
    paths = [[queue[0]]]
    
    while len(queue) > 0:
        state = queue.pop(0)
        visited.append(state)
        current_path = paths.pop(0)
        
        #Check if the target has been reached
        if state == target:
            reached = True
            if debug:
                print("Target Found: ", state)
                print("Path :",current_path) 
                print("Pathways explored: ")
                for i,q in enumerate(branches):
                    print("Branch" , i + 1, ":", q)
                    leaves.append(q[-1])
            return {"found": reached, "leaves": leaves, "capacity": capCheck}
        
        #Check if depth has been exceeded
        if len(current_path) >= depth:
            continue
        
        # This will iterate through every jug, filling it, poring it into anouther jug and empting it.
        for i,j1 in enumerate(state):
            # Filling jugs:
            if j1 < capacity[i]:
                next_state = state.copy()
                next_state[i] = capacity[i]
                if next_state not in current_path:
                    queue.insert(0,next_state)
                    paths.insert(0,current_path + [next_state])
                    
                    if current_path in branches: 
                        branches[branches.index(current_path)] = current_path + [next_state]
                    else:
                        branches.append(current_path + [next_state])
            
            # Pouring it into another:
            for t,j2 in enumerate(state):
                if i == t:
                    continue
                if j1 > 0 and j2 < capacity[t]:
                    next_state = state.copy()
                    amount = min( j1, capacity[t] - j2)
                    next_state[i] = j1 - amount
                    next_state[t] = j2 + amount
                    if next_state not in current_path:
                        queue.insert(0,next_state)
                        paths.insert(0,current_path + [next_state])
                        
                        if current_path in branches: 
                            branches[branches.index(current_path)] = current_path + [next_state]
                        else:
                            branches.append(current_path + [next_state])
                
            # Empting Jugs:
            if j1 > 0:
                next_state = state.copy()
                next_state[i] = 0
                if next_state not in current_path:
                    queue.insert(0,next_state)
                    paths.insert(0,current_path + [next_state])
                    if current_path in branches: 
                        branches[branches.index(current_path)] = current_path + [next_state]
                    else:
                        branches.append(current_path + [next_state])
    
    if(not(reached)): #if while loop ends and the target hasn't been reached.
        for i,q in enumerate(branches):
            leaves.append(q[-1])
            
        if not(debug):
           return {"found": reached, "leaves": leaves, "capacity": capCheck}
        
        if not(depth == float("inf")):
            print("Path couldn't be found with the depth of ", depth)
            print("Pathways explored: ")
            for i,q in enumerate(branches):
                print("Branch" , i + 1, ":", q)
            return {"found": reached, "leaves": leaves, "capacity": capCheck}
        
        print("Path couldn't be found.")
        print("Nodes expanded: ", visited)
    return {"found": reached, "leaves": leaves, "capacity": capCheck}

    