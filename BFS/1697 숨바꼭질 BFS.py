#bfs
from collections import deque
def solution(n,k):
    queue = deque()
    queue.append((n,0)) # 시간
    visited = {n}
    while queue:
        next, time = queue.popleft()
        if next == k:
            print(time)
            break
        # 방문한 위치는 다시 방문하지 않는다
        if 0<=next-1<=100000 and next-1 not in visited:
            queue.append((next-1, time+1))
            visited.add(next-1)
        if 0<=next+1<=100000 and next+1 not in visited:
            queue.append((next+1, time+1))
            visited.add(next+1)
        if 0<=next*2<=100000 and next*2 not in visited:
            queue.append((next*2, time+1))
            visited.add(next*2)

n,k = map(int, input().split())
solution(n,k)
