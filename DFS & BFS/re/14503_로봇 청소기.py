def solution(n,m,r,c,d,graph):
    visited = [[0]*m for _ in range(n)]
    # 북0,동1,남2,서3
    # 빈칸0, 벽1
    visited[r][c] = 1 # 방문처리
    answer = 1  # 제일먼저 잇는곳 청소
    while True:
        flag = 0
        # 북동남서
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        # 회전 알고리즘
        for _ in range(4):
            d = (d+3)%4
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<n and 0 <=nc<m and graph[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                answer += 1
                r = nr
                c = nc
                flag = 1 # 청소
                break # 청소 한 경우 break
        if flag == 0: # 청소 다 되어 있어서 청소 못함
            # 후진했을 때 벽이라면 break
            if graph[r-dr[d]][c-dc[d]] == 1:
                print(answer)
                break
            # 후진했을 때 벽 아니면 그대로 후진
            else:
                r = r - dr[d]
                c = c - dc[d]

n,m = map(int, input().split()) # 세로, 가로
r,c,d = map(int, input().split()) # 청소기 y,x,방향
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
solution(n,m,r,c,d,graph)
