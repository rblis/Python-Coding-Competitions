from collections import deque

dictionary = {}
def getWays(n, c):
    if n == 0:#fully divisible
        return 1
    if c == []:#not possible to divide any further
        return 0
    memo = str(n) + ',' + str(c[-1])    
    if memo in dictionary:
        return dictionary[memo]
    divisions, combinations = int(n/c[-1]), 0
    for multiplier in range(divisions+1):
        combinations += getWays(n-c[-1]*multiplier, c[:-1])
        dictionary[memo] = combinations
    return combinations

n = 10
c = [2,3,5,6]
print(getWays(n,c))
