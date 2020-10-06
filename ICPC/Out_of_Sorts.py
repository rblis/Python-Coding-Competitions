token = input().split()
n,m,a,c,x = int(token[0]),int(token[1]),int(token[2]),int(token[3]),int(token[4])

unsortd_seq = [0]*n
unsortd_seq[0] = (a*x+c)%m
for index in range(1,n,):
    unsortd_seq[index] = (a*unsortd_seq[index-1]+c)%m

count, high, low, mid = 0, n-1, 0, 0
for num in unsortd_seq:    
    while(high>=low):
        mid = low + (high-low)//2
        if unsortd_seq[mid] == num:
            count+=1
            break
        if unsortd_seq[mid] > num:
            high = mid - 1
        else:
            low = mid + 1
    high, low = n-1,0
print(count)
    # if unsortd_seq[0] == num or unsortd_seq[-1] == num:
    #     count+=1
    #     continue
# sortd_seq = [0]*n
# sortd_seq[0] = (a*x+c)%m
    # sortd_seq[index] = unsortd_seq[index]
    # for index2 in range(index, 0, -1):
    #     if sortd_seq[index2] < sortd_seq[index2-1]:
    #         sortd_seq[index2-1] += sortd_seq[index2]
    #         sortd_seq[index2] = sortd_seq[index2-1] - sortd_seq[index2]
    #         sortd_seq[index2-1] = sortd_seq[index2-1] - sortd_seq[index2]
    #     else:
    #         break
    # if unsortd_seq[index] == sortd_seq[index]: 
    #     count+= 1
