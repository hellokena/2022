from collections import deque

def bfs(nidx):
    visited = [0]*
    queue = deque()
    queue.append(nidx)
    visited[nidx] = 1
    while queue:
        nown = queue.popleft()
        if nown == n-1: return 'YES'
        for nextn in range(nown+1, n):
            power = (nextn-nown)*(1+abs(stones[nown]-stones[nextn]))
            if power<=k and visited[nextn] == 0:
                queue.append(nextn)
                visited[nextn] = 1
    return 'NO'

def solution(n,k,stones):
    print(bfs(0))

n,k = map(int, input().split())
stones = list(map(int, input().split()))
solution(n,k,stones)
