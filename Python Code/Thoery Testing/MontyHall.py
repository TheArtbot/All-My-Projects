import random
import math
import pandas

def MontyHaul(n,a,switchState):
    # i was orginally planing to make it so you could increase the number of "sports cars" behind the door
    # but i decided it's doesn't matter now that i understood the formula for calculating your chances of winning.
    # Pr(win) = Pr(that you were wrong before) * Pr(that you're correct now) = ((n-k)/n) * (k/(n-p-1))
    # where: n -> #of doors, k -> #of "sports cars", p -> #number of doors monty throws out.
    
    # the game when you don't "switch" but just "pick again"
    def game(a):
        doors = [0 for _ in range(a)]
        for i in range(1):
            index = random.randrange(a)
            if doors[index] != 0: i -= 1; continue
            doors[index] = 1
        
        players_choice = random.randrange(a)
        host_choice = random.randrange(a)
        while (host_choice == players_choice) or (doors[host_choice] != 0): 
            host_choice = random.randrange(a)
        doors.pop(host_choice)
        if host_choice < players_choice: 
            players_choice -= 1
        switch = (50 < random.randrange(100))
        
        if switch: players_choice = random.randrange(a-1)
        win = (doors[players_choice] != 0)
        
        return {"Win":win,"Switch":switch}
        
    # the game when you do "switch"
    def game2(a):
        doors = [0 for _ in range(a)]
        for i in range(1):
            index = random.randrange(a)
            if doors[index] != 0: i -= 1; continue
            doors[index] = 1
        
        players_choice = random.randrange(a)
        switch = (50 < random.randrange(100))
        
        host_choice = random.randrange(a)
        while (host_choice == players_choice) or (doors[host_choice] != 0): 
            host_choice = random.randrange(a)
        doors.pop(host_choice)
        if host_choice < players_choice: 
            players_choice -= 1
        
        if switch:
            final_player_choice = random.randrange(a-1)
            while final_player_choice == players_choice:
                final_player_choice = random.randrange(a-1)
        else:
            final_player_choice = players_choice
            
        win = (doors[final_player_choice] != 0)
        return {"Win":win,"Switch":switch}

    # game when monty doesn't remove a door
    def game3(a):
        doors = [0 for _ in range(a)]
        for i in range(1):
            index = random.randrange(a)
            if doors[index] != 0: i -= 1; continue
            doors[index] = 1
        
        players_choice = random.randrange(a)
        switch = (50 < random.randrange(100))
        
        if switch:
            final_player_choice = random.randrange(a)
            while final_player_choice == players_choice:
                final_player_choice = random.randrange(a)
        else:
            final_player_choice = players_choice
            
        win = (doors[final_player_choice] != 0)
        
        return {"Win":win,"Switch":switch}
        
    
    results = []
    scores = [[0,0],[0,0]] # [switch[win,loss],non-switch[win,loss]]
    for _ in range(n):
        if switchState == 0 :single_result = game(a)
        elif switchState == 1: single_result = game2(a)
        elif switchState == 2: single_result = game3(a)
        
        if single_result["Switch"]: s_i = 0
        else: s_i = 1
        if single_result["Win"]: w_i = 0
        else: w_i = 1
        scores[s_i][w_i] += 1
        
        results.append(single_result)
        #df = pandas.DataFrame(results)
    
    print("Switching should tend towards:", (a-1)/(a**2 - 2*a))
    print("Win Rates of a statagey against when that statagey loss")
    print("Switching Win rate:",(scores[0][0]/sum(scores[0])))
    print("Non-Switching Win rate:", (scores[1][0]/sum(scores[1])))   
    print()
    print("Switching and Non-Switching Rates")
    print("Switching rate:",(sum(scores[0])/(sum(scores[0]) + sum(scores[1]))))
    print("Non-Switching rate:", (sum(scores[1])/(sum(scores[0]) + sum(scores[1])))) 
    
    
MontyHaul(100,3,2)
