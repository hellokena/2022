# 그리디 # 동전 0
# 주의 : 각각의 동전을 매우많이 가지고 있다

def solution(n,k,coins):
    answer = 0
    coins.sort(reverse=True) # 큰수부터 해야 동전 갯수의 최댓값
    for c in coins:
        answer += k // c
        k %= c
    print(answer)

n,k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
solution(n,k,coins)
