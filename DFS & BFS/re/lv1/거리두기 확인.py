from collections import deque
def bfs(i,j,place):
    queue = deque()
    queue.append((i,j,0))
    visited = [[0]*5 for _ in range(5)]
    visited[i][j] = 1
    while queue:
        nowh, noww, dist = queue.popleft()
        # 맨해튼 거리 2 이하로 앉아야 하므로 대각선 불가!
        dh = [-1,1,0,0]
        dw = [0,0,-1,1]
        for d in range(4):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<5 and 0<=nextw<5 and visited[nexth][nextw] == 0:
                if place[nexth][nextw] == 'P' and dist+1 <= 2: # 거리 2 이내 사람 발견
                    return False # 위반
                elif place[nexth][nextw] == 'O':
                    queue.append((nexth,nextw,dist+1))  
                    visited[nexth][nextw] = 1          
    return True # 잘 지킴
            
def solution(places):
    answer = []
    for place in places:
        state = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs(i,j,place): 
                        state = False
                        break
            if not state: break
        if state: answer.append(1)
        else: answer.append(0)
    return answer
