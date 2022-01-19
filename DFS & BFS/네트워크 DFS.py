# dfs
def dfs(n, computers, graph, visited, v):
    visited[v] = 1 # 방문처리
    for i in graph[v]:
        if visited[i] == 0:
            dfs(n, computers, graph, visited, i)
                
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
            dfs(n, computers, graph, visited, i)
            answer += 1
    return answer
