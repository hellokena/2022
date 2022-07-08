from collections import deque
def bfs(hidx,widx,visited):
    sheep, wolf = 0,0
    queue = deque()
    queue.append((hidx,widx))
    visited[hidx][widx] = 1
    if graph[hidx][widx] == 'o': sheep += 1
    elif graph[hidx][widx] == 'v': wolf += 1
    while queue:
        nowh,noww = queue.popleft()
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for d in range(4):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<r and 0<=nextw<c and visited[nexth][nextw] == 0 and graph[nexth][nextw] != '#':
                if graph[nexth][nextw] == 'o': sheep += 1
                elif graph[nexth][nextw] == 'v': wolf += 1
                visited[nexth][nextw] = 1
                queue.append((nexth,nextw))
    return sheep, wolf

def solution(r,c,graph):
    sheep, wolf = 0,0
    visited = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] != '#' and visited[i][j] == 0:
                now_sheep, now_wolf = bfs(i,j,visited)
                if now_sheep > now_wolf: sheep += now_sheep
                else: wolf += now_wolf
    print(sheep, wolf)

r,c = map(int, input().split()) # 행,열
graph = []
for _ in range(r):
    graph.append(list(input()))
solution(r,c,graph)
