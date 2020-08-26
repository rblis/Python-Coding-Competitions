'''
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to

the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days
and a client's total daily expenditures for a period of days, find and print the number of times the client will receive a notification over all

days.

For example,
and . On the first three days, they just collect spending data. At day , we have trailing expenditures of . The median is and the day's expenditure is . Because , there will be a notice. The next day, our trailing expenditures are and the expenditures are . This is less than

so no notice will be sent. Over the period, there was one notice sent.

Note: The median of a list of numbers can be found by arranging all the numbers from smallest to greatest. If there is an odd number of numbers, the middle one is picked. If there is an even number of numbers, median is then defined to be the average of the two middle values. 
'''
def getMedian(arr, d):
    count_arr = arr.copy()
    for i in range(len(arr)):
        count_arr[i] += count_arr[i-1]    
    a,b = 0,0
    if(d%2==0):
        first = int(d/2)
        second = first+1
        i = 0
        while(i <201):
            if(first<=count_arr[i]):
                a=i 
                break
            i += 1
        while(i < 201):
            if(second <= count_arr[i]):
                b = i
                break
            i+= 1
    else:
        first = int(d/2) +1
        for i in range(201):
            if(first <= count_arr[i]):
                a = 2*i
                break
    return (a+b)
                



# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    exp = expenditure[:d] 
    count_array = [0]*(201)
    notifs = 0
    for num in exp: #number of occurances
        count_array[num] += 1    
    for i in range(d,len(expenditure)):
        mid = getMedian(count_array,d)
        if(expenditure[i] >= mid):
            notifs += 1
        count_array[expenditure[i]] += 1
        count_array[expenditure[i-d]] -= 1

    return notifs




print(activityNotifications([1,2,3,4,5],3))
    
    #activityNotifications([2,3,4,2,3,6,8,4,5],5))


'''
Original Attempt
    exp = expenditure[:d] 
    count_array = [0]*(201)
    for num in exp: #number of occurances
        count_array[num] += 1
    mid = 0
    counter: int = 0
    overshoot: int = 0
    for i in range(201):
        if(count_array[i] != 0):
            counter += count_array[i]
        if(counter >= (d+1)/2):
            mid = i
            if(counter > d/2+1):
                overshoot = int(counter - d/2+1)
            break
    print(mid)
    print(overshoot)
    #print(count_array[mid])
'''
