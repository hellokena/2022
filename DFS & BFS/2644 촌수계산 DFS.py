# dfs 촌수계산
# dfs, bfs 안에서 함수출력이 아닌 return 값을 받도록
import sys
sys.setrecursionlimit(10**5)

def dfs(v,n2,visited,result):
    visited[v] = 1  # 방문 처리
    # 재귀함수에서 조기종료는 어렵다...^^
    #if v == n2:
    for i in graph[v]:
        if visited[i] == 0: # 아직 방문하지 않은 노드
            result[i] = result[v] + 1
            dfs(i,n2,visited,result)

def solution(n,n1,n2,m,graph):
    visited = [0] * (n+1)
    result = [0] * (n+1)
    dfs(n1,n2,visited,result)
    # 여기서 리턴값 받기 - dfs 내부에서는 계속 돌아가기 때문
    if result[n2]:
        print(result[n2])
        return result[n2]
    else:
        print(-1)
        return -1

n = int(input()) # 사람수
n1, n2 = map(int, input().split()) # 촌수 계산해야 하는 사람
m = int(input()) # 관계수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
solution(n,n1,n2,m,graph)
