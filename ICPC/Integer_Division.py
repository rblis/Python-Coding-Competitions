token = input().split()
d = int(token[1])
equals = {}
token = input().split()
for num in token:
    res = int(int(num)/d)
    if res in equals:
        equals[res] += 1
    else:
        equals[res] = 1
result = 0
for num in equals.values():
    if num >= 2:
        for summ in range(1,num):
            result += summ
print(result)
