def solution(n,m,coins):
    dp = [0]*(m+1)
    dp[0] = 1 # 0을 만드는 횟수는 1
    for coin in coins:
        for i in range(m+1):
            if i>=coin:
                dp[i] += dp[i-coin]
    print(dp[m])

t = int(input())
for _ in range(t):
    n = int(input()) # 동전 종류
    coins = list(map(int, input().split()))
    m = int(input()) #만들어야 하는 금액
    solution(n,m,coins)
