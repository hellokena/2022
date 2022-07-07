from collections import deque
# 멈추는 경우
# 벽인 경우, 구멍인 경우
# 파란 구슬이 구멍에 들어간 경우
# 빨강 파랑 둘다 구슬에 들어간 경우
# 파랑 구슬만 들어간 경우
def move(hidx,widx,dhidx,dwidx): # 구슬을 기울이는 경우
    # 움직일 때는 그 방향으로 쭉 가야함
    # 다음 칸이 #이 아니거나 현재 자리가 O이 아니면 계속 반복
    cnt = 0
    # 끝까지 기울임
    while graph[hidx+dhidx][widx+dwidx] != '#' and graph[hidx][widx] != 'O':
        hidx += dhidx
        widx += dwidx
        cnt += 1 # 총 횟수가 아니고 빨강 구슬, 파랑 구슬이 움직인 횟수 /  답 아님
    return hidx,widx,cnt

def bfs(rh,rw,bh,bw):
    visited = set()
    queue = deque()
    queue.append((rh,rw,bh,bw,0)) # 횟수
    visited.add((rh,rw,bh,bw))
    while queue:
        now_red_h, now_red_w, now_blue_h, now_blue_w, cnt = queue.popleft()
        if cnt >= 10: # 움직인 횟수가 10회 이상이면 할 수 없음 / -1 출력
            print(-1)
            return
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for d in range(4):
            next_red_h, next_red_w, r_cnt = move(now_red_h,now_red_w,dh[d],dw[d])
            next_blue_h, next_blue_w, b_cnt = move(now_blue_h,now_blue_w,dh[d],dw[d])
            # 파란 공이 구멍에 들어가지 않았고
            if graph[next_blue_h][next_blue_w] != 'O':
                # 빨간 공이 구멍에 들어간 경우
                if graph[next_red_h][next_red_w] == 'O':
                    print(cnt+1)
                    return
                # 빨간 구슬과 파란 구슬이 겹칠 경우
                if next_red_h == next_blue_h and next_red_w == next_blue_w:
                    # 더 많이 움직인 경우를 없앰
                    # r_cnt == b_cnt 경우는 없음
                    # 왜냐하면 두 개의 공은 같은 위치에 있을 수 없기 때문
                    if r_cnt > b_cnt: # 빨간 구슬이 더 많이 움직임
                        next_red_h -= dh[d]
                        next_red_w -= dw[d]
                    else:
                        next_blue_h -= dh[d]
                        next_blue_w -= dw[d]
            if (next_red_h,next_red_w,next_blue_h,next_blue_w) not in visited:
                queue.append((next_red_h,next_red_w,next_blue_h,next_blue_w,cnt+1))
                visited.add((next_red_h,next_red_w,next_blue_h,next_blue_w))
    print(-1)

def solution(n,m,graph):
    blueh, bluew = 0,0
    redh, redw = 0,0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'B':
                blueh, bluew = i,j
            elif graph[i][j] == 'R':
                redh, redw = i,j
    bfs(redh, redw, blueh, bluew)

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
solution(n,m,graph)
