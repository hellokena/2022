#dfs

answer = 0

def dfs(v):
    global answer
    visited[v] = 1 # 방문처리
    for i in graph[v]:
        if visited[i] == 0: # 아직 방문하지 않았다면
            answer += 1
            dfs(i)

def solution(n,m):
    global answer
    dfs(1)
    print(answer)

n = int(input()) # 컴퓨터 수
m = int(input()) # 네트워크 수
graph = [[] for _ in range(n+1)] # 연결리스트
visited = [0]*(n+1)
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
solution(n,m)
