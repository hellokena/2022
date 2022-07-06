# 같은 최단 경로 중 가장 위쪽,가장 왼쪽인 경로 찾기
from collections import deque
def bfs(hidx,widx,now_level): # 가장 가까운 물고기 찾기
    visited = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append((hidx,widx,0))
    visited[hidx][widx] = 1
    fish = []
    while queue:
        nowh, noww, cnt = queue.popleft()
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for d in range(4):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<n and 0<=nextw<n and visited[nexth][nextw] == 0:
                # 잡아먹을수 있는 물고기가 존재하는 경우
                # 물고기가 존재하고, 현재 아기 상어 레벨보다 작을 경우
                if graph[nexth][nextw] != 0 and graph[nexth][nextw] < now_level:
                    fish.append((cnt+1,nexth,nextw))
                    queue.append((nexth,nextw,cnt+1))
                    visited[nexth][nextw] = 1
                # 그냥 지나가는 경우
                # 물고기가 없거나, 같은 크기의 물고기 존재
                elif graph[nexth][nextw] == 0 or graph[nexth][nextw] == now_level:
                    queue.append((nexth,nextw,cnt+1))
                    visited[nexth][nextw] = 1
    fish.sort()
    if fish:
        return [fish[0][1], fish[0][2], fish[0][0]]
    else: return []

def solution(n,graph):
    answer = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9: # 아기상어 찾기
                graph[i][j] = 0 # 아기상어 위치 초기화
                y,x = i,j
                break
    level = 2
    eat = 0
    while True:
        fish_location = bfs(y,x,level)
        if fish_location: # 잡아 먹을 수 있는 물고기가 존재할 경우
            graph[fish_location[0]][fish_location[1]] = 0 # 와앙 잡아먹기
            eat += 1 # 현재 아기상어가 잡아먹은 물고기 갯수
            answer += fish_location[2] # 현재 물고기를 잡아먹고 지난 시간
            if eat == level: # 아기상어가 잡아먹은 물고기 갯수와 레벨이 동일하다면
                level += 1
                eat = 0
            y = fish_location[0]
            x = fish_location[1]
        else:
            break
    print(answer)


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
solution(n,graph)
