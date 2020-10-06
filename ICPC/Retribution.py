'''
The coaches in a certain regional are fed up with the judges. During the last contest over 90

% of the teams failed to solve a single problem—in fact, even half the judges found the problems 
too hard to solve. So the coaches have decided to tar and feather the judges. They know the locations 
of all the judges as well as the locations of tar repositories and feather storehouses. They would like 
to assign one repository and one storehouse to each judge so as to minimize the total distances involved. 
But this is a hard problem and the coaches don’t have time to solve it (the judges are evil but not stupid—they 
have a sense of the unrest they’ve fomented and are getting ready to leave town). So instead they’ve decided to 
se a greedy solution. They’ll look for the smallest distance between any tar repository and any judge location 
and assign that repository to that judge. Then they’ll repeat the process with the remaining repositories and 
judges until all the judges have a repository assigned to them. After they’re finished with the tar assignments 
they’ll do the same with the feather storehouses and the judges. Your job is to determine the total distances 
between repositories and storehouses and their assigned judges.

All judges, tar repositories and feather storehouses are numbered 1,2,…

. In case of any ties, always assign a repository/storehouse to the lowest numbered judge first. If there is 
still a tie, use the lowest numbered repository/storehouse.

Better hurry up—an unmarked van has just been spotted pulling up behind the judges’ room.
Input

Input starts with a line containing three positive integers: n
m p (1≤n≤m,p≤1000), representing the number of judges, tar repositories and feather storehouses, respectively. 
Following this are n lines, each containing two integers x y (|x|,|y|≤10000) specifying the locations of the n 
judges, starting with judge 1. This is followed by m similar lines specifying the locations of the tar repositories 
(starting with repository 1) and p lines specifying the locations of the feather storehouses (starting with storehouse 1

).
Output

Output the the sum of all distances between judges and their assigned tar repositories and feather storehouses, 
using the greedy method described above. Your answer should have an absolute or relative error of at most 10−6
.
'''


from decimal import *
class point:
    def __init__(i):
        i.x = 0
        i.y = 0
        i.rank = 0
        i.dist = -1



def distance(point1: point, point2: point):
    return Decimal( ((point1.x-point2.x)**2) + ((point1.y-point2.y)**2) ).sqrt().quantize(Decimal('.000001'))

token = input().split()
n, m , p  = int(token[0]), int(token[1]), int(token[2])
judges, tars, feaths = [None]*n,[None]*m,[None]*p

for i in range(0,n):
    judges[i] = point()
    token = input().split()
    judges[i].rank = i
    judges[i].x = int(token[0])
    judges[i].y = int(token[1])

for i in range(0,m):
    tars[i] = point()
    token = input().split()
    tars[i].rank = i
    tars[i].x = int(token[0])
    tars[i].y = int(token[1])

for i in range(0,p):
    feaths[i] = point()
    token = input().split()
    feaths[i].rank = i
    feaths[i].x = int(token[0])
    feaths[i].y = int(token[1])


total_distance = Decimal("0.0")

for j in range(0,n):
    j_mini, tars_min = 0, Decimal('Infinity')
    for t in range(0,m):
        calc_dist = distance(judges[j], tars[t])
        if calc_dist < tars_min:
            tars_min = calc_dist
            j_mini = t
    jj_mini = 0
    for jj in range(0,n):
        if jj != j:
            calc_dist = distance(judges[jj], tars[j_mini])
            if calc_dist < tars_min:
                tars_min = calc_dist
                jj_mini = jj
            elif calc_dist == tars_min:
                if jj < j:
                    jj_mini = jj
    total_distance += tars_min

for j in range(0,n):
    j_mini, feaths_min = 0, Decimal('Infinity')
    for f in range(0,p):
        calc_dist = distance(judges[j], feaths[f])
        if calc_dist < feaths_min:
            feaths_min = calc_dist
            j_mini = f
    jj_mini = 0

    for jj in range(0,n):
        if jj != j:
            calc_dist = distance(judges[jj], feaths[j_mini])
            if calc_dist < feaths_min:
                feaths_min = calc_dist
                jj_mini = jj
            elif calc_dist == feaths_min:
                if jj < j:
                    jj_mini = jj
    total_distance += feaths_min




print(total_distance.quantize(Decimal('.000001')))


# while judge_i < n:
#     tars_min_i, tars_min = 0, float('inf')
#     for i in range(0, m):
#         calc_dist = distance(judges[judge_i], tars[i])
#         if calc_dist < tars_min:
#             tars_min = calc_dist
#             tars_min_i = i
#     tars_j

#     feaths_min_i, feaths_min = 0, float('inf')
#     for i in range(0, p):
#         if feaths[i].rank != -1:
#             calc_dist = distance(judges[judge_i], feaths[i])
#             if calc_dist < feaths_min:
#                 feaths_min = calc_dist
#                 feaths_min_i = i
#     total_distance += feaths_min
#     feaths[feaths_min_i].rank = -1
#     judge_i += 1

# for i in range(0,m):
#     judge_min_i, tars_min = 0, float('inf')
#     for j in range(0,n):
#         calc_dist = distance(judges[j], tars[i])
#         if calc_dist < tars_min:
#             tars_min = calc_dist
#             judge_min_i = j
#         elif calc_dist == tars_min:
#             if j < judge_min_i:
#                 judge_min_i = j
#     total_distance += tars_min
            
# for i in range(0,p):
#     judge_min_i, feath_min = 0, float('inf')
#     for j in range(0,n):
#         calc_dist = distance(judges[j], feaths[i])
#         if calc_dist < feath_min:
#             feath_min = calc_dist
#             judge_min_i = j
#         elif calc_dist == feath_min:
#             if j < judge_min_i:
#                 judge_min_i = j
#     total_distance += feath_min



