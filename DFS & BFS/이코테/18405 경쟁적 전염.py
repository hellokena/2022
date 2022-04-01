# 경쟁적 전염
import sys
from collections import deque

def solution(n,k,graph,s,x,y):
    # visitied 필요 없음
    queue = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                queue.append((graph[i][j],i,j,0))
    queue.sort()
    queue = deque(queue)
    # 상하좌우 방향벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        level, nowx, nowy, time = queue.popleft()
        if time == s:
            break
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            if 0<=nextx<n and 0<=nexty<n and graph[nextx][nexty] == 0:
                graph[nextx][nexty] = level
                queue.append((level,nextx,nexty,time+1))
    print(graph[x-1][y-1])

n,k = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
s,x,y = map(int, sys.stdin.readline().split())
solution(n,k,graph,s,x,y)
