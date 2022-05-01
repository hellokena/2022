from collections import deque
def bfs(hidx,widx,graph):
    queue = deque()
    for i in range(hidx):
        for j in range(widx):
            if graph[i][j] == 1:
                queue.append((i,j)) # 전체 아기 상어 위치 append

    while queue:
        nowh, noww = queue.popleft()
        dh = [-1,-1,-1,0,1,1,1,0]
        dw = [-1,0,1,1,1,0,-1,-1]
        for d in range(8):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<hidx and 0<=nextw<widx and graph[nexth][nextw] == 0:
                graph[nexth][nextw] = graph[nowh][noww] + 1
                queue.append((nexth,nextw))
    return max(map(max, graph))-1

def solution(n,m,graph):
    print(bfs(n,m,graph))

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
solution(n,m,graph)
