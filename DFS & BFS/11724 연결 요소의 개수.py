#bfs
# 시간초과 -> 이유 : input 때문에...^^
from collections import deque
def solution(n,m,graph):
    answer = 0
    visited = [0]*(n+1)
    queue = deque()
    for i in range(1, n+1): # 범위가 1부터 시작해야 함
        if visited[i] == 0: # 방문하지 않은 노드
            answer += 1
            queue.append(i)
            visited[i] = 1
            while queue:
                pop = queue.popleft()
                for j in graph[pop]:
                    if visited[j] == 0: # 방문하지 않은 노드
                        queue.append(j)
                        visited[j] = 1
    print(answer)

n,m = map(int, input().split()) # 노드, 간선
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
solution(n,m,graph)

# -------------------------------------------------------

#bfs
from collections import deque
import sys

def solution(n,m,graph):
    answer = 0
    visited = [0]*(n+1)
    queue = deque()
    for i in range(1, n+1): # 범위가 1부터 시작해야 함
        if visited[i] == 0: # 방문하지 않은 노드
            answer += 1
            queue.append(i)
            visited[i] = 1
            while queue:
                pop = queue.popleft()
                for j in graph[pop]:
                    if visited[j] == 0: # 방문하지 않은 노드
                        queue.append(j)
                        visited[j] = 1
    print(answer)

#n,m = map(int, input().split()) # 노드, 간선
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, sys.stdin.readline().rstrip().split())
    #u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
solution(n,m,graph)

# ------------------------------------------------------------

#bfs
from collections import deque
import sys
# 덩어리 세기
def bfs(v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        pop = queue.popleft()
        for i in graph[pop]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

def solution(n,m,graph):
    answer = 0
    visited = [0] * (n+1)
    for i in range(1, n+1):
        if visited[i] == 0: # 방문하지 않은 노드
            bfs(i, visited)
            answer += 1
    print(answer)

#n,m = map(int, input().split()) # 노드, 간선
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    #u,v = map(int, input().split())
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
solution(n,m,graph)
