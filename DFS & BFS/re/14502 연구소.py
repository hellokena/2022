from collections import deque
from itertools import combinations
import copy

def virus(graph):
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i,j))
                visited[i][j] = 1
    while queue:
        nowh, noww = queue.popleft()
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for d in range(4):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<n and 0<=nextw<m:
                if graph[nexth][nextw] == 0 and visited[nexth][nextw] == 0:
                    graph[nexth][nextw] = 2 # 바이러스야 퍼져라~
                    queue.append((nexth,nextw))
                    visited[nexth][nextw] = 1

def bfs(graph): # 안전공간 찾기
    virus(graph) # 바이러스야 퍼져라~
    safezone = 0
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                queue.append((i,j))
                visited[i][j] = 1
    while queue:
        nowh, noww = queue.popleft()
        safezone += 1
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for d in range(4):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<n and 0<=nextw<m:
                if graph[nexth][nextw] == 0 and visited[nexth][nextw] == 0:
                    queue.append((nexth,nextw))
                    visited[nexth][nextw] = 1
    return safezone

def solution(n,m,graph):
    origin = copy.deepcopy(graph)
    answer = 0
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                queue.append((i,j)) # 벽을 세울 수 있는 공간
    temp = list(combinations(queue,3))
    for first, second, third in temp:
        graph[first[0]][first[1]] = 1 # 벽세우기
        graph[second[0]][second[1]] = 1
        graph[third[0]][third[1]] = 1
        answer = max(bfs(graph), answer)
        graph = copy.deepcopy(origin)
    print(answer)

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
solution(n,m,graph)
