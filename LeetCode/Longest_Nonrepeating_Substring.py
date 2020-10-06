
def lengthOfLongestSubstring(s: str) -> int:
    dic, back_index, max_count = {}, 0, 0
    for front_index, character in enumerate(s):# stores the index at dictionary location
        if character in dic and dic[character] + 1 > back_index:                
            back_index = dic[character] +1 # sets the new back index to the index of the duplicitous char in substring
        if (front_index - back_index + 1) > max_count:# computes the current length of non repeating substring
            max_count = front_index - back_index + 1
        dic[character] = front_index
    return max_count
    
    
print(lengthOfLongestSubstring("ckilbkd"))



'''
Original Attempt
dic = {}
    order = 0
    count = 0
    max_count = 0
    last_char = ''
    for char in s:
        if char in dic:
            if dic[char] != order:
                count += 1
            else:
                if char == last_char:
                    if count > max_count:
                        max_count = count
                    count = 1
                    order += 1
                else:
                    if count > max_count:
                        max_count = count                          
                
            dic[char] = order
        else:
            dic[char] = order
            count += 1
        last_char = char

    if count > max_count:
        max_count = count
    return max_count
'''