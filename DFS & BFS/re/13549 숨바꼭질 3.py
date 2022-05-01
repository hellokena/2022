from collections import deque
def solution(n,k):
    visited = set()
    queue = deque()
    queue.append((n,0))
    visited.add(n)
    while queue:
        now, cnt = queue.popleft()
        if now == k: print(cnt)
        if 0<=2*now<=100000 and 2*now not in visited:
            queue.appendleft((now*2,cnt))
            visited.add(now*2)
        if 0<=now-1<=100000 and now-1 not in visited:
            queue.append((now-1,cnt+1))
            visited.add(now-1)
        if 0<=now+1<=100000 and now+1 not in visited:
            queue.append((now+1,cnt+1))
            visited.add(now+1)
            
n,k = map(int, input().split())
solution(n,k)

# ---------------------------------------------

from collections import deque


def solution(n, k):
    visited = set()
    queue = deque()
    queue.append((n, 0))
    visited.add(n)
    while queue:
        now, cnt = queue.popleft()
        if now == k: print(cnt)
        if 0 <= 2 * now <= 100000 and 2 * now not in visited:
            queue.appendleft((now * 2, cnt))
            visited.add(now * 2)
        for next in [now-1, now+1]:
            if 0 <= next <= 100000 and next not in visited:
                queue.append((next, cnt + 1))
                visited.add(next)

n, k = map(int, input().split())
solution(n, k)
