from collections import deque
def solution(n,graph):
    visited= [0]*n
    queue = deque()
    queue.append((0,0)) # idx, time
    visited[0] = 1 # 방문 처리
    while queue:
        now_idx, cnt = queue.popleft()
        if now_idx == n-1:
            print(cnt)
            return
        for i in range(now_idx,now_idx+graph[now_idx]+1):
            if 0<=i<n and visited[i] == 0:
                queue.append((i,cnt+1))
                visited[i] = 1
    print(-1)

n = int(input())
graph = list(map(int, input().split()))
solution(n,graph)
