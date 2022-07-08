from collections import deque
import sys
input = sys.stdin.readline
def bfs(hidx,widx):
    max_num = 0
    queue = deque()
    queue.append((hidx,widx))
    visited = [[0]*w for _ in range(h)] # 매번 초기화
    visited[hidx][widx] = 1
    while queue:
        nowh, noww = queue.popleft()
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for d in range(4):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<h and 0<=nextw<w:
                if graph[nexth][nextw] == 'L' and visited[nexth][nextw] == 0:
                    visited[nexth][nextw] = visited[nowh][noww] + 1
                    queue.append((nexth,nextw))
                    max_num = max(max_num,visited[nexth][nextw])
    return max_num-1

def solution(h,w,graph):
    answer = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 'L': # 육지
                answer = max(answer,bfs(i,j))
    print(answer)
h,w = map(int, input().split())
graph = []
for _ in range(h):
    graph.append(list(input()))
solution(h,w,graph)
