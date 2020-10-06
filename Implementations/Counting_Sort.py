def Counting_Sort(arr):    
    max_val = 0
    for num in arr:
        if(num > max_val):
            max_val = num
    count_array = [0]*(max_val+1)
    for num in arr:
        count_array[num] += 1
    
    for i in range(1,max_val+1):
        count_array[i] += count_array[i-1]
    temp = count_array[0]
    shift = 0
    for i in range(1,max_val+1):
        shift = count_array[i]
        count_array[i] = temp
        temp = shift    
    count_array[0] = 0
    sorted_array = [0]*(len(arr))
    for ind in arr:
        sorted_array[count_array[ind]] = ind
        count_array[ind] += 1

Counting_Sort([1,0,3,1,3,1])
