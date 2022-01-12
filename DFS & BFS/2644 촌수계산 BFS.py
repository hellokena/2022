# bfs
from collections import deque

def bfs(v,graph,visited):
    # 관계를 나타내는 변수를 선언할 필요 없음
    result = [0]*(n+1) ##
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        pv = queue.popleft()
        if pv == n2: ##
            print(result[pv])
            break
        for i in graph[pv]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                result[i] = result[pv] + 1 ##
    else: print(-1)

def solution(n,n1,n2,r,graph):
    visited = [0]*(n+1)
    bfs(n1,graph,visited)

n = int(input()) # 사람수
n1,n2 = map(int, input().split()) # 찾아야 하는 두 사람
r = int(input()) # 관계수
graph = [[] for _ in range(n+1)]
for _ in range(r):
    p,c = map(int, input().split())
    graph[c].append(p)
    graph[p].append(c)
solution(n,n1,n2,r,graph)
