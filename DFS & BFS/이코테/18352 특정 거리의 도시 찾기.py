import sys
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

n,m,k,x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
solution(n,m,k,x,graph)

# -------------------------------------

import sys
from collections import deque

def solution(n,m,k,x,graph):
    answer = []
    visited = [0]*(n+1)
    queue = deque()
    queue.append((x,0))
    visited[x] = 1 # 방문처리

    while queue:
        now, d = queue.popleft()
        if d == k:
           answer.append(now)
        for next in graph[now]:
            if visited[next] == 0:
                queue.append((next, d+1))
                visited[next] = 1 # 방문처리

    if len(answer) == 0: print(-1)
    else:
        answer.sort()
        for a in answer:
            print(a)

n,m,k,x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
solution(n,m,k,x,graph)
