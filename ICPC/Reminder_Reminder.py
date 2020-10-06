token = input().split()
x = int(token[0])
y = int(token[1])
box1 = int(token[2])
box2 = int(token[3])
box3 = int(token[4])
start = int(token[5])
end = int(token[6])

first, second, third = (x-2)*(y-2), (x-4)*(y-4)*2, (x-6)*(y-6)*3
x-=8
y-=8
z = 4

bestH = int(0.5 + (x + y - (y * y + x * x - y * x) ** 0.5) / 6)

v1 = (y - 2 * bestH) * (x - 2 * bestH) * bestH
v2 = (y - 2 * (bestH-1)) * (x - 2 * (bestH-1)) * (bestH-1)
v3 = (y - 2 * (bestH+1)) * (x - 2 * (bestH+1)) * (bestH+1)
v4 = (y - 2 * (bestH-2)) * (x - 2 * (bestH-2)) * (bestH-2)
v5 = (y - 2 * (bestH+2)) * (x - 2 * (bestH+2)) * (bestH+2)
xx = [v1,v2,v3,v4,v5]
xx.sort()
first = xx[4]
second = xx[3]
third = xx[2]

# while x > 1 and y > 1:
#     if first < second and second > third:
#         break;
#     first, second, third = second, third, x*y*z
#     x,y,z = x-2,y-2,z+1

# if first > second and second > third:
#     None
# else:
#     if first < third:
#         temp = first
#         first, second, third = second, third, temp
#     else:
#         temp = first
#         first, second = second, temp


if box1-(start%first) >= 0:
    start += box1-(start%first)
else:
    start += box1-(start%first)+first

while start <= end:
    if start%second == box2:
        if start%third == box3:
            print(start)
            break
    start+=first
#print(first,second,third)