from collections import deque
def bfs(hidx,widx,graph):
    cnt = 0
    graph[hidx][widx] = 0
    queue = deque()
    queue.append((hidx,widx))
    while queue:
        nowh,noww = queue.popleft()
        cnt += 1
        dh = [-1, 1, 0, 0]
        dw = [0, 0, 1, -1]
        for i in range(4):
            nexth = nowh + dh[i]
            nextw = noww + dw[i]
            if 1<=nexth<=n and 1<=nextw<=m and graph[nexth][nextw] == 1:
                queue.append((nexth,nextw))
                graph[nexth][nextw] = 0
    return cnt

def solution(n,m,k,temp):
    answer = []
    graph = [[0]*(m+1) for _ in range(n+1)]
    for x,y in temp:
        graph[x][y] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if graph[i][j] == 1:
                answer.append(bfs(i,j,graph))

    print(max(answer))
    return max(answer)

n,m,k = map(int, input().split())
temp = []
for _ in range(k):
    temp.append(list(map(int, input().split())))
solution(n,m,k,temp)
