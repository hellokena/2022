from collections import deque
def bfs(n,computers,visited,nidx):
    queue = deque()
    queue.append(nidx)
    visited[nidx] = 1
    while queue:
        now = queue.popleft()
        for i in range(n):
            if i != now and computers[now][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
        
def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if visited[i] == 0:
            bfs(n,computers,visited,i)
            answer += 1
    return answer
