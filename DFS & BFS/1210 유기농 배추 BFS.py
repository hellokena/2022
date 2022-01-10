#bfs
from collections import deque

def bfs(i,j):
    queue = deque()
    queue.append((i, j))
    graph[i][j] = 0  # 방문처리
    while queue:
        poph, popw = queue.popleft()
        # 상하좌우 방향벡터
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for r in range(4):
            nh = poph + dh[r]
            nw = popw + dw[r]
            if 0<=nh<m and 0<=nw<n and graph[nh][nw] == 1:
                graph[nh][nw] = 0 # 방문처리
                queue.append((nh,nw))

def solution(m,n,k,graph): # 필요한 지렁이의 수
    answer = 0
    for i in range(m): # 가로
        for j in range(n):# 세로
            if graph[i][j] == 1: # 배추가 있는 곳
                bfs(i,j)
                answer += 1
    print(answer)

t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split()) # 가로, 세로, 배추 수
    graph = [[0]*n for _ in range(m)]
    for _ in range(k):
        x,y = map(int, input().split())
        graph[x][y] = 1

    solution(m,n,k,graph)
    
    # --------------------------------------------------
    
    #bfs
from collections import deque

def solution(m,n,k,graph): # 필요한 지렁이의 수
    answer = 0
    for i in range(m): # 가로
        for j in range(n):# 세로
            if graph[i][j] == 1: # 배추가 있는 곳
                answer += 1 # 지렁이수를 하나 늘림
                queue = deque()
                queue.append((i, j))
                graph[i][j] = 0  # 방문처리
                while queue:
                    poph, popw = queue.popleft()
                    # 상하좌우 방향벡터
                    dh = [-1, 1, 0, 0]
                    dw = [0, 0, -1, 1]
                    for r in range(4):
                        nh = poph + dh[r]
                        nw = popw + dw[r]
                        if 0 <= nh < m and 0 <= nw < n and graph[nh][nw] == 1:
                            graph[nh][nw] = 0  # 방문처리
                            queue.append((nh, nw))
    print(answer)

t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split()) # 가로, 세로, 배추 수
    graph = [[0]*n for _ in range(m)]
    for _ in range(k):
        x,y = map(int, input().split())
        graph[x][y] = 1

    solution(m,n,k,graph)
