# greedy
def solution(n,m,coins):
    answer = 0
    coins.sort(reverse=True) # 내림차순 정렬
    for c in coins:
        if m%c == 0:
            answer += m//c
            m = 0
    if not m: print(answer)
    else: print(-1)
n,m = map(int, input().split()) # 화폐 종류 갯수, 타겟 가격
coins = []
for _ in range(n):
    coins.append(int(input()))
solution(n,m,coins)
