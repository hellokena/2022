# dfs
import sys
sys.setrecursionlimit(10**5)

def dfs(nowh,noww):
    graph[nowh][noww] = 0 # 방문 처리
    # 상하좌우 방향벡터
    dh = [-1, 0, 1, 0]
    dw = [0, 1, 0, -1]
    for i in range(4):
        nexth = nowh + dh[i]
        nextw = noww + dw[i]
        if 0<=nexth<n and 0<=nextw<m and graph[nexth][nextw] == 1:
            dfs(nexth,nextw)

def solution(m,n,k,graph):
    answer = 0
    for i in range(n): # 세로
        for j in range(m): # 가로
            if graph[i][j] == 1: # 배추가 있는 위치
                dfs(i,j)
                answer += 1
    print(answer)

tc = int(input())
for _ in range(tc):
    # 가로, 세로, 배추 갯수
    m,n,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int, input().split())
        graph[y][x] = 1
    solution(m,n,k,graph)
    
# --------------------------------------------------------------------------

# bfs
from collections import deque

def bfs(nowh,noww):
    queue = deque()
    queue.append((nowh,noww))
    graph[nowh][noww] = 0 # 방문 처리
    while queue:
        nowh, noww = queue.popleft()
        # 상하좌우 방향벡터
        dh = [-1, 0, 1, 0]
        dw = [0, 1, 0, -1]
        for i in range(4):
            nexth = nowh + dh[i]
            nextw = noww + dw[i]
            if 0<=nexth<n and 0<=nextw<m and graph[nexth][nextw] == 1:
                queue.append((nexth,nextw))
                graph[nexth][nextw] = 0 # 방문 처리

def solution(m,n,k,graph):
    answer = 0
    for i in range(n): # 세로
        for j in range(m): # 가로
            if graph[i][j] == 1: # 배추가 있는 위치
                bfs(i,j)
                answer += 1
    print(answer)

tc = int(input())
for _ in range(tc):
    # 가로, 세로, 배추 갯수
    m,n,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int, input().split())
        graph[y][x] = 1
    solution(m,n,k,graph)
