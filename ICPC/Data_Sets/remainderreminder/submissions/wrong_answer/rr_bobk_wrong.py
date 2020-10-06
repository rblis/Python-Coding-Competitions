#!/usr/bin/python

def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def modinv(a,n):
#    global t
#    global u
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

    if t < 0:
        t += n
    return t

(sheetLength,sheetWidth,rem1,rem2,rem3,minBooks,maxBooks) = map(int,raw_input().split())

bestH = int(0.5 + (sheetLength + sheetWidth - (sheetWidth * sheetWidth + \
    sheetLength * sheetLength - sheetWidth * sheetLength) ** 0.5) / 6)

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


m1 = v1 // gcd(v1,v2)
m1 = m1 // gcd(m1,v3)
m2 = v2 // gcd(v1,v2)
m2 = m2 // gcd(m2,v3)
m3 = v3 // gcd(v1,v3)
#print m3
m3 = m3 // gcd(m3,v2)

#print gcd(m1,m2),gcd(m1,m3),gcd(m2,m3)

maxM = m1 * m2 * m3

if maxBooks - minBooks + 1 > maxM:
    print "Answer is not unique!"

#print m1,m2,m3,m1*m2*m3

r1 = rem1 % m1
r2 = rem2 % m2
r3 = rem3 % m3

mhat1 = m2 * m3
mhat2 = m1 * m3
mhat3 = m2 * m1

mhatinv1 = modinv(mhat1,m1)
mhatinv2 = modinv(mhat2,m2)
mhatinv3 = modinv(mhat3,m3)

#print mhat1,mhat2,mhat3
#print mhatinv1,mhatinv2,mhatinv3

n = (mhat1 * mhatinv1 * r1 + mhat2 * mhatinv2 * r2 + mhat3 * mhatinv3 * r3) % maxM

#print r1,r2,r3,n

answer = ((maxBooks - n) // maxM) * maxM + n

print answer

