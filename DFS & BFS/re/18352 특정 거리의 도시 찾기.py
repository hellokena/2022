import sys
from collections import deque
input = sys.stdin.readline

def solution(n,m,k,x,temp):
    graph = [[]*(n+1) for _ in range(n+1)]
    for i,j in temp:
        graph[i].append(j)
    answer = [0] * (n + 1)
    visited = [0] * (n + 1)
    queue = deque()
    queue.append(x)
    visited[x] = 1
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next] == 0:
                queue.append(next)
                answer[next] = answer[now] + 1
                visited[next] = 1
    if answer.count(k):
        for i in range(1,n+1):
            if answer[i] == k:
                print(i)
    else: print(-1)

n,m,k,x = map(int, input().split())
temp = []
for _ in range(m):
    temp.append(list(map(int, input().split())))
solution(n,m,k,x,temp)
