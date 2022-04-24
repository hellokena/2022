def solution(n):
    dp = [0]*10001
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(3,n+1):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[n]%10007)

n = int(input())
solution(n)
