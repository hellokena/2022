# 2178 미로 탐색 bfs 버전
# 최단거리는 bfs
from collections import deque

def solution(n,m):
    # 상하좌우 방향벡터
    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]
    queue = deque()
    queue.append((0,0)) # 시작점 추가
    while queue:
        nowh, noww = queue.popleft()
        for i in range(4):
            nh = nowh + dh[i]
            nw = noww + dw[i]
            if 0<=nh<n and 0<=nw<m and graph[nh][nw] == 1:
                graph[nh][nw] = graph[nowh][noww] + 1
                queue.append((nh,nw))
    print(graph[-1][-1])

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
solution(n,m)
