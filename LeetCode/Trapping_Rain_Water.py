'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
'''

def trap(height) -> int:
    if len(height) < 3:
        return 0
    pool = 0
    index = 1
    while index < len(height):
        if height[index] < height[index-1]:
            end_index, add_pool = find_end(height, index-1)
            if end_index != -1:
                pool += add_pool
                index = end_index
            else: 
                index += 1
        else:
            index += 1

    return(pool)

def find_end(height, start_index) -> int:
    start_height = height[start_index]
    end_index = -1
    pool = 0
    for index in range(start_index+1, len(height)):
        pool += start_height-height[index]
        if height[index] >= start_height:
            end_index = index
            pool -= start_height-height[index]
            break
        elif height[index] > height[index-1]:
            end_index = index
    return end_index, pool


print(trap([4,2,3]))
            