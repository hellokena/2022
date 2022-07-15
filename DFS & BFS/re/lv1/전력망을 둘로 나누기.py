from collections import deque
import sys

def bfs(nidx,graph,visited):
    cnt = 0
    queue = deque()
    queue.append(nidx)
    visited[nidx] = 1
    while queue:
        nown = queue.popleft()
        cnt += 1
        for nextn in graph[nown]:
            if visited[nextn] == 0:
                queue.append(nextn)
                visited[nextn] = 1
    return cnt

def solution(n, wires):
    result = sys.maxsize
    for i in range(len(wires)):
        answer = []
        remove = wires.pop(i) # 전선 중 하나 끊은 다음 저장
        graph = [[] for _ in range(n+1)]
        visited = [0]*(n+1)
        for a,b in wires:
            graph[a].append(b)
            graph[b].append(a)
        # 한번에 연결된 모든 걸 찾는 경우는 bfs내에서 visited 선언해도되지만
        # 주어진 그래프내에서 모든영역을 찾는다든가 하는 경우는 밖에서 visited 선언
        for j in range(1,n+1): ## 0이 아닌 1부터 시작한다
            if visited[j] == 0:
                answer.append(bfs(j,graph,visited))
        if len(answer) == 2: # 영역이 2개로 나눠진 경우
             result = min(result, abs(answer[0]-answer[1]))
        wires.insert(i,remove) # 끊은 전선을 해당 위치에 다시 추가   
    return result
