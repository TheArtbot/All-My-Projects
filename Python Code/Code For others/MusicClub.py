import math

def CountDisagrements(order_,lst_,k,n):
    fisrt = order_.copy()
    others = [item.copy() for item in lst_]
    
    disagree = [0 for _ in range(n)]
     
    for _ in range(k):
        p = fisrt.pop(0)
        for m_index in range(n):
            disagree[m_index] += others[m_index].index(p)
            others[m_index].remove(p) 
    return disagree

k = 5
n = 4
m = 10
members_profile = [[2,5,1,3,4],[3,4,2,1,5],[2,3,1,5,4],[1,2,5,4,3]]
members_topRankLst = [[57, 23, 10, 15, 7, 2, 19, 27, 41, 61],[33, 17, 19, 27, 61, 99, 91, 57, 71, 50],[10, 23, 2, 72, 61, 57, 41, 27, 50, 47],[7, 19, 61, 51, 19, 80, 84, 43, 31, 90]]

disagreements = CountDisagrements(members_profile[0],members_profile[1:],k,n - 1)
minimum = min(disagreements)
min_index = [i+1 for i in range(0,n-1) if disagreements[i] == minimum]

similar_topRankLst = [ members_topRankLst[i] for i in range(n) if i in min_index]

best_songs = []
for ranking in range(m):
    best_songs = [-1 for _ in range(len(min_index))]
    for member, lst in enumerate(similar_topRankLst):
        if lst[ranking] not in members_topRankLst[0]:
            best_songs[member] = lst[ranking]
    while -1 in best_songs: best_songs.remove(-1)
    if len(best_songs) > 0: break

if len(best_songs) > 0: print(min(best_songs))
else: print(-1)
    
        