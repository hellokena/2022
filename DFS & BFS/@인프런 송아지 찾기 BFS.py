# 송아지 찾기 # BFS
from collections import deque
def solution(s,e):
    visitied = [0]*10001
    queue = deque()
    queue.append((s,0)) # 현수 위치와 점프 횟수
    visitied[s] = 1 # 방문 처리
    while queue:
        now, jump = queue.popleft()
        if e == now: break # 현수가 송아지 위치에 도착
        for next in (now-1, now+1, now+5):
            if 1<=next<=10001 and visitied[next] == 0:
                queue.append((next, jump+1))
                visitied[next] = 1 # 방문 처리
    print(jump)

s,e = map(int, input().split()) # 현수와 송아지의 위치
solution(s,e)
