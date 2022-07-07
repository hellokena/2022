from collections import deque
def bfs(nidx):
    bacon = [0 for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    queue = deque()
    queue.append(nidx)
    visited[nidx] = 1
    while queue:
        now_node = queue.popleft()
        for next_node in relations[now_node]:
            if visited[next_node] == 0:
                bacon[next_node] = bacon[now_node] + 1
                queue.append(next_node)
                visited[next_node] = 1
    return sum(bacon)

def solution(relations):
    answer = []
    for i in range(1,n+1):
        answer.append(bfs(i))
    print(answer.index(min(answer))+1)
    
n,m = map(int, input().split())
relations = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)
solution(relations)
