from collections import deque

def bfs(l,startx,starty,goalx,goaly):
    visited = [[0]*l for _ in range(l)]
    queue = deque()
    queue.append((startx,starty))
    visited[startx][starty] = 1
    while queue:
        nowx, nowy = queue.popleft()
        if nowx == goalx and nowy == goaly:
            return visited[nowx][nowy]-1
        dx = [1, 2, 2, 1, -1, -2, -2, -1]
        dy = [2, 1, -1, -2, -2, -1, 1, 2]
        for i in range(8):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            if 0<=nextx<l and 0<=nexty<l and visited[nextx][nexty] == 0:
                queue.append((nextx,nexty))
                visited[nextx][nexty] = visited[nowx][nowy] + 1

def solution(l,startx,starty,goalx,goaly):
    print(bfs(l,startx,starty,goalx,goaly))

t = int(input())
for _ in range(t):
    l = int(input())
    startx, starty = map(int, input().split())
    goalx, goaly = map(int, input().split())
    solution(l,startx,starty,goalx,goaly)
