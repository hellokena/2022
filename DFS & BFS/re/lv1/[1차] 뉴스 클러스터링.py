from collections import Counter
# 자카드 유사도 : 교집합 / 합집합
def solution(str1, str2):
    array1, array2 = [], []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha(): array1.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha(): array2.append(str2[i:i+2].lower())
    #if len(array1) == 0 and len(array2) == 0: return 65536
    all_num = set(array1+array2)
    a1 = Counter(array1)
    a2 = Counter(array2)
    intersect = []
    union = []
    for num in all_num:
        for i in range(min(a1[num], a2[num])):
            intersect.append(num)
        for i in range(max(a1[num], a2[num])):
            union.append(num)
    if not union: return 65536 # intersect는 없을 수도 있음
    return int(len(intersect)/len(union)*65536)
    

# 자카드 유사도 : 교집합 / 합집합
def solution(str1, str2):
    array1, array2 = [], []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha(): array1.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha(): array2.append(str2[i:i+2].lower())
    #if len(array1) == 0 and len(array2) == 0: return 65536
    all_num = set(array1+array2)
    intersect = []
    union = []
    for num in all_num:
        intersect.extend([num]*min(array1.count(num),array2.count(num)))
        union.extend([num]*max(array1.count(num), array2.count(num)))
    if not union: return 65536 # intersect는 없을 수도 있음
    return int(len(intersect)/len(union)*65536)
