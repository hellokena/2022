from collections import deque
def bfs(h,w,n,m,graph):
    cnt = 0
    queue = deque()
    queue.append((h,w))
    graph[h][w] = 0 # 방문처리
    while queue:
        poph, popw = queue.popleft()
        cnt += 1
        # 상하좌우 방향벡터
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for r in range(4):
            nh = poph + dh[r]
            nw = popw + dw[r]
            if 0<nh<=n and 0<nw<=m and graph[nh][nw] == 1:
                queue.append((nh,nw))
                graph[nh][nw] = 0 # 방문처리
    return cnt

def solution(n,m,k,graph):
    result = []
    for i in range(1, n+1): # 1부터 시작해야 함
        for j in range(1, m+1):
            if graph[i][j] == 1:
                result.append(bfs(i,j,n,m,graph))
    print(max(result))

n,m,k = map(int, input().split())
graph =[[0]*(m+1) for _ in range(n+1)]
for _ in range(k):
    r,c = map(int, input().split())
    graph[r][c] = 1
solution(n,m,k,graph)
