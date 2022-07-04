from collections import deque
def bfs(hidx,widx,n,graph,visited,color):
    queue = deque()
    queue.append((hidx,widx))
    visited[hidx][widx] = 1
    while queue:
        nowh, noww = queue.popleft()
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for d in range(4):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<n and 0<=nextw<n:
                if visited[nexth][nextw] == 0 and graph[nexth][nextw] == color:
                    queue.append((nexth,nextw))
                    visited[nexth][nextw] = 1

def solution(n,graph):
    visited = [[0] * n for _ in range(n)]
    normal = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i,j,n,graph,visited,graph[i][j])
                normal += 1
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'R':
                graph[i][j] = 'G'
    visited = [[0] * n for _ in range(n)]
    green = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i,j,n,graph,visited,graph[i][j])
                green += 1
    print(normal, green)

n = int(input())
graph = []
for _ in range(n):
    graph.append((list(input())))
solution(n,graph)
