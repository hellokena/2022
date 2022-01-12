#dfs
#1:땅, 0:바다
#덩어리 갯수

import sys
sys.setrecursionlimit(10**5)

def dfs(hidx,widx,graph):
    graph[hidx][widx] = 0
    # 북,북동,동,동남,남,남서,서,서북 방향벡터
    dh = [-1, -1, 0, 1, 1, 1, 0, -1]
    dw = [0, 1, 1, 1, 0, -1, -1, -1]
    for r in range(8):
        nh = hidx + dh[r]
        nw = widx + dw[r]
        if 0<=nh<h and 0<=nw<w and graph[nh][nw] == 1: # 땅
            dfs(nh,nw,graph)

def solution(w,h,graph):
    answer = 0
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1: # 땅
                dfs(i,j,graph)
                answer += 1
    print(answer)

while True:
    w,h = map(int, input().split())
    if w==0 and h==0: break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    solution(w,h,graph)
