def solution(n,houses):
    for i in range(1,n):
        # 1번째 집은 상관 없으므로 자기의 빨,빠,초 값을 넘어줌
        # 2번째 집부터 연속된 색상 불가능
        # 앞의 집의 최솟값을 구해 계산
        houses[i][0] = houses[i][0] + min(houses[i-1][1], houses[i-1][2])
        houses[i][1] = houses[i][1] + min(houses[i-1][0], houses[i-1][2])
        houses[i][2] = houses[i][2] + min(houses[i-1][0], houses[i-1][1])
    print(min(houses[-1]))
    
n = int(input())
houses = []
for _ in range(n):
    houses.append(list(map(int, input().split())))
solution(n,houses)
