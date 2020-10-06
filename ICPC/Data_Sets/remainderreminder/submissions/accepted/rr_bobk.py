#!/usr/bin/python

def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def modinv(a,n):
    global t
    global u
    t = 0
    newt = 1
    u = 1
    newu = 0
    r = n
    newr = a

    while newr != 0:
        q = r // newr
        (t,newt) = (newt,t-q*newt)
        (u,newu) = (newu,u-q*newu)
        (r,newr) = (newr,r-q*newr)

    if r > 1:
        print "Error"

(sheetLength,sheetWidth,rem1,rem2,rem3,minBooks,maxBooks) = map(int,raw_input().split())

bestH = int(0.5 + (sheetLength + sheetWidth - (sheetWidth * sheetWidth + sheetLength * sheetLength - sheetWidth * sheetLength) ** 0.5) / 6)

v1 = (sheetWidth - 2 * bestH) * (sheetLength - 2 * bestH) * bestH
v2 = (sheetWidth - 2 * (bestH-1)) * (sheetLength - 2 * (bestH-1)) * (bestH-1)
v3 = (sheetWidth - 2 * (bestH+1)) * (sheetLength - 2 * (bestH+1)) * (bestH+1)
v4 = (sheetWidth - 2 * (bestH-2)) * (sheetLength - 2 * (bestH-2)) * (bestH-2)
v5 = (sheetWidth - 2 * (bestH+2)) * (sheetLength - 2 * (bestH+2)) * (bestH+2)

x = [v1,v2,v3,v4,v5]
x.sort()
v1 = x[4]
v2 = x[3]
v3 = x[2]

t = u = 0

g = gcd(v1,v2)
modinv(v1/g,v2/g)

mod = v1 / g * v2

answer = (rem1 * (v2 / g)*u + rem2 * (v1/g)*t) % mod

if answer < 0:
    answer += mod
v1 = mod

t = u = 0

g = gcd(v1,v3)
modinv(v1/g,v3/g)

mod = v1 / g * v3

answer = (answer * (v3 / g)*u + rem3 * (v1/g)*t) % mod

while answer < minBooks:
    answer += mod
while answer > maxBooks:
    answer -= mod

if answer + mod <= maxBooks or answer - mod >= minBooks:
    print "Answer is not unique!"

print answer
