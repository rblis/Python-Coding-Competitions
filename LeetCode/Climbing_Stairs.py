'''

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


def climbStairs(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    fib = [1,1] + [0]*(n-2)
    #print(fib)
    for index in range(2,n):
        fib[index] = fib[index-1] + fib[index-2]
    #print(fib)
    return fib[-1]
print(climbStairs(6))