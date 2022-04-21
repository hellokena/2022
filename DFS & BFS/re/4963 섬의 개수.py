from collections import deque
def bfs(hidx,widx):
    queue = deque()
    queue.append((hidx,widx))
    graph[hidx][widx] = 0
    while queue:
        nowh, noww = queue.popleft()
        dh = [-1, -1, -1, 0, 1, 1, 1, 0]
        dw = [-1, 0, 1, 1, 1, 0, -1, -1]
        for i in range(8):
            nexth = nowh + dh[i]
            nextw = noww + dw[i]
            if 0<=nexth<h and 0<=nextw<w and graph[nexth][nextw] == 1:
                queue.append((nexth,nextw))
                graph[nexth][nextw] = 0

def solution(w,h,graph):
    answer = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i,j)
                answer += 1
    print(answer)

while True:
    w, h = map(int, input().split())
    if w==0 and h==0: break
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    solution(w,h,graph)
