from collections import deque
def bfs(hidx,widx,n,m,graph):
    cnt = 0
    queue = deque()
    queue.append((hidx,widx))
    graph[hidx][widx] = 0 # 방문 처리
    while queue:
        nowh, noww = queue.popleft()
        cnt += 1
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for d in range(4):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<n and 0<=nextw<m and graph[nexth][nextw] == 1:
                queue.append((nexth,nextw))
                graph[nexth][nextw] = 0
    return cnt

def solution(n,m,graph):
    answer = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                answer.append(bfs(i,j,n,m,graph))

    print(len(answer))
    if len(answer): print(max(answer))
    else: print(0)

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
solution(n,m,graph)
