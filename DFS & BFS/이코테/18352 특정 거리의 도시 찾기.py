from collections import deque

def solution(n,m,k,x,graph):
    distance = [0]*(n+1)
    visited = [0]*(n+1)
    queue = deque()
    queue.append(x)
    visited[x] = 1 # 방문처리

    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next] == 0:
                queue.append(next)
                visited[next] = 1 # 방문처리
                distance[next] = distance[now] + 1

    check = distance.count(k)
    if check:
        for i in range(1, n+1):
            if distance[i] == k:
                print(i)
    else: print(-1)

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
solution(n,m,k,x,graph)
