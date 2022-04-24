from collections import deque

def bfs(pidx,cidx,relations):
    answer = [0]*(n+1)
    visited = [0]*(n+1)
    queue = deque()
    queue.append(pidx)
    visited[pidx] = 1
    while queue:
        nowc = queue.popleft()
        if nowc == cidx: return answer[cidx]
        for nextc in relations[nowc]:
            if visited[nextc] == 0:
                queue.append(nextc)
                visited[nextc] = 1
                answer[nextc] = answer[nowc] + 1
    return -1

def solution(n,p,c,temp):
    relations = [[] for _ in range(n+1)]
    for x,y in temp:
        relations[x].append(y)
        relations[y].append(x)
    print(bfs(p,c,relations))
n = int(input())
p,c = map(int, input().split())
r = int(input())
temp = []
for _ in range(r):
    temp.append(list(map(int, input().split())))
solution(n,p,c,temp)
