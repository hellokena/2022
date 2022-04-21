from collections import deque

def bfs(nidx):
    visited = set()
    queue = deque()
    queue.append((nidx,0))
    visited.add(nidx)
    while queue:
        nown, cnt = queue.popleft()
        if nown == g: return cnt
        if 1<=nown-d<=f and nown-d not in visited:
            queue.append((nown-d,cnt+1))
            visited.add(nown-d)
        if 1<=nown+u<=f and nown+u not in visited:
            queue.append((nown+u, cnt+1))
            visited.add(nown+u)
    return "use the stairs"

def solution(f,s,g,u,d):
    print(bfs(s))

f,s,g,u,d = map(int, input().split())
solution(f,s,g,u,d)
