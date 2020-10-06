sett = set()
def countSubstrings(s: str) -> int:
    back_index, front_index = 0,1
    count = 0
    while front_index <= len(s) and back_index < len(s):
        if checkPalindrome(s, back_index, front_index):
            count += 1
        front_index += 1
        if front_index > len(s) and back_index < len(s):
            back_index +=1 
            front_index = back_index+1
    return count
        

def checkPalindrome(s, back_index, front_index):
    substr = s[back_index:front_index]
    if substr in sett:
        return True
    for index in range(0,int(len(substr)/2)):
        if substr[index] != substr[-(index+1)]:
            return False
    sett.add(substr)
    return True

print(countSubstrings('abc'))