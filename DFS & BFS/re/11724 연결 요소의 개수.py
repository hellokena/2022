from collections import deque
import sys
input = sys.stdin.readline

def bfs(nidx, visited):
    queue = deque()
    queue.append(nidx)
    visited[nidx] = 1 # 방문처리
    while queue:
        nown = queue.popleft()
        for nextn in graph[nown]:
            if visited[nextn] == 0:
                queue.append(nextn)
                visited[nextn] = 1

def solution(n,m,graph):
    visited = [0]*(n+1)
    answer = 0
    for i in range(1,n+1):
        if visited[i] == 0:
                bfs(i, visited)
                answer += 1
    print(answer)

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
solution(n,m,graph)
