from collections import defaultdict

def solution(n,clothes):
    clotheslist = defaultdict(int) # value 타입
    for c in clothes:
        name, type = c.split()
        clotheslist[type] += 1
    answer = 1
    for i in clotheslist.values():
        answer *= (i+1)
    print(answer-1)


tc = int(input()) # 테스트 케이스
for _ in range(tc):
    n = int(input())
    clothes = []
    for _ in range(n):
        clothes.append(input())
    solution(n,clothes)



