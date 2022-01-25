# 나이트의 이동
# BFS
from collections import deque
def solution(n, nowx, nowy, nextx, nexty):
    visited = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append((nowx, nowy, 0))
    visited[nowx][nowy] = 1 # 방문처리
    while queue:
        popx, popy, cnt = queue.popleft()
        # 처음에 탐색 완료시가 최소
        if popx == nextx and popy == nexty: return cnt
        # 방향벡터
        dx = [1, 2, 2, 1, -1, -2, -2, -1]
        dy = [2, 1, -1, -2, -2, -1, 1, 2]
        for i in range(8):
            nx = popx + dx[i]
            ny = popy + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                queue.append((nx,ny,cnt+1))
                visited[nx][ny] = 1

t = int(input())
for _ in range(t):
    n = int(input()) # 체스판 nxn
    nowx, nowy = map(int, input().split())
    nextx, nexty = map(int, input().split())
    answer = solution(n, nowx, nowy, nextx, nexty)
    print(answer)
