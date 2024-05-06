from bdb import Breakpoint
import math


def equalString(str1, str2):
    #print("Str1:",str1,"\nStr2:",str2,"\n----------------")
    if not(len(str1) == len(str2)): return False
    for i,s in enumerate(str1): 
        #print("s1: ", s)
        #print("s2: ", str2[i], ":", str2[i].upper(), ":", str2[i].lower())
        if not(s == str2[i] or s == str2[i].upper() or s == str2[i].lower()): return False
    return True

def stringSubtract(str1 = "",str2 = "", allCase = False):
    for s in str2:
        checkS = str1
        str1 = str1.replace(s,'',1)
        if not(allCase):
            continue
        if checkS == str1:
            str1 = str1.replace(s.lower(),'',1)
        if checkS == str1:
            str1 = str1.replace(s.upper(),'',1)
    return str1

def strFind(source, search, Case = False, Order = False):
    if len(search) > len(source):
        return False
    
    foundCount = 0
    start = 0
    
    for i,s in enumerate(search):
        if not(Order): start = 0
        temp = source[start:].find(s)
        if not(temp == -1):
            foundCount += 1
            temp += start
            start = temp + 1
            continue
        
        if not(Case):
            temp = source[start:].find(s.lower())
            if not(temp == -1):
                foundCount += 1
                temp += start
                start = temp + 1
                continue
            temp = source[start:].find(s.upper())
            if not(temp == -1):
                foundCount += 1
                temp += start
                start = temp + 1
                continue
            
    return (foundCount == len(search))

def listSubset(sub, sup, whole = False):
    if len(sub) == 0: return True
    if len(sub) > len(sup): return False
    if not whole:
        for i,s in enumerate(sub):
            if s not in sup: return False
        return True
        
    start = 0
    for i,s in enumerate(sup):
        if start >= len(sup): return False
        if sub[0] not in sup[start:]: return False
        
        start = start + sup[start:].index(sub[0])
        if len(sup) - start - len(sub) < 0: return False
        
        check = False
        for n in sub:
            check = n in sup[start:(start + len(sub))]
            if not check: break
        if check: return True
        
        start += 1
    return False
    

def wasting_water_UI(jugs,capacity):
    print("Welcome to Wasting Water!")
    print(">> To play type play()")
    print(">> To read the rules type rules()")
    print(">> To view and change settings type sett()")
    print(">> To quit type quit()")
    userIn = input("  >> ")
    
    if equalString(userIn,"play()"):
        game(jugs,capacity)
        
        print("something went wrong...")
        return None
    if equalString(userIn,"rules()"):
        
        print("something went wrong...")
        return None
    if equalString(userIn,"sett()"):
        
        print("something went wrong...")
        return None
    if equalString(userIn,"quit()"):
        print("Thanks for playing!")
        exit()
    
    
    return None

def playAgain(capacity):
    print(">> Would you like to play again (Y/n)?")
    userIn = input("  >> ")
    if equalString(userIn,"y"):
        return game(starting,capacity)
    if equalString(userIn,"n"):
        return wasting_water_UI(starting,capacity)
    print(">> Invalid input")
    return playAgain(capacity)

def game(jugs,capacity):
    turn = 0
    turnOrder = ["p","b"]
    
    def goingFirst():
        print(">> If you would like to go first [y/n]")
        print(">> else hit <Enter>")
        userIn = input("  >> ")
        
        if equalString(userIn,"y"):
            return ["p","b"]
            
        elif equalString(userIn,"n"):
            return ["b","p"]
        else:
            print(">> Invalid Responce")
            return goingFirst()

    def playing(turnOrder,turn,jugs,capacity):
        while True:
            if turnOrder[turn%2] == "p":
                while True:
                    print("Current Jug State: \n", jugs)
                    print(">> Type a move:")
                    print(">>> fill(<jug#>) -- fill a jug")
                    print(">>> fill(<jug A#>,<jug B#>) -- pour jug A into jug B until [will not overfill jug B]")
                    print(">>> empty(<jug#>)")
                    userIn = input("   >>> ")
                    
                    if strFind(userIn,"fill()",False,True):
                        jugNums = stringSubtract(userIn,"fill()").split(',')
                        #print(jugNums)
                        
                        if len(jugNums) > 2:
                            print(">> Too many values enter into fillJug. you can only fill one jug or pour one into another")
                            continue
                        if len(jugNums) < 1:
                            print(">> fill() needs at least one integer value. you can ether fill one jug or pour one into another")
                            continue
                        for j in jugNums: 
                            if not(j.isdigit()): print(">> Values entered must be an integer") 
                            break
                        
                        if len(jugNums) == 2:
                            results = pourJug(jugs,capacity,int(jugNums[0]) - 1 ,int(jugNums[1]) - 1,debug)                            
                            jugs = results["jugs"]
                            break
                        results = fillJug(jugs,capacity,int(jugNums[0]) - 1,debug)
                        jugs = results["jugs"]
                        break
                    
                    if strFind(userIn,"empty",False,True):
                        jugNum = stringSubtract(userIn,"empty()")
                        if jugNum == "":
                            print(">> Must enter a jug to empty")
                            continue
                            
                        if not(jugNum.isdigit()):
                            print(">> Values entered must be an integer")
                            continue
                        
                        results = emptyJug(jugs,capacity,int(jugNum) - 1, debug)
                        jugs = results["jugs"]
                        break
                    
                    print(">> Invalid input")
            if turnOrder[turn%2] == "b":
                print("Current Jug State: \n", jugs)
                print(">> robots turn...")
                bot_move = search(jugs,capacity,searchDepth,pTarget,bTarget,debug)
                jugs = bot_move["jugs"]
                
            turn += 1
            #code for checking the winner...
            if jugs == pTarget:
                print(">> Congratulations! You won!")
                break
            if jugs == bTarget:
                print(">> Sorry The bot has won!")
                break    
            
        return None

    print("Before we start...")
    turnOrder = goingFirst()
    print("Alright Lets Begin!")
    playing(turnOrder,turn,jugs,capacity)
    
    playAgain(capacity)
    return None

def fillJug(_jugs,_capacity,index,debug = False):
    jugs = _jugs.copy()
    capacity = _capacity.copy()
    
    if index >= len(jugs) or index >= len(capacity):
        if debug: print(">> [Error From: fillJug()] >> index too high")
        return {"success": False, "jugs":jugs, "indexError": True, "fillError": False }
    if index < 0:
        if debug: print(">> [Error From: fillJug()] >> index too low")
        return {"success": False, "jugs":jugs, "indexError": True, "fillError": False }
    if jugs[index] == capacity[index]:
        if debug: print(">> [Message From: fillJug()] >> jug was already full")
        return {"success": False, "jugs":jugs, "indexError": False, "fillError": True }
    
    jugs[index] = capacity[index]
    if debug: print(">> [Message From: fillJug()] >> jug filled Successfully")
    return {"success": True, "jugs":jugs, "indexError": False, "fillError": False }

def pourJug(_jugs,_capacity,index, index2,debug = False):
    jugs = _jugs.copy()
    capacity = _capacity.copy()
    
    if index >= len(jugs) or index >= len(capacity):
        if debug: print(">> [Error From: pourJug()] >> index too high")
        return {"success": False, "jugs":jugs, "indexError": True, "fillError": False , "emptyError": False}
    if index < 0:
        if debug: print(">> [Error From: pourJug()] >> index too low")
        return {"success": False, "jugs":jugs, "indexError": True, "fillError": False , "emptyError": False}
    
    if index2 >= len(jugs) or index2 >= len(capacity):
        if debug: print(">> [Error From: pourJug()] >> index2 too high")
        return {"success": False, "jugs":jugs, "indexError": True, "fillError": False , "emptyError": False}
    if index2 < 0:
        if debug: print(">> [Error From: pourJug()] >> index2 too low")
        return {"success": False, "jugs":jugs, "indexError": True, "fillError": False , "emptyError": False}

    if jugs[index2] >= capacity[index2]:
        if debug: print(">> [Message From: pourJug()] >> JugB was already full")
        return {"success": False, "jugs":jugs, "indexError": False, "fillError": True , "emptyError": False}
    
    if jugs[index] <= 0:
        if debug: print(">> [Message From pourJug()] >> JugA was empty")
        return {"success": False, "jugs":jugs, "indexError":False, "fillError": False , "emptyError": True}
    
    temp = jugs[index2]
    jugs[index2] = min(capacity[index2],(jugs[index2] + jugs[index]))
    jugs[index] = jugs[index] - (jugs[index2] - temp)
    if debug: print(">> [Message From: pourJug()] >> jugs filled Successfully")
    return {"success": True, "jugs":jugs, "indexError": False, "fillError": False , "emptyError": False}
    
def emptyJug(_jugs,_capacity,index,debug = False):
    jugs = _jugs.copy()
    capacity = _capacity.copy()
    
    if index >= len(jugs) or index >= len(capacity):
        if debug: print(">> [Error From: fillJug()] >> index too high")
        return {"success": False, "jugs":jugs, "indexError": True, "emptyError": False}
    if index < 0:
        if debug: print(">> [Error From: fillJug()] >> index too low")
        return {"success": False, "jugs":jugs, "indexError": True, "emptyError": False}
    if jugs[index] <= 0:
        if debug: print(">> [Message From: fillJug()] >> jug was already empty")
        return {"success": False, "jugs":jugs, "indexError": False, "emptyError": True}
    
    jugs[index] = 0
    if debug: print(">> [Message From: fillJug()] >> jug filled Successfully")
    return {"success": True, "jugs":jugs, "indexError": False, "emptyError": False}

def search(jugs,capacity, depth, ptarget, btarget, debug = False):
    # there is a possiblity that we need a max_start variable to tell if we started on a max or a min.
    
    # a function for pruning the leaf nodes that are no longer needed.
    def prune(queue,paths,common):
        rl = []
        for p in paths:
            if listSubset(common,p):
               rl.append(p)
               queue.remove(p[-1]) 
        
        for p in rl:
            paths.remove(p)
        
        return queue
    
    branches = []
    queue = [{"jugs":jugs,"alpha": -float("inf"), "beta": float("inf")}]
    paths = [[queue[0]]]
    while len(queue) > 0:
        state = queue.pop(0)
        current_path = paths.pop(0)
        
        if debug:print("state: ", state,"\ncurrent_path: ", current_path)
        
        # Alpha/Beta pruning process.
        if len(current_path) >= depth or state["jugs"] == ptarget or state["jugs"] == btarget:
            #breakpoint()
            for i in range(len(current_path) - 1):
                n = -(i + 2)
                if (len(current_path) - n)%2 == 1:
                    if current_path[n]["alpha"] > current_path[n+1]["beta"]:
                        # figure out the logistics of pruning the tree and if i want to <continue> afterwards.
                        t = len(current_path) - i
                        queue = prune(queue,paths,current_path[:t])
                        continue
                    current_path[n]["alpha"] = max(current_path[n]["alpha"],current_path[n+1]["beta"])
                else:
                    if current_path[n]["beta"] < current_path[n+1]["alpha"]:
                        # figure out the logistics of pruning the tree and if i want to <continue> afterwards.
                        t = len(current_path) - i
                        queue = prune(queue,paths,current_path[:t])
                        continue
                    current_path[n]["beta"] = min(current_path[n]["beta"],current_path[n+1]["alpha"])
            
            branches.append(current_path)
            continue
        
        #itterates through each jug filling and empting combination.
        for i,j1 in enumerate(state["jugs"]):
            # filling jugs...
            if j1 < capacity[i]:
                next_jugs = fillJug(state["jugs"],capacity,i)["jugs"].copy()
                # alpah and beta values are natrually inherited from the nodes above.
                next_alpha = current_path[-1]["alpha"]
                next_beta = current_path[-1]["beta"]
                if len(current_path) == depth-1 or next_jugs == ptarget or next_jugs == btarget:
                    # accounting for the alpha/beta values at the leaf nodes...
                    value = Hueristic(next_jugs,btarget) - Hueristic(next_jugs,ptarget)
                    if (len(current_path)%2 == 1):
                        next_alpha = value
                    else:
                        next_beta = value
                
                next_state = {"jugs": next_jugs,"alpha" : next_alpha,"beta": next_beta}
                if debug:  print("[filling] next_state:",next_state)
                if next_state not in current_path: # if next state has yet to be explored in this branch.
                    queue.insert(0,next_state)
                    paths.insert(0,current_path + [next_state])
            #breakpoint()
            # pouring one to another...
            for t, j2 in enumerate(jugs):
                if i == t: continue
                if j1 > 0 and j2 < capacity[t]:
                    next_jugs = pourJug(state["jugs"],capacity,i,t)["jugs"].copy()
                    # alpah and beta values are natrually inherited from the nodes above.
                    next_alpha = current_path[-1]["alpha"]
                    next_beta = current_path[-1]["beta"]
                    if len(current_path) == depth-1 or next_jugs == ptarget or next_jugs == btarget:
                        # accounting for the alpha/beta values at the leaf nodes...
                        if (len(current_path)%2 == 1):
                            next_alpha = max(Hueristic(next_jugs,btarget) - Hueristic(next_jugs,ptarget),current_path[-1]["alpha"])
                        else:
                            next_beta = min(Hueristic(next_jugs,btarget) - Hueristic(next_jugs,ptarget),current_path[-1]["beta"])
                    
                    next_state = {"jugs": next_jugs,"alpha" : next_alpha,"beta": next_beta}
                    if debug: print("[pouring] next_state:",next_state)
                    if next_state not in current_path: # if next state has yet to be explored in this branch.
                        queue.insert(0,next_state)
                        paths.insert(0,current_path + [next_state])    
            
            #empting jugs...
            if j1 > 0:
                next_jugs = emptyJug(state["jugs"],capacity,i)["jugs"].copy()
                # alpah and beta values are natrually inherited from the nodes above.
                next_alpha = current_path[-1]["alpha"]
                next_beta = current_path[-1]["beta"]
                if len(current_path) == depth-1 or next_jugs == ptarget or next_jugs == btarget:
                    # accounting for the alpha/beta values at the leaf nodes...
                    if (len(current_path)%2 == 1):
                        next_alpha = max(Hueristic(next_jugs,btarget) - Hueristic(next_jugs,ptarget),current_path[-1]["alpha"])
                    else:
                        next_beta = min(Hueristic(next_jugs,btarget) - Hueristic(next_jugs,ptarget),current_path[-1]["beta"])
                    
                next_state = {"jugs": next_jugs,"alpha" : next_alpha,"beta": next_beta}
                if debug: print("[empting] next_state:",next_state)
                if next_state not in current_path: # if next state has yet to be explored in this branch.
                    queue.insert(0,next_state)
                    paths.insert(0,current_path + [next_state])

    # picking the best choice for the bot.
    #breakpoint()
    choice = branches[0][1]
    for p in branches:
        if p[1]["alpha"] > choice["alpha"]:
            choice = p[1]
        
        
    return choice

def Hueristic(current, target):
    total = 0
    for i,s in enumerate(current):
        total += pow(s - target[i],2)
    return math.sqrt(total)
    

# settings variables

pTarget = [1,1,1,5]
bTarget = [5,1,1,1]

capacity = [5,2,3,5]
searchDepth = 5
debug = False

starting = [0,0,0,0]

# TODO LIST:
# Add settings menu
# Add a rule that you can't undo you oppenents last move.
# Add the display of what move the bot made.
# Add the display of the max capacities of the jugs
# refine documentation.

wasting_water_UI(starting,capacity)


