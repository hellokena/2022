from collections import deque
def solution(n,house,conv,fest):
    visited = [0 for _ in range(n)] # 편의점 갯수 만큼
    queue = deque()
    queue.append((house[0],house[1])) # 출발점
    while queue:
        nowx, nowy = queue.popleft()
        if abs(nowx-fest[0]) + abs(nowy-fest[1]) <= 1000: # 거리가 50*20이면
            print("happy")
            return
        for i in range(n): #편의점 갯수
            if not visited[i]: # 아직 방문하지 않은 편의점
                if abs(nowx-conv[i][0]) + abs(nowy-conv[i][1]) <= 1000:
                    queue.append((conv[i][0], conv[i][1]))
                    visited[i] = 1
    print("sad")

t = int(input())
for _ in range(t):
    n = int(input())
    house = list(map(int, input().split()))
    conv = []
    for _ in range(n):
        conv.append(list(map(int, input().split())))
    fest = list(map(int, input().split()))
    solution(n,house,conv,fest)
