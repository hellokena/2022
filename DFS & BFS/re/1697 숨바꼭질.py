from collections import deque

def bfs(n,k):
    visited = set()
    queue = deque()
    queue.append((n,0))
    visited.add(n) # 시간단축
    while queue:
        loc, cnt = queue.popleft()
        if loc == k: break
        if 0<=loc-1<=100000 and loc-1 not in visited:
            queue.append((loc-1,cnt+1))
            visited.add(loc-1)
        if 0<=loc+1<=100000 and loc+1 not in visited:
            queue.append((loc+1,cnt+1))
            visited.add(loc+1)
        if 0<=loc*2<=100000 and loc*2 not in visited:
            queue.append((loc*2,cnt+1))
            visited.add(loc*2)
    return cnt

def solution(n,k):
    print(bfs(n,k))
n,k = map(int, input().split())
solution(n,k)
