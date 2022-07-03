from collections import deque
import sys
input = sys.stdin.readline
# 빙하 갯수 확인 -> 빙하 녹이기
# 빙하 갯수와 주변 바다 갯수 세는걸 동시에
def bfs(n,m,hidx,widx,graph,visited,sea): # n이 세로m이 가로 # 빙산 갯수 세기
    queue = deque()
    queue.append((hidx,widx))
    visited[hidx][widx] = 1 # 방문처리
    while queue:
        nowh, noww = queue.popleft()
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for d in range(4):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<n and 0<=nextw<m and visited[nexth][nextw] == 0:
                if graph[nexth][nextw] > 0 and visited:
                    queue.append((nexth,nextw))
                    visited[nexth][nextw] = 1 # 방문처리
                elif graph[nexth][nextw] == 0:
                    sea[nowh][noww] += 1 # 빙하갯수세기

def solution(n,m,graph):
    answer = 0 # 빙하가 쪼개지는데 걸리는 시간
    while True:
        visited = [[0]*m for _ in range(n)] # 방문
        sea = [[0]*m for _ in range(n)] # 주변 바다 갯수
        cnt = 0 # 빙하 갯수
        for i in range(n):
            for j in range(m):
                if graph[i][j] > 0 and visited[i][j] == 0:
                    bfs(n,m,i,j,graph,visited,sea)
                    cnt += 1

        # 마지막에 빙산 한꺼번에 녹여줌
        # 중간에 녹이면 방금 녹인 빙산을 바다로 인식 가능하기 때문
        for i in range(n):
            for j in range(m):
                graph[i][j] -= sea[i][j]
                # 만약 깎인수가 음수면 0으로 세팅
                if graph[i][j] < 0: graph[i][j] = 0
                
        if cnt>=2:
            print(answer)
            return
        elif cnt == 0:
            print(0)
            return
        else: answer += 1 # 다시 한번 돌리기

n,m = map(int, input().split()) # 행, 열
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
solution(n,m,graph)



