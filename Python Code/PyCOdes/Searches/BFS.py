def water_jugs(goal_state): 
    # Changes made:
    # The actual search procces was not changed only some print statements
    # 
    # A reached boolean variable was added to find if the search was able to reach the target value and
    # return a message if i could not do so.
    # 
    # The print statement that tracked the queue was changed to display the current state as well.
    # 
    # Finialy, the program now will prompt the user for the target value.
    
    
    reached = False
    
    capacity1 = 3
    capacity2 = 1 
    visited = []
    queue = [(0, 0)]  # The initial state is (0, 0) 
    paths = [[queue[0]]]
    while len(queue) > 0: 
        state = queue.pop(0) 
        visited.append(state)
        current_path = paths.pop(0)
        # Check if the current state is the goal state 
        if state == goal_state:
            reached = True
            print("Target Found: ", state)
            print("Path :",current_path) 
            print("Nodes expanded: ", visited) 
            return None
        # Generate the next states.
        if state[0] < capacity1: #Fill Jug A 
            next_state = (capacity1, state[1]) 
            if next_state not in visited:
                queue.append(next_state)
                paths.append(current_path + [next_state]) 
        if state[1] < capacity2: #Fill Jug B
            next_state = (state[0], capacity2) 
            if next_state not in visited:
                queue.append(next_state)
                paths.append(current_path + [next_state])
        if state[0] > 0 and state[1]<capacity2: # pour from Jug A into B 
            amount = min(state[0], capacity2 - state[1])
            next_state = (state[0] - amount, state[1] + amount) 
            if next_state not in visited:
                queue.append(next_state)
                paths.append(current_path + [next_state])
        if state[1] > 0  and state[0]<capacity1:# pour from Jug B into A 
            amount = min(state[1], capacity1 - state[0])
            next_state = (state[0] + amount, state[1] - amount) 
            if next_state not in visited:
                queue.append(next_state)
                paths.append(current_path + [next_state]) 
        if state[0] > 0: #Empty Jug A
            next_state  = (0,state[1]) 
            if next_state not in visited:
                queue.append(next_state)
                paths.append(current_path + [next_state]) 
        if state[1] > 0: #Empty Jug B
            next_state = (state[0],0) 
            if next_state not in visited:
                queue.append(next_state)
                paths.append(current_path + [next_state])
        
        print( state , " : [" , queue , "]") # The new print statement to track the queue and the last state 
                                             # checked
    
    if(not(reached)):
        print("Path couldn't be found.")
        print("Nodes expanded: ", visited)
    return None


print("A classic water jug fill puzzel, Jug A can hold 3 and Jug B can hold 1.")
targetA = int(input("Enter your target value for Jug A: "))
targetB = int(input("Enter your target value for Jug B: "))
print("Target: ", (targetA,targetB))
water_jugs((targetA,targetB))

