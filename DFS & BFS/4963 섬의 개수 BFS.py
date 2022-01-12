#bfs
#1:땅, 0:바다
#덩어리 갯수
from collections import deque

def bfs(hidx,widx,graph):
    queue = deque()
    queue.append((hidx,widx))
    graph[hidx][widx] = 0
    while queue:
        vh, vw = queue.popleft()
        # 북,북동,동,동남,남,남서,서,서북 방향벡터
        dh = [-1, -1, 0, 1, 1, 1, 0, -1]
        dw = [0, 1, 1, 1, 0, -1, -1, -1]
        for r in range(8):
            nh = vh + dh[r]
            nw = vw + dw[r]
            if 0<=nh<h and 0<=nw<w and graph[nh][nw] == 1: # 땅
                queue.append((nh,nw))
                graph[nh][nw] = 0

def solution(w,h,graph):
    answer = 0
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1: # 땅
                bfs(i,j,graph)
                answer += 1
    print(answer)

while True:
    w,h = map(int, input().split())
    if w==0 and h==0: break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    solution(w,h,graph)
