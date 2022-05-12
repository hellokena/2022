def solution(n,t,temp):
    stime = [0]
    score = [0]
    for time,s in temp:
        stime.append(time)
        score.append(s)
    dp = [[0]*(t+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, t+1):
            if stime[i]<=j:
                dp[i][j] = max(dp[i-1][j-stime[i]]+score[i],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][t])

n,t = map(int, input().split())
temp = []
for _ in range(n):
    temp.append(list(map(int, input().split())))
solution(n,t,temp)
