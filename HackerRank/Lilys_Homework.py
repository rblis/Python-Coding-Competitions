'''
Whenever George asks Lily to hang out, she's busy doing homework. George wants to help her finish it faster, but he's in over his head! Can you help George understand Lily's homework so she can hang out with him?

Consider an array of
distinct integers, . George can swap any two elements of the array any number of times. An array is beautiful if the sum of among

is minimal.

Given the array

, determine and return the minimum number of swaps that should be performed in order to make the array beautiful.

For example,
. One minimal array is

. To get there, George performed the following swaps:

Swap      Result
      [7, 15, 12, 3]
3 7   [3, 15, 12, 7]
7 15  [3, 7, 12, 15]

It took

swaps to make the array beautiful. This is minimal among the choice of beautiful arrays possible.

Function Description

Complete the lilysHomework function in the editor below. It should return an integer that represents the minimum number of swaps required.

lilysHomework has the following parameter(s):

    arr: an integer array

Input Format

The first line contains a single integer,
, the number of elements in . The second line contains space-separated integers

.

Constraints

Output Format

Return the minimum number of swaps needed to make the array beautiful.

Sample Input

4
2 5 3 1

Sample Output

2

Explanation

Let's define array
to be the beautiful reordering of . The sum of the absolute values of differences between its adjacent elements is minimal among all permutations and only two swaps ( with and then with ) were performed.

'''

# Complete the lilysHomework function below.
def lilysHomework(arr):
    arrD = arr.copy()
    ascend = arr.copy()
    descend = arr.copy()
    ascend.sort()
    descend.sort(reverse = True)

    dicA, dicD = {},{}
    swapsA, swapsD = 0,0
    for i in range(len(arr)):
        dicA[arr[i]] = i
        dicD[arr[i]] = i
    for i in range(len(arr)):        
        if(arr[i] != ascend[i]):
            index = dicA[ascend[i]]#get index of swap location
            dicA[ascend[i]] = i #swap the indexes of the two keys
            dicA[arr[i]] = index
            temp = arr[i]
            arr[i] = arr[index]
            arr[index] = temp
            swapsA += 1
        if(arrD[i] != descend[i]):
            index = dicD[descend[i]]#get index of swap location
            dicD[descend[i]] = i #swap the indexes of the two keys
            dicD[arrD[i]] = index
            temp = arrD[i]
            arrD[i] = arrD[index]
            arrD[index] = temp
            swapsD += 1
    if(swapsA > swapsD):
        return swapsD
    else:
        return swapsA
        
    

print(lilysHomework([3,4,2,5,1]))                



'''
Original Attempt

swaps: int = 0
    abs_min = 0
    new_abs_min = -1    
    index = 0 # right index of the differnce pair
    diff = 0
    while(new_abs_min < abs_min):
        big_diff = -1
        new_abs_min = 0
        abs_min = 0
        for i in range(len(arr)-1):
            diff = abs(arr[i]-arr[i+1])
            abs_min += diff
            if(diff > big_diff):
                index = i+1
                big_diff = diff   
        swap_index = index
        min_diff = big_diff
        
        diff = abs(arr[index]-arr[1])
        if(diff < min_diff):
            min_diff = diff
            swap_index = i
        for i in range(1,len(arr)-1):
            if(i != index):
                diff = abs(arr[index]-arr[i+1])
                if(diff < min_diff):
                    min_diff = diff
                    swap_index = i
        if(swap_index != index):
            temp = arr[swap_index]
            arr[swap_index] = arr[index]
            arr[index] = temp
            swaps += 1

        for i in range(len(arr)-1):
            diff = abs(arr[i]-arr[i+1])
            new_abs_min += diff        
    return (swaps-1)


Second Attempt

    ascend = arr.copy()
    swapsA, swapsD = 0,0
    indexA, indexD = 0, len(arr)-1    
    for i in range(len(arr)):
        minA, maxD = ascend[i], arr[len(arr)-i-1]
        for j in range(i,len(arr)):
            if(ascend[j] < minA):#small to big
                minA = ascend[j]
                indexA = j
            if(arr[len(arr)-j-1] > maxD):#big to small
                maxD = arr[len(arr)-j-1]
                indexD = len(arr)-j-1
        if(minA != ascend[i]):
            temp = ascend[i]
            ascend[i] = ascend[indexA]
            ascend[indexA] = temp
            swapsA += 1
        if(maxD != arr[len(arr)-i-1]):
            temp = arr[i]
            arr[i] = arr[len(arr)-i-1]
            arr[len(arr)-i-1] = temp
            swapsD += 1
    if(swapsA > swapsD):
        return swapsD
    else:
        return swapsA
'''