from collections import deque
import sys
input = sys.stdin.readline

def bfs(nidx):
    visited = [0 for _ in range(n+1)]
    queue = deque()
    queue.append(nidx)
    visited[nidx] = 1
    cnt = 1
    while queue:
        nown = queue.popleft()
        for nextn in graph[nown]:
            if visited[nextn] == 0:
                queue.append(nextn)
                visited[nextn] = 1
                cnt += 1
    return cnt

def solution(graph):
    answer = []
    for i in range(1,n+1):
        answer.append(bfs(i)) # 해킹 가능 컴퓨터 갯수, idx
    max_value= max(answer)
    for i in range(n):
        if answer[i] == max_value:
            print(i+1, end= ' ')

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[b].append(a) ##
solution(graph)
