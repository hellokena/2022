from collections import deque
def solution(m,n,h,graph):
    answer = 0
    queue = deque()
    for k in range(h): # 박스수
        for i in range(n): # 세로
            for j in range(m): # 가로
                if graph[k][i][j] == 1:
                    queue.append((k,i,j))
                    # 익으면 방문처리
    while queue:
        nowz, nowy, nowx = queue.popleft()
        # 왼, 오른쪽, 앞 뒤
        dy = [ -1, 1, 0, 0, 0, 0]
        dx = [0, 0, -1, 1, 0, 0]
        dz = [0, 0, 0, 0, -1, 1]
        for d in range(6):
            nexty = nowy + dy[d]
            nextx = nowx + dx[d]
            nextz = nowz + dz[d]
            if 0<=nextz<h and 0<=nexty<n and 0<=nextx<m and graph[nextz][nexty][nextx] == 0:
                graph[nextz][nexty][nextx] = graph[nowz][nowy][nowx] + 1 # 익게 해버림
                queue.append((nextz,nexty,nextx))

    for k in range(h):  # 박스수
        for i in range(n):  # 세로
            for j in range(m):  # 가로
                if graph[k][i][j] == 0: # 이래도 안익은거
                    print(-1)
                    return
                answer = max(answer, graph[k][i][j])
    print(answer-1) # 1을 빼주는 이유 : -1, 0, 1 중에 최댓값이 1이기 때문에 시간은 -1

m,n,h = map(int, input().split())
graph = []
for i in range(h): # 박스 갯수만큼
    temp = []
    for j in range(n): # 세로 길이 만큼
        temp.append(list(map(int, input().split())))
    graph.append(temp)
solution(m,n,h,graph)
