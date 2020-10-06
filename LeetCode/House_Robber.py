'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
 the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and 
 it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money
 you can rob tonight without alerting the police.

'''

def rob(nums: List[int]) -> int:
    if len(nums) == 0: 
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1] #regular ternary operator

    sums = [0] * len(nums)
    sums[0] = nums[0]
    sums[1] = nums[1] if nums[1] > nums[0] else nums[0]
    for index in range(2, len(nums)):#Tuple based ternary operator not as efficient as tuple is created/computed for both values
        sums[index] = (nums[index] + sums[index-2], sums[index-1])[nums[index]+sums[index-2] < sums[index-1]]
    return sums[-1]