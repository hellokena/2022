def solution(n,m,memory,cost): # 앱의 갯수, 필요한 메모리
    memory.insert(0,0)
    cost.insert(0,0)
    dp = [[0]*(sum(cost)+1) for _ in range(n+1)]
    result = sum(cost)
    for i in range(1,n+1):
        for j in range(1,sum(cost)+1):
            if cost[i]<=j:
                # i번째 앱까지 중 j 코스트로 얻을 수 있는 최대의 메모리
                dp[i][j] = max(dp[i-1][j-cost[i]]+memory[i], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
            if dp[i][j] >= m:
                result = min(result,j)
    print(result)

n,m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
solution(n,m,memory,cost)
