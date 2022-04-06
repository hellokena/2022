# bfs도 될듯?
from collections import deque
def solution(n):
    sset = set()
    queue = deque()
    queue.append((n,0))
    sset.add(n)
    while queue:
        num, cnt = queue.popleft()
        if num == 1: break
        if num%3 == 0 and num//3 not in sset:
            temp = num//3
            queue.append((temp,cnt+1))
            sset.add(temp)
        if num%2 == 0 and num//2 not in sset:
            temp = num// 2
            queue.append((temp,cnt+1))
            sset.add(temp)
        if num - 1 not in sset:
            temp = num - 1
            queue.append((temp,cnt+1))
            sset.add(temp)
    print(cnt)

n = int(input())
solution(n)
