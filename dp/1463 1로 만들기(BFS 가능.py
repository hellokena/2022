def solution(n):
    dp = [0]*(10**6+1) # dp[0] = 0
    for i in range(2,n+1):
        # 1 빼기
        dp[i] = dp[i-1] + 1
        if i%3 == 0: # 3 나누기
            dp[i] = min(dp[i], dp[i//3]+1)
        if i%2 == 0: # 2 나누기
            dp[i] = min(dp[i], dp[i//2]+1)
    print(dp[n])

n = int(input())
solution(n)
