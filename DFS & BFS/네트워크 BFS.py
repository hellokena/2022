# bfs
from collections import deque
def bfs(n, computers, graph, visited, v):
    queue = deque()
    queue.append(v)
    while queue:
        nv = queue.popleft()
        for i in graph[nv]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                
def solution(n, computers):
    answer = 0
    graph = [[]*n for _ in range(n)]
    visited = [0]*n
    for i in range(n):
        for j in range(n):
            if i==j: continue
            if computers[i][j] == 1:
                graph[i].append(j)
    for i in range(n):
        if visited[i] == 0:
            bfs(n, computers, graph, visited, i)
            answer += 1
    return answer
