import math
import os
import queue
import random
from time import sleep
from tracemalloc import start


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
    """returns True if the list 'sub' is a subset of 'sup'. If 'whole' is set to true then 'sub' must appear contingently"""
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
   
def clear():
    '''fucntion from: https://www.geeksforgeeks.org/clear-screen-python/'''
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear') 
 
def clearPrevLine(count = 1):
    '''function from: https://itnext.io/overwrite-previously-printed-lines-4218a9563527'''
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    SCROLL_UP = '\033[1S'
    for i in range(count + 1):
        print(LINE_UP, end=LINE_CLEAR)
        #print(SCROLL_UP, end = LINE_UP)

def wasting_water_UI(sett_vars):
    clear()
    print("\033[1;4mWelcome to Wasting Water!\033[0m")
    print(">> To play type play()")
    print(">> To read the rules type rules()")
    print(">> To view and change settings type sett()")
    print(">> To quit type quit()")
    while True:
        userIn = input("  >> ")
        
        if equalString(userIn,"play()") or equalString(userIn,"play") or equalString(userIn,"play("):
            game(sett_vars)
            print("something went wrong...")
            return None
        if equalString(userIn,"rules()") or equalString(userIn,"rules") or equalString(userIn,"rules("):
            rules(sett_vars)
            print("something went wrong...")
            return None
        if equalString(userIn,"sett()") or equalString(userIn,"sett") or equalString(userIn,"sett("):
            setting(sett_vars)
            print("something went wrong...")
            return None
        if equalString(userIn,"quit()") or equalString(userIn,"quit") or equalString(userIn,"quit("):
            print("Thanks for playing!")
            exit()
            
        print(">> Sorry I don't not recognise: ", userIn)
  
def rules(sett_vars):
    clear()
    print("\033[4mRULES:\033[0m")
    print(">> The rules are simple.")
    print(">> You start with a variety of jugs \033[4m(usually empty)\033[0m")
    print(">> On your turn you can interact with a jug or jugs")
    print(">> Interactions allowed: ")
    print("  >> Fill a jug with water")
    print("  >> Pour water from one jug to the next till ether")
    print("     the pouring jugs is empty or the filling jug is full")
    print("  >> Empty a jug.")  
    print(">> Your goal is to get a specific water level in each jug.")
    print(">> But... You'll be playing against a bot and its goal is get a different arrangement...\033[4m(usually)\033[0m")
    print(">> So is the man better than the machine, or is the hard cold metal prevaile?")
    print(">> Whatever the outcome, One things certain...")
    print(">> You'll be \033[1mWasting Water\033[0m")
    print("Press enter to return the main screen")
    input()
    
    wasting_water_UI(sett_vars)

def setting(sett_vars):
    clear()
    print("\033[4mSETTINGS:\033[0m")
    while True:
        breakpoint()
        print(">> Difficulty: ", sett_vars["diffLv"])
        print(">> Here are the settings for your current difficulty level : ")
        print("  >> Your Goal: ", sett_vars["pTarget"])
        print("  >> Bot's Goal: ", sett_vars["bTarget"])
        print("  >> Jug capacity: ", sett_vars["capacity"])
        print("  >> Starting arrangement: ", sett_vars["start"])
        print("  >> search depth: ", sett_vars["searchDepth"])
        if (sett_vars["diffLv"] >= 5): print("\033[2m",end ='')
        print(">> to increase difficulty type LvUp()\033[0m")
        if sett_vars["diffLv"] <= 1:print("\033[2m",end ='')
        print(">> to decrease difficulty type LvDown()\033[0m")
        print(">> For custumised Setting, type custom()")
        print(">> To return to the Main Menu, type main()")
        while True:
            userIn = input("  >> ")
            
            if equalString(userIn,"LvUp()") or equalString(userIn,"LvUp(") or equalString(userIn,"LvUp"):
                if sett_vars["diffLv"] >= 5: print(">> Max level reached");continue
                stats = LevelAdjust(sett_vars["diffLv"],1)
                sett_vars["diffLv"] = sett_vars["diffLv"] + 1
                sett_vars["pTarget"] = stats["pTarget"]
                sett_vars["bTarget"] = stats["bTarget"]
                sett_vars["capacity"] = stats["capacity"]
                sett_vars["start"] = stats["start"]
                sett_vars["searchDepth"] = stats["searchDepth"]
                setting(sett_vars)
            elif equalString(userIn,"LvDown()") or equalString(userIn,"LvDown(") or equalString(userIn,"LvDown"):
                if sett_vars["diffLv"] <= 1: print(">> Min level reached");continue
                stats = LevelAdjust(sett_vars["diffLv"],1)
                sett_vars["diffLv"] = sett_vars["diffLv"] - 1
                sett_vars["pTarget"] = stats["pTarget"]
                sett_vars["bTarget"] = stats["bTarget"]
                sett_vars["capacity"] = stats["capacity"]
                sett_vars["start"] = stats["start"]
                sett_vars["searchDepth"] = stats["searchDepth"]
                setting(sett_vars)
            elif equalString(userIn,"custom()") or equalString(userIn,"custom(") or equalString(userIn,"custom"):
                settCustomise()
            elif equalString(userIn,"main()") or equalString(userIn,"main(") or equalString(userIn,"main"):
                wasting_water_UI(sett_vars)
            else:
                print(">> Sorry couldn't recoginse: ", userIn)

def LevelAdjust(Lv,increment = 0):
    # first we need to increment the difficulty level.
    Lv = Lv + increment
    return realizeDifficulty(Lv) # then we change the setting varriable relive to the difficulty.
    
def realizeDifficulty(level):
    # Deciding the search depth
    s_depth = 4 + 3 * level
    
    # Deciding the number of jugs
    jugAmount = 2 + math.ceil(level/2)
    
    # then to decide how much distance there can be between the start and the goal.
    # both player and the bot have to have the same distance between start and goal.
    dis_from_start = 7 * math.ceil(level/2)
    
    # then how far from the max filled jugs, this is to ensure the winnablity of an arrangment.
    # same as before, they must be the same distance etc...
    dis_from_full = math.ceil(level/2) 
    
    # this represent the minimum amount of state the search needs to pass before i can start the selection process
    min_path_len = math.ceil(level/2) + 7
    
    # we need to set the starting jugs and jug capacities.
    # to optimise the variance of player and bot goals
    # there need to be as much overlap between the states that fir the start_dis and the states that fit the
    # full_dis. 

    # So working out the facts:
    #   the minimum case for full_jugs "position" is a "point" start_rad + full_rad away from start.
    #   the maximum case is a "point" where: full_rad = start_rad + dis_between.
    # so i need to find the distance between the two points and then place full_jug along that line.
    # thus rewrite the eqn in terms of dis_between.
    #   max: dis_between = start_rad + full_rad.
    #   min: dis_between = full_rad - star_rad.
    
    start_jugs = [0 for n in range(jugAmount)]
    start_full_dis = (random.randint(abs(dis_from_full - dis_from_start),(dis_from_start + dis_from_full)))**2 

    # I wil make a free vector with the required magnitude and add it to full_jug.
    free_vec = [1 for n in range(jugAmount)]
    for index, comp in enumerate(free_vec):
        if index == len(free_vec) - 1: free_vec[index] = start_full_dis; continue
        free_vec[index] = random.randrange(1,start_full_dis - sum(free_vec[index+1:]))
        start_full_dis -= free_vec[index]
        #breakpoint()
    
    full_jugs = [round(math.sqrt(x)) for x in free_vec]
    for index, jug in enumerate(full_jugs):
        #breakpoint()
        full_jugs[index] = jug + start_jugs[index]
       
    # shuffle the capacity to make things more interesting.
    random.shuffle(full_jugs)
    
    # now that we have the capacity, we can start the depth first search to find suitable values the make the
    # ptarget and btarget.
    good_nodes = [] # good_nodes are states that can possibly be the goal states.
    queue = [start_jugs]
    paths = [queue]
    tolerance = 10
    while len(queue) > 0:
        # to increase diversity of good_nodes, the queue and path will be shuffled at random.
        if len(queue) >= min_path_len and random.random() <= 0.1:
            shuffle_queue = []
            shuffle_paths = []
            while len(queue) > 0:
                i = int(random.randint(1,len(queue)) - 1)
                shuffle_queue.append(queue.pop(i))
                shuffle_paths.append(paths.pop(i))
            queue = shuffle_queue.copy()
            paths = shuffle_paths.copy()
            continue
        
        current = queue.pop(0)
        path = paths.pop(0)
        
        # break condition once we found enough good_nodes.
        if len(good_nodes) >= 50:
            break    
        
        # stop the branch if the current state satifies the conditions.
        current_start_dis = Hueristic(current, start_jugs)
        current_full_dis = Hueristic(current,full_jugs)
        
        start_dis_check = current_start_dis >= dis_from_start - tolerance and current_start_dis <= dis_from_start + tolerance 
        full_dis_check = current_full_dis >= dis_from_full - tolerance and current_full_dis <= dis_from_full + tolerance
        path_check = len(path) >= min_path_len and (current not in good_nodes)
        
        if start_dis_check and full_dis_check and path_check:
            good_nodes.append(current)
            continue
        
        # else we can extend the path if possible.
        for index,jug in enumerate(current):
            # fill empty jugs
            if jug < full_jugs[index]:
                next = fillJug(current,full_jugs,index)["jugs"].copy()
                if next not in path:
                    queue.insert(0,next)
                    paths.insert(0,path + [next])
            # pour jug into another
            for index2, jug2 in enumerate(current):
                if index2 == index:continue
                next = pourJug(current,full_jugs,index,index2)["jugs"].copy()
                if next not in path:
                    queue.insert(0,next)
                    paths.insert(0,path + [next])
            # empty jugs
            if jug > 0:
                next = emptyJug(current,full_jugs,index)["jugs"].copy()
                if next not in path:
                    queue.insert(0,next)
                    paths.insert(0,path + [next])
    
    # Now that we should have all the leaf nodes, we can pick ones for        
    player_goal = good_nodes.pop(random.randrange(0,len(good_nodes)))
    bot_goal = good_nodes.pop(random.randrange(0,len(good_nodes)))
    
    return {"pTarget": player_goal, "bTarget": bot_goal, "capacity": full_jugs, "start": start_jugs, "searchDepth":s_depth}
          
def settCustomise():
    print("CUSTOMISE SETTINGS: ")
    print(">> Here are the current settings: ")
    print("  >> Your Goal: ", pTarget)
    print("     to change type pGoal()")
    print("  >> Bot's Goal: ", bTarget)
    print("     to change type bGoal()")
    print("  >> Jug capacity: ", capacity)
    print("     to change type cap()")
    print("  >> Starting arrangement: ", starting)
    print("     to change type start()")    
    
def playAgain(sett_vars):
    print(">> Would you like to play again (Y/n)?")
    userIn = input("  >> ")
    if equalString(userIn,"y"):
        return game(sett_vars)
    if equalString(userIn,"n"):
        return wasting_water_UI(sett_vars)
    print(">> Invalid input")
    return playAgain(sett_vars)

def game(sett_vars):
    clear()
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
        lastmove = [starting]
        while True:
            if turnOrder[turn%2] == "p":
                while True:
                    print("------ <<< Your Turn >>> ------")
                    print("Jug Capacity:", capacity)
                    print("Your Goal:", sett_vars["pTarget"])
                    print("Bots Goal:", sett_vars["bTarget"])
                    print("Current Jug State:", jugs)
                    print(">> Type a move:")
                    print(">>> fill(<jug#>) -- fill a jug")
                    print(">>> fill(<jug A#>,<jug B#>) -- pour jug A into jug B until [will not overfill jug B]")
                    print(">>> empty(<jug#>)")
                    userIn = input("   >>> ")
                    
                    if strFind(userIn,"fill()",False,True):
                        jugNums = stringSubtract(userIn,"fill()").split(',')
                        #print(jugNums)
                        
                        # quickly check if the user input is valid
                        if len(jugNums) > 2: # are there too many numbers?
                            print(">> Too many values enter into fillJug. you can only fill one jug or pour one into another")
                            continue
                        if len(jugNums) < 1: # are there too little?
                            print(">> fill() needs at least one integer value. you can ether fill one jug or pour one into another")
                            continue
                        check = False
                        for j in jugNums: # are all the values digits (whole numbers)
                            if not(j.isdigit()): print(">> Values entered must be an integer"); check = True 
                            break
                        if not check: continue
                        
                        # quickly sees if the user entered two numbers, implying they wnated to pour from one jug to the next.
                        if len(jugNums) == 2:
                            results = pourJug(jugs,capacity,int(jugNums[0]) - 1 ,int(jugNums[1]) - 1,debug)                            
                            if len(lastmove) > 0 and results["jugs"] == lastmove[-1]:
                                print(">> You can't undo your oponents last move")
                                continue
                            jugs = results["jugs"]
                            lastmove.append(results["jugs"])
                            if len(lastmove) > reverseRestrain:
                                lastmove.pop(0)
                            break
                        results = fillJug(jugs,capacity,int(jugNums[0]) - 1,debug)
                        
                        if len(lastmove) > 0 and results["jugs"] == lastmove[-1]:
                            print(">> You can't undo your oponents last move")
                            continue  
                        jugs = results["jugs"]
                        lastmove.append(results["jugs"])
                        if len(lastmove) > reverseRestrain:
                            lastmove.pop(0)
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
                        if len(lastmove) > 0 and results["jugs"] == lastmove[-1]:
                            print(">> You can't undo your oponents last move")
                            continue
                        jugs = results["jugs"]
                        lastmove.append(results["jugs"])
                        if len(lastmove) > reverseRestrain + 1:
                            lastmove.pop(0)
                        break
                    
                    print(">> Invalid input")
                    
            if turnOrder[turn%2] == "b":
                print("\n\n")
                print("------ <<< Bot's Turn >>> ------")
                print("Jug Capacity:", capacity)
                print("Your Goal:", pTarget)
                print("Bots Goal:", bTarget)
                print("Current Jug State:", jugs)
                bot_move = search(jugs,capacity,sett_vars["searchDepth"],sett_vars["pTarget"],sett_vars["bTarget"],lastmove,debug)
                jugs = bot_move["jugs"]
                lastmove.append(bot_move["jugs"])
                if len(lastmove) > reverseRestrain + 1:
                    lastmove.pop(0)
                if bot_move["action"] == "fill":
                    print(">> Bot filled jug ", bot_move["index"][0] + 1)
                elif bot_move["action"] == "pour":
                    print(">> Bot poured jug", bot_move["index"][0] + 1, "into jug", bot_move["index"][1] + 1)
                elif bot_move["action"] == "empty":
                    print(">> Bot emptied jug", bot_move["index"][0] + 1)
                
            turn += 1
            #code for checking the winner...
            if jugs == pTarget:
                print(">> \033[3mCongratulations! You won!\033[0m")
                break
            if jugs == bTarget:
                print(">> \033[3mSorry The bot has won!\033[0m")
                break    
            
        return None

    print("Before we start...")
    turnOrder = goingFirst()
    clear()
    print("Alright Lets Begin!")
    playing(turnOrder,turn,sett_vars["start"],capacity)
    
    playAgain(sett_vars)
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

def search(jugs,capacity, depth, ptarget, btarget, lastmove, debug = False):
    # a function for pruning the leaf nodes that are no longer needed.
    def prune(queue,paths,common):
        """Prunes the paths of the unneeded branches.
         Does this by removing the path contianing 'common' and removing it latest value fromt he queue.
         Returns the new queue"""
        rl = []
        for p in paths:
            if listSubset(common,p):
               rl.append(p)
               queue.remove(p[-1]) 
        
        for p in rl:
            paths.remove(p)
        
        return queue
    
    #stores all the completed paths from root to node
    branches = []
    #stores all discovered states in order of which is to be called first
    queue = [{"jugs":jugs,"alpha": -float("inf"), "beta": float("inf"), "action": "none","index":[], "leaf": False}]
    #stores the branch of each state in the queue, it's in the same order as queue
    paths = [[queue[0]]]
    while len(queue) > 0:
        state = queue.pop(0)
        current_path = paths.pop(0)
        
        if debug:print("state: ", state,"\ncurrent_path: ", current_path)
        
        # assume that stae is a leaf node, correct assumption is proven wrong later.
        state["leaf"] = True
            
        #itterates through each jug filling and empting combination.
        for i,j1 in enumerate(state["jugs"]):
            if len(current_path) > depth-1:
                break
            
            # filling jugs...
            if j1 < capacity[i]:
                next_jugs = fillJug(state["jugs"],capacity,i)["jugs"].copy()
                newState = True #checking if the current_path has this option already
                for c in current_path:
                    newState = not(c["jugs"] == next_jugs)
                    if not newState: break
        
                if next_jugs not in lastmove and newState:
                    # if there can be a new node of of state node, the state node is not a leaf
                    state["leaf"] = False
                    # alpah and beta values are natrually inherited from the nodes above.
                    next_alpha = current_path[-1]["alpha"]
                    next_beta = current_path[-1]["beta"]
                    # if max depth reached then we have a leaf node.
                    leaf = len(current_path) == depth-1
                    
                    next_state = {"jugs": next_jugs,"alpha" : next_alpha,"beta": next_beta,"action": "fill", "index": [i], "leaf": leaf}
                    if debug:  print("[filling] next_state:",next_state)
                    queue.insert(0,next_state)
                    paths.insert(0,current_path + [next_state])
            
            # pouring one to another...
            for t, j2 in enumerate(jugs):
                if i == t: continue
                if j1 > 0 and j2 < capacity[t]:
                    next_jugs = pourJug(state["jugs"],capacity,i,t)["jugs"].copy()
                    newState = True #checking if the current_path has this option already
                    for c in current_path:
                        newState = not(c["jugs"] == next_jugs)
                        if not newState: break
 
                    if next_jugs not in lastmove and newState:
                        # if there can be a new node of of state node, the state node is not a leaf
                        state["leaf"] = False
                        # alpah and beta values are natrually inherited from the nodes above.
                        next_alpha = current_path[-1]["alpha"]
                        next_beta = current_path[-1]["beta"]
                        # if max depth reached then we have a leaf node.
                        leaf = len(current_path) == depth-1
                        
                        next_state = {"jugs": next_jugs,"alpha" : next_alpha,"beta": next_beta,"action": "pour", "index": [i,t], "leaf": leaf}
                        if debug:  print("[filling] next_state:",next_state)
                        queue.insert(0,next_state)
                        paths.insert(0,current_path + [next_state])
                        
            #empting jugs...
            if j1 > 0:
                next_jugs = emptyJug(state["jugs"],capacity,i)["jugs"].copy()
                newState = True #checking if the current_path has this option already
                for c in current_path:
                    newState = not(c["jugs"] == next_jugs)
                    if not newState: break
                
                if next_jugs not in lastmove and newState:
                    # if there can be a new node of of state node, the state node is not a leaf
                    state["leaf"] = False
                    # alpah and beta values are natrually inherited from the nodes above.
                    next_alpha = current_path[-1]["alpha"]
                    next_beta = current_path[-1]["beta"]
                    # if max depth reached then we have a leaf node.
                    leaf = len(current_path) == depth-1
                    
                    next_state = {"jugs": next_jugs,"alpha" : next_alpha,"beta": next_beta,"action": "empty", "index": [i], "leaf": leaf}
                    if debug:  print("[filling] next_state:",next_state)
                    queue.insert(0,next_state)
                    paths.insert(0,current_path + [next_state])
                    
        # Alpha/Beta pruning process.
        if state["leaf"]:
            # evaluate how close the current state is from losing or winning....
            loseEval = Hueristic(state["jugs"],ptarget)
            winEval = Hueristic(state["jugs"],btarget)
            if winEval == 0: value = math.inf
            else: value = loseEval/winEval
            # set the alpha/beta values....
            if (len(current_path)%2 == 1):
                state["alpha"] = value
            else:
                state["beta"] = value
            
            
            for i in range(len(current_path) - 1):
                n = -(i + 2) # might rephrase....
                if (len(current_path) - n)%2 == 0:
                    # if alpha cut conditions have been meet.
                    if current_path[n]["alpha"] > current_path[n+1]["beta"]:
                        # "prunes" the game tree by cutting out the path from the queue
                        t = len(current_path) - i
                        queue = prune(queue,paths,current_path[:t])
                        continue
                    current_path[n]["alpha"] = max(current_path[n]["alpha"],current_path[n+1]["beta"])
                else:
                    # if beta cut conditions have been meet.
                    if current_path[n]["beta"] < current_path[n+1]["alpha"]:
                        # "prunes" the game tree by cutting out the path from the queue
                        t = len(current_path) - i
                        queue = prune(queue,paths,current_path[:t])
                        continue
                    current_path[n]["beta"] = min(current_path[n]["beta"],current_path[n+1]["alpha"])
            branches.append(current_path)
            continue
        
    # picking the best choice for the bot.
    choice = branches[0][1]
    for p in branches:
        if p[1]["alpha"] > choice["alpha"]:
            print(p)
            choice = p[1]
            
    return choice

def Hueristic(current, target):
    total = 0
    for i,s in enumerate(current):
        total += pow((s - target[i]),2)
    total = math.sqrt(total)
    return total

# settings variables

pTarget = [5,1,2]
bTarget = [5,2,1]

capacity = [5,3,2]
searchDepth = 10
reverseRestrain = 3
debug = False
difficultyLv = 2

starting = [0,0,0]

sett_vars = {
    "pTarget":pTarget,
    "bTarget":bTarget,
    "capacity":capacity,
    "start":starting,
    "searchDepth":searchDepth,
    "diffLv": difficultyLv,
    "replayLimit":reverseRestrain,
    "debug":debug,
    
    }

wasting_water_UI(sett_vars)