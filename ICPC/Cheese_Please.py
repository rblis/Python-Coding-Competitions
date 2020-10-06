token = input().split()
n, m = int(token[0]), int(token[1])
token = input().split()
weights = [0]*n
for index in range(0,n):
    weights[index] = int(token[index])
#size mxn array
percents = [[0 for i in range(n+1)] for j in range(m)]  
for index1 in range(0,m):
    token = input().split()
    for index2 in range(0,n):
        percents[index1][index2] = float(token[index2])/100.0
    percents[index1][-1] = float(token[-1])
percents.sort(key=lambda x: x[-1], reverse=True)
