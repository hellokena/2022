from collections import deque
def bfs(nidx,temp):
    cnt = 0
    visited = [0]*(n+1)
    queue = deque()
    queue.append(nidx)
    visited[nidx] = 1
    while queue:
        nown = queue.popleft()
        cnt += 1
        for nextn in temp[nown]:
            if visited[nextn] == 0:
                queue.append(nextn)
                visited[nextn] = 1
    return cnt-1 # 1번 제외

def solution(n,m,graph):
    temp = [[] for i in range(n+1)]
    for node1, node2 in graph:
        temp[node1].append(node2)
        temp[node2].append(node1)
    print(bfs(1,temp))

n = int(input())
m = int(input())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))
solution(n,m,graph)
