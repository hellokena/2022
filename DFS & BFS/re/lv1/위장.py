from collections import defaultdict
def solution(clothes):
    answer = 1
    clothes_list = defaultdict(int)
    for n,t in clothes:
        clothes_list[t] += 1
    for i in clothes_list.values():
        answer *= (i+1) # 안 입는 경우도 ++
    return answer - 1 # 다 벗는 경우
