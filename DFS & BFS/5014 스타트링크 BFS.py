#bfs
from collections import deque

def solution(floor,start,goal,up,down):
    move = [0]*10000001 # 1~1000000 # 누른 횟수
    #parent = [0]*10000001
    queue = deque() # 큐 선언
    queue.append(start) # 시작점 삽입
    while queue:
        v = queue.popleft()
        if v == goal:
            print(move[v])
            #answer = []
            #while v != start:
            #    answer.append(v) # 끝점 삽입
            #    v = parent[v] # 부모 찾기
            #answer.append(start) # 시작점 삽입
            #answer.reverse()
            #print(' '.join(map(str, answer)))
            break
        for np in [v+up, v-down]:
            # move[np] == 1 이라면 방문한 적이 이미 있음, 즉 전에 더 빨리 갈수있음
            # np!=start : 다시 시작점으로 돌아오면
            # 현재 move[1]이 0이라서 불필요한 탐색 한번 더하게 됨 그걸 방지
            if start<=np<floor and move[np] == 0 and np!=start: ##
                move[np] = move[v] + 1
                #parent[np] = v
                queue.append(np)
    else: print('use the stairs') # while-else문

# 전체층, 시작, 골, 업, 다운
floor,start,goal,up,down = map(int, input().split())
solution(floor,start,goal,up,down)

# -----------------------------------------------

#bfs
from collections import deque

def solution(floor,start,goal,up,down):
    queue = deque() # 큐 선언
    queue.append((start,0)) # 횟수
    visited = {start}
    while queue:
        v, cnt = queue.popleft()
        if v == goal:
            print(cnt)
            break
        if 1<=v+up<=floor and v+up not in visited:
            queue.append((v+up, cnt+1))
            visited.add(v+up) ## set은 add
        if 1<=v-down<=floor and v-down not in visited:
            queue.append((v-down, cnt+1))
            visited.add(v-down) ##
    print('use the stairs')

# 전체층, 시작, 골, 업, 다운
floor,start,goal,up,down = map(int, input().split())
solution(floor,start,goal,up,down)
