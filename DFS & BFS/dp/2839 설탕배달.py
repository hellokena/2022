def solution(n):
    dp = [-1]*5001
    dp[3] = 1
    dp[5] = 1
    for i in range(6,n+1):
        if dp[i-5] != -1: # 5부터 뺌
            dp[i] = dp[i-5] + 1
        elif dp[i-3] != -1:
            dp[i] = dp[i-3] + 1
    print(dp[n])

n = int(input())
solution(n)
