from collections import deque

def bfs(hidx,widx):
    cnt = 0
    queue = deque()
    queue.append((hidx,widx))
    graph[hidx][widx] = 0
    while queue:
        nowh, noww = queue.popleft()
        cnt += 1
        # 상하좌우 방향벡터
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for i in range(4):
            nexth = nowh + dh[i]
            nextw = noww + dw[i]
            if 0<=nexth<n and 0<=nextw<n and graph[nexth][nextw] == 1:
                queue.append((nexth,nextw))
                graph[nexth][nextw] = 0
    return cnt

def solution(n,graph):
    temp = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1: # 집이 있는 곳
                temp.append(bfs(i,j))
    print(len(temp))
    for i in sorted(temp):
        print(i)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
solution(n,graph)
