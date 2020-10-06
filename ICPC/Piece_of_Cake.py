

token = input().split()
n,h,v = int(token[0]), int(token[1]), int(token[2])
x = h if h > (n-h) else (n-h)
y = v if v > (n-v) else (n-v)
print(x*y*4)

