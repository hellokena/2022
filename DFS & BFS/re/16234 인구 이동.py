from collections import deque
import sys
input = sys.stdin.readline

def bfs(hidx,widx,visited):
    queue = deque()
    queue.append((hidx,widx))
    visited[hidx][widx] = 1
    # 연합 국가
    union = []
    union.append((hidx,widx)) # 연합된 국가 기록
    people = graph[hidx][widx] # 연합된 국가 속 인원 수
    while queue:
        nowh,noww = queue.popleft()
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for d in range(4):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<n and 0<=nextw<n and visited[nexth][nextw] == 0:
                if l<=abs(graph[nexth][nextw]-graph[nowh][noww])<=r:
                    people += graph[nexth][nextw]
                    queue.append((nexth,nextw))
                    visited[nexth][nextw] = 1 # 방문 처리
                    union.append((nexth,nextw)) # 연합 국가 추가
    for h,w in union:
        graph[h][w] = people // len(union)
    return len(union)

def solution(n,l,r,graph):
    answer = 0 # 인구이동 발생 일수
    while True:
        flag = False  # 인구이동 발생 유무 ###
        visited = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0:
                    if bfs(i,j,visited) > 1:
                        flag = True
        if flag == False:
            break
        answer += 1
    print(answer)

n,l,r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
solution(n,l,r,graph)
