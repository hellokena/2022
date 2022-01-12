#dfs
import sys
sys.setrecursionlimit(10**5)

def dfs(v, graph, visited):
    visited[v] = 1 # 방문 처리
    for i in graph[v]:
        if visited[i] == 0: # 아직 방문을 하지 않음
            dfs(i, graph,visited)

def solution(n,m,graph):
    answer = 0
    visited = [0]*(n+1)
    for i in range(1, n+1):
        if visited[i] == 0: # 아직 방문하지 않은 노드
            dfs(i, graph, visited)
            answer += 1
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
