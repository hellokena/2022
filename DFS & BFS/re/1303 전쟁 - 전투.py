from collections import deque

def bfs(hidx,widx,visited,team):
    answer = 0
    queue = deque()
    queue.append((hidx,widx))
    visited[hidx][widx] = 1
    while queue:
        nowh, noww = queue.popleft()
        answer += 1
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for i in range(4):
            nexth = nowh + dh[i]
            nextw = noww + dw[i]
            if 0<=nexth<m and 0<=nextw<n and visited[nexth][nextw] == 0 and graph[nexth][nextw] == team:
                queue.append((nexth,nextw))
                visited[nexth][nextw] = 1
    return answer**2

def solution(n,m,graph):
    blue = 0
    white = 0
    visited = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 'B' and visited[i][j] == 0:
                blue += bfs(i,j,visited,'B')
            elif graph[i][j] == 'W' and visited[i][j] == 0:
                white += bfs(i,j,visited,'W')
    print(white, blue)

n,m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(input()))
solution(n,m,graph)
