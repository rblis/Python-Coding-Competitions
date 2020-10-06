'''
In fantasy hockey, there are n team owners that each selects k

hockey players. To determine which owner gets which players, the owners hold a draft.

The draft proceeds as follows: the first owner may select any player, then the second owner can select any player 
except the player taken first and so on. In general, the current owner may take any player that has not been taken previously. 
Once all owners have selected one player, they repeat this process until all owners have selected k

players. No player may be selected by multiple teams.

Initially, all players are given a ranking based on how well they played in the previous year. 
However, the owners may not agree with this order. For example, the first owner may believe that the player 
which was ranked third in the previous year is the best player and would prefer to take them.

Each owner has a preference list. On their turn, the owner selects the player that is the highest available
 player on their own preference list. If all players on their preference list are taken, then they resort 
 to using the ordering from the previous year.

Given the preference list of each owner and the rankings from the previous year, which players did each owner get?
'''
import os, collections
input = open('ICPC\Fantasy_Draft\\2.in', 'r')
token = input.readline().split()
n,k = int(token[0]), int(token[1])
coach_prefs = [0]*n
players = {}
for index in range(0,n):
    token = input.readline().split()
    q = int(token[0])
    coach_prefs[index] = collections.deque()
    if q > 0:
        for index2 in range(1,q+1):
            coach_prefs[index].append(token[index2])   
p = int(input.readline().split()[0])
draft_list = []*p
for index in range(0,p):
    token = input.readline().split()[0]
    players[token] = True
    draft_list[index] = token
input.close()
draft = []*n

for index in range(0,n):
    draft[index] = collections.deque()
count = 0
index = 0
while count < n*k:
    #find next available player
    while index < p and players[draft_list[index]] != False:
        index+=1
    #go through list of players 
    for coachIndex in range(0,n):
        next


def solution(n: int, k: int):
    return