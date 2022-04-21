from collections import deque

def bfs(n):
    answer = 0
    queue = deque()
    queue.append(0)
    while queue:
        nown = queue.popleft()
        if nown == n: answer += 1
        if nown+1<=n: queue.append(nown+1)
        if nown+2<=n: queue.append(nown+2)
        if nown+3<=n: queue.append(nown+3)
    return answer

def solution(n):
    print(bfs(n))
    
t = int(input())
for _ in range(t):
    n = int(input())
    solution(n)
