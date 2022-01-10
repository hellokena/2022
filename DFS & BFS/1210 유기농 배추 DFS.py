# dfs
import sys
sys.setrecursionlimit(10**5)

def dfs(i,j):
    graph[i][j] = 0 # 방문 처리
    # 상하좌우 방향벡터
    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]
    for r in range(4):
        nh = i + dh[r]
        nw = j + dw[r]
        if 0<=nh<m and 0<=nw<n and graph[nh][nw] == 1:
            dfs(nh,nw)

def solution(m,n,k,graph):
    answer = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                dfs(i,j)
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
