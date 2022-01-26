from collections import deque
def wbfs(n,m,i,j,visited,team):
    cnt = 0
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    while queue:
        poph, popw = queue.popleft()
        cnt += 1
        # 상하좌우 방향벡터
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for r in range(4):
            nh = poph + dh[r]
            nw = popw + dw[r]
            if 0<=nh<m and 0<=nw<n and visited[nh][nw] == 0 and graph[nh][nw] == team:
                queue.append((nh,nw))
                visited[nh][nw] = 1
                # cnt += 1 # 여기서 해버리면 맨 첫원소는 안들어감
    return cnt**2

def solution(n,m,graph):
    white = 0
    blue = 0
    visited = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if visited[i][j]==0 and graph[i][j] == 'W':
                white += wbfs(n,m,i,j,visited,'W')
    visited = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if visited[i][j]==0 and graph[i][j] == 'B':
                blue += wbfs(n,m,i,j,visited,'B')
    print(white, blue)

n,m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(input()))
solution(n,m,graph)

