# dp, knapsack
def solution(n,k,items):
    weight = [0]
    value = [0]
    for w,v in items:
        weight.append(w)
        value.append(v)

    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(1,n+1): # 아이템수
        for j in range(1,k+1): # 가방 최대 무게
            # 현재 넣으려는 아이템 무게 보다 가방 최대 무게가 더 크면
            if j >= weight[i]: # i는 idx는 0부터 시작
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
            else: dp[i][j] = dp[i-1][j]
    print(dp[n][k])

n,k = map(int, input().split())
items = []
for _ in range(n):
    items.append(list(map(int, input().split())))
solution(n,k,items)
