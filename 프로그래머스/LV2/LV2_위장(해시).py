from collections import defaultdict
def solution(clothes):
    clotheslist = defaultdict(int)
    for n,t in clothes:
        clotheslist[t] += 1
    answer = 1
    for i in clotheslist.values():
        answer *= (i+1)
    return answer - 1
