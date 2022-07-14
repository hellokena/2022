# py 제공 안함
from collections import deque
def bfs(m,n,picture,i,j,visited):
    area_num = picture[i][j] # 현재 영역 숫자
    cnt = 0
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    while queue:
        nowh,noww = queue.popleft()
        cnt += 1
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for d in range(4):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<m and 0<=nextw<n:
                if visited[nexth][nextw] == 0 and picture[nexth][nextw] == area_num:
                    queue.append((nexth,nextw))
                    visited[nexth][nextw] = 1
    return cnt

def solution(m,n,picture):
    areas = []
    visited = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            # picture의 원소 중 값이 0인경우는 색칠하지 않는 영역을 뜻한다.
            if visited[i][j] == 0 and picture[i][j] != 0:
                areas.append(bfs(m,n,picture,i,j,visited))
    print(len(areas),max(areas))

m,n = 6,4 # 세로, 가로
picture = [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]
solution(m,n,picture)
