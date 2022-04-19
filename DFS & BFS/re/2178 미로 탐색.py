from collections import deque
def bfs(hidx,widx):
    queue = deque()
    queue.append((hidx,widx))
    while queue:
        nowh, noww = queue.popleft()
        # 상하좌우 방향벡터
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for i in range(4):
            nexth = nowh + dh[i]
            nextw = noww + dw[i]
            if 0<=nexth<n and 0<=nextw<m and graph[nexth][nextw] == 1:
                queue.append((nexth,nextw))
                graph[nexth][nextw] = graph[nowh][noww] + 1
    return graph[-1][-1]

def solution(n,m,graph):
    print(bfs(0,0))

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
solution(n,m,graph)
