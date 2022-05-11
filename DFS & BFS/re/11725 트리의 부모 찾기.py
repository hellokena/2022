from collections import deque

def bfs(nidx,temp):
    visited = [0]*(n+1)
    answer = [0]*(n+1)
    queue = deque()
    queue.append(nidx)
    visited[nidx] = 1
    while queue:
        nown = queue.popleft()
        for nextn in temp[nown]:
            if visited[nextn] == 0:
                answer[nextn] = nown
                queue.append(nextn)
                visited[nextn] = 1
    return answer

def solution(n,graph):
    temp = [[] for _ in range(n+1)]
    for x,y in graph:
        temp[x].append(y)
        temp[y].append(x)
    answer = bfs(1,temp) # 루트부터 차근차근
    for a in answer[2:]:
        print(a)

n = int(input())
graph = []
for _ in range(n-1):
    graph.append(list(map(int, input().split())))
solution(n,graph)

# -------------------

from collections import deque
import sys
input = sys.stdin.readline

def bfs(nidx,temp):
    answer = [0]*(n+1)
    queue = deque()
    queue.append(nidx)
    while queue:
        nown = queue.popleft()
        for nextn in temp[nown]:
            if answer[nextn] == 0:
                answer[nextn] = nown
                queue.append(nextn)
    return answer

def solution(n,graph):
    temp = [[] for _ in range(n+1)]
    for x,y in graph:
        temp[x].append(y)
        temp[y].append(x)
    answer = bfs(1,temp) # 루트부터 차근차근
    for a in answer[2:]:
        print(a)

n = int(input())
graph = []
for _ in range(n-1):
    graph.append(list(map(int, input().split())))
solution(n,graph)
