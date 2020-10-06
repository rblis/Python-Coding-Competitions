        
# def solution(N):
#     global solutionx
#     solutions = [0]*N
#     solve(N,0,0, solutions)    
#     return solutionx
        

# solved = False
# solutionx = []
  
# def solve(target: int, iteration: int, sum: int, solutions: list):    
#     global solved
#     if target == sum:
#         solved = True
#         solutionx = solutions[0:iteration]
#     start = 1;
#     if iteration > 0:
#         start = solutions[iteration - 1] + 2;
#     odd_interval = start
#     while target >= odd_interval:
#         if not solved and target >= sum + odd_interval:
#             solutions[iteration] = odd_interval
#             solve(target,iteration+1, sum + odd_interval)
#         else: 
#             return
#         odd_interval += 2





# depth = 0
# def solution(T):
#     distinct_set = set()
#     dfs(T, distinct_set)
#     return depth

# def dfs(T, distinct_set: set):
#     if T.x in distinct_set:
#         return
#     else:
#         distinct_set.add(T.x)
#         if depth < len(distinct_set):
#             depth = len(distinct_set)
#         if T.l != None:
#             dfs(T.l, distinct_set)
#         if T.r != None:
#             dfs(T.r, distinct_set)
#         distinct_set.remove(T.x)



    # stack = collections.deque()
    # distinct_set = set()    
    # depth = 0
    # stack.append(T)
    # while stack:
    #     pop_node = stack.pop()
    #     if pop_node.x in distinct_set:
    #         pass
    #     else:
    #         distinct_set.add(pop_node.x)
    #         if depth < len(distinct_set):
    #             depth = len(distinct_set)
    #     if pop_node.r != None:
    #         stack.append(pop_node.r)
    #     if pop_node.l != None:
    #         stack.append(pop_node.l)
            
    # return depth

    