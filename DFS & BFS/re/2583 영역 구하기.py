# dfs # 0인 곳을 탐색
import sys
sys.setrecursionlimit(10**5)

def dfs(nowh,noww,m,n,graph):
    global in_cnt # 내부 갯수 세기
    in_cnt += 1
    graph[nowh][noww] = 1 # 방문 처리
    # 상하좌우 방향벡터
    dh = [-1, 0, 1, 0]
    dw = [0, 1, 0, -1]
    for i in range(4):
        nexth = nowh + dh[i]
        nextw = noww + dw[i]
        if 0<=nexth<m and 0<=nextw<n and graph[nexth][nextw] == 0:
            dfs(nexth,nextw,m,n,graph)
    #return in_cnt

def solution(m,n,k,graph):
    answer = []
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:
                global in_cnt # 초기화
                in_cnt = 0
                #answer.append(dfs(i,j,m,n,graph))
                dfs(i,j,m,n,graph)
                answer.append(in_cnt)
    print(len(answer))
    # print(' '.join(map(str,sorted(answer))))
    for i in sorted(answer):
        print(i, end=' ')

m,n,k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1
solution(m,n,k,graph)

# -----------------------------------------------

# bfs
# bfs는 재귀가 아니므로 global 필요 없음
from collections import deque

def bfs(nowh,noww,m,n,graph):
    # in_cnt = 0
    global in_cnt
    queue = deque()
    queue.append((nowh,noww))
    graph[nowh][noww] = 1 # 방문 처리
    while queue:
        nowh, noww = queue.popleft()
        in_cnt += 1
        # 상하좌우 방향벡터
        dh = [-1, 0, 1, 0]
        dw = [0, 1, 0, -1]
        for i in range(4):
            nexth = nowh + dh[i]
            nextw = noww + dw[i]
            if 0<=nexth<m and 0<=nextw<n and graph[nexth][nextw] == 0:
                queue.append((nexth,nextw))
                graph[nexth][nextw] = 1 # 방문 처리
    return in_cnt

def solution(m,n,k,graph):
    answer = []
    for i in range(m): # 세로
        for j in range(n): # 가로
            if graph[i][j] == 0: # 배추가 있는 위치
                global in_cnt
                in_cnt = 0
                bfs(i,j,m,n,graph)
                answer.append(in_cnt)
    print(len(answer))
    for a in sorted(answer):
        print(a, end =' ')

m,n,k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1
solution(m,n,k,graph)

# ---------------------------------------------

# bfs
# bfs는 재귀가 아니므로 global 필요 없음
from collections import deque

def bfs(nowh,noww,m,n,graph):
    in_cnt = 0
    queue = deque()
    queue.append((nowh,noww))
    graph[nowh][noww] = 1 # 방문 처리
    while queue:
        nowh, noww = queue.popleft()
        in_cnt += 1
        # 상하좌우 방향벡터
        dh = [-1, 0, 1, 0]
        dw = [0, 1, 0, -1]
        for i in range(4):
            nexth = nowh + dh[i]
            nextw = noww + dw[i]
            if 0<=nexth<m and 0<=nextw<n and graph[nexth][nextw] == 0:
                queue.append((nexth,nextw))
                graph[nexth][nextw] = 1 # 방문 처리
    return in_cnt

def solution(m,n,k,graph):
    answer = []
    for i in range(m): # 세로
        for j in range(n): # 가로
            if graph[i][j] == 0: # 배추가 있는 위치
                answer.append(bfs(i,j,m,n,graph))

    print(len(answer))
    for a in sorted(answer):
        print(a, end =' ')

m,n,k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1
solution(m,n,k,graph)
