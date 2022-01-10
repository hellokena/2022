from collections import deque

def dfs(v):
    print(v, end = ' ')
    visited[v] = 1 # 정점 방문처리
    for i in sorted(graph[v]): # 현재 방문한 노드와 연결된 노드 중에서
        if visited[i] == 0: # 아직 방문하지 않은 노드가 있다면
            dfs(i)

def solution(n,m,v):
    dfs(v)
    print()
    # bfs
    visited = [0]*(n+1) # visited 초기화
    queue = deque() # 큐 선언
    queue.append(v) # 첫 정점 삽입
    visited[v] = 1 # 첫 정점 방문처리
    print(v, end=' ')
    while queue:
        n = queue.popleft()
        for i in sorted(graph[n]):
            if visited[i] == 0: # 아직 방문하지 않았다면
                print(i, end = ' ')
                visited[i] = 1 # 방문처리
                queue.append(i)

# n:노드, m:간선, v:시작점
n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
#graph = [[]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

solution(n,m,v)

# --------------------------------------

from collections import deque

def dfs(v):
    print(v, end=' ')
    visited[v] = 1  # 정점 방문처리
    for i in sorted(graph[v]):  # 현재 방문한 노드와 연결된 노드 중에서
        if visited[i] == 0:  # 아직 방문하지 않은 노드가 있다면
            dfs(i)

def bfs(v):
    queue = deque()  # 큐 선언
    queue.append(v)  # 첫 정점 삽입
    visited[v] = 1  # 첫 정점 방문처리
    print(v, end=' ')
    while queue:
        n = queue.popleft()
        for i in sorted(graph[n]):
            if visited[i] == 0:  # 아직 방문하지 않았다면
                print(i, end=' ')
                visited[i] = 1  # 방문처리
                queue.append(i)

def solution(n, m, v):
    global visited ##
    dfs(v)
    print()
    visited = [0] * (n+1)  # visited 초기화
    bfs(v)

# n:노드, m:간선, v:시작점
n, m, v = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

solution(n, m, v)
