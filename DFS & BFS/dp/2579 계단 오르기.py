def solution(n,stairs):
    stairs.insert(0,0) # 0에다가 0을 넣어줌
    dp = [0]*(n+1)
    if n == 1: print(stairs[1])
    elif n == 2: print(stairs[1] + stairs[2])
    else:
        dp[1] = stairs[1]
        dp[2] = stairs[1] + stairs[2]
        for i in range(3,n+1):
            # 연속 3계단을 밟을 수 없음 활용
            # 현재 계단 점수 + 2칸 밑의 계산된 점수
            # 현재 계단 점수 + 1칸 밑 한 계단의 점수 + 3칸 밑의 점수
            dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])
        print(dp[n])

n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))
solution(n,stairs)
