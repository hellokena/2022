from collections import deque
import sys
input = sys.stdin.readline

def bfs(nidx,graph,visited):
    queue = deque()
    queue.append(nidx)
    visited[nidx] = 1  # 방문 처리
    while queue:
        now_node = queue.popleft()
        for next_node in graph[now_node]:
            if visited[next_node] == 0:  # 아직 방문하지 않은 경우
                visited[next_node] = -visited[now_node] # 자식은 우선 다 반대 부호로 칠해버령
                queue.append(next_node)
            else:  # 방문한 경우
                if visited[next_node] == visited[now_node]:
                    return False # 이분 그래프가 아님
    return True # 그 외의 경우 이분 그래프가 맞음

def solution(v,e,graph):
    flag = True # 우선 이분그래프가 맞다고 가정
    visited = [0 for _ in range((v+1))]
    for i in range(1,v+1):
        if visited[i] == 0: # 방문하지 않은경우
            if bfs(i,graph,visited) == False: # 이분 그래프가 아닐 경우
                flag = False
                break
    if flag == True: print("YES")
    else: print("NO")

t = int(input())
for _ in range(t):
    v,e = map(int, input().split())# 정점, 간선
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    solution(v,e,graph)
