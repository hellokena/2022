from collections import deque
def bfs(hidx,widx,rain,visited):
    queue = deque()
    queue.append((hidx,widx))
    visited[hidx][widx] = 1 # 방문 처리
    while queue:
        nowh,noww = queue.popleft()
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for d in range(4):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<n and 0<=nextw<n and graph[nexth][nextw] > rain and visited[nexth][nextw] == 0:
                queue.append((nexth,nextw))
                visited[nexth][nextw] = 1

def solution(n,graph):
    answer = []
    temp = max(map(max,graph))
    for rain in range(temp):
        cnt = 0
        visited = [[0]*n for _ in range(n)] # 각 레벨마다 초기화
        for i in range(n):
            for j in range(n):
                if graph[i][j] > rain and visited[i][j] == 0:
                    bfs(i,j,rain,visited)
                    cnt += 1
        answer.append(cnt)
    print(max(answer))

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
solution(n,graph)
