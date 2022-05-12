def solution(n):
    if n<=2:
        print(n%15746)
        return
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2])%15746 # 메모리초과 해결
    print(dp[n])
n = int(input())
solution(n)
