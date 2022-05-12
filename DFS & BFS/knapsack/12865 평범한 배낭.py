def solution(n,k,temp): # 물품수, 무게
    w = [0]
    v = [0]
    for weight,value in temp:
        w.append(weight)
        v.append(value)
    dp = [[0]*(k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if w[i]<=j: # 현재 무게 기준
                dp[i][j] = max(dp[i-1][j-w[i]]+v[i], dp[i-1][j])
            elif w[i]>j:
                dp[i][j] = dp[i-1][j]
    print(dp[n][k])

n,k = map(int, input().split())
temp = []
for _ in range(n):
    temp.append(list(map(int,input().split())))
solution(n,k,temp)
