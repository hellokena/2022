from collections import deque
def solution(n,m,graph):
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((0,0,0))
    visited[0][0][0] = 1 # 방문처리
    while queue:
        nowh,noww,wall = queue.popleft() # 부순횟수
        if nowh == n-1 and noww == m-1:
            print(visited[-1][-1][wall])
            return
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for d in range(4):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<n and 0<=nextw<m:
                # 그냥 이동 / 벽을 지금 부쉈든 말든 0이면 갈 수 있음
                # 갈 수 있는 길, 아직 도착하지 않음 -> 최단
                if graph[nexth][nextw] == 0 and visited[nexth][nextw][wall] == 0:
                    visited[nexth][nextw][wall] = visited[nowh][noww][wall] + 1
                    queue.append((nexth,nextw,wall))
                # 벽 부수고 이동
                elif graph[nexth][nextw] == 1 and wall == 0: # 아직 하나도 안 부순 경우
                    visited[nexth][nextw][1] = visited[nowh][noww][0] + 1
                    queue.append((nexth,nextw,1)) # 벽 부숨
    print(-1)
    return

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
solution(n,m,graph)
