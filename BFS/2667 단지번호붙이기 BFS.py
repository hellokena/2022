#bfs
from collections import deque

def solution(n):
    temp = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1: # 집이 있는 곳
                answer = 0
                queue = deque()
                queue.append((i,j))
                graph[i][j] = 0 # 방문처리
                while queue:
                    nowh, noww = queue.popleft()
                    answer += 1
                    # 상하좌우 방향벡터
                    dh = [-1, 1, 0, 0]
                    dw = [0, 0, -1, 1]
                    for x in range(4):
                        nexth = nowh + dh[x]
                        nextw = noww + dw[x]
                        if 0<=nexth<n and 0<=nextw<n and graph[nexth][nextw] == 1:
                            graph[nexth][nextw] = 0
                            queue.append((nexth, nextw))
                temp.append(answer)

    print(len(temp))
    for k in sorted(temp):
        print(k)

n = int(input()) # 지도 크기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
solution(n)

# ---------------------------------------------------------

#bfs
from collections import deque

def bfs(i,j):
    answer = 0
    queue = deque()
    queue.append((i, j))
    graph[i][j] = 0  # 방문처리
    while queue:
        nowh, noww = queue.popleft()
        answer += 1
        # 상하좌우 방향벡터
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for x in range(4):
            nexth = nowh + dh[x]
            nextw = noww + dw[x]
            if 0 <= nexth < n and 0 <= nextw < n and graph[nexth][nextw] == 1:
                graph[nexth][nextw] = 0
                queue.append((nexth, nextw))
    return answer

def solution(n):
    temp = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1: # 집이 있는 곳
                temp.append(bfs(i,j))

    print(len(temp))
    for k in sorted(temp):
        print(k)

n = int(input()) # 지도 크기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
solution(n)
