from collections import deque

def solution(a,b):
    #visited = set()
    queue = deque()
    queue.append((a,0))
    #visited.add(a)
    while queue:
        n, cnt = queue.popleft()
        if n == b:
            print(cnt+1)
            return cnt+1
        if n*2<=b: #and n*2 not in visited:
            queue.append((n*2,cnt+1))
            #visited.add(n*2)
        temp = int(str(n)+'1')
        if temp<=b: #and temp not in visited:
            queue.append((temp,cnt+1))
            #visited.add(temp)
    print(-1)
    return -1

a,b = map(int, input().split())
solution(a,b)
