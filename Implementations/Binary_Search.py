n = 0
high, low = n-1,0
num = 0
arr = []
while(high>=low):
    mid = low + (high-low)//2
    if arr[mid] == num:
        break
    if arr[mid] > num:
        high = mid - 1
    else:
        low = mid + 1
    high, low = n-1,0