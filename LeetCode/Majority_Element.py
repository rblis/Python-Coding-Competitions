def majorityElement(nums: List[int]) -> int:
    dic: dict[int:int] = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1;
        else:
            dic[num] += 1;
    majority, count = 0,0 
    for num in dic.keys():
        if dic[num] > count:
            majority = num
            count = dic[num]
    return majority