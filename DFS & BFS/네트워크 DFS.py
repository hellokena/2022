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

# ---------------------------

# dfs
def dfs(n, computers, visited, v):
    visited[v] = 1 # 방문처리
    for i in range(n):
        # 같은 컴퓨터 제외, 연결컴퓨터(1), 방문안했을 때
        if i != v and computers[v][i] == 1 and visited[i] == 0:
            dfs(n, computers, visited, i)
                
def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if visited[i] == 0:
            dfs(n, computers, visited, i)
            answer += 1
    return answer
