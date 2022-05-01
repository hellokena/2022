from collections import deque
def solution(n,k):
    visited =[0]*200000
    queue = deque()
    queue.append((n,0))
    visited[n] = 1 # 방문 처리
    visited_cnt = 0 # 방문 횟수
    min_time = 0 # 방문한 최소 타임
    while queue:
        now,cnt = queue.popleft()
        visited[now] = 1
        if now == k:
            if visited_cnt == 0: # 첫 방문일 경우
                min_time = cnt
            if min_time == cnt:
                visited_cnt += 1
        # now-1, now+1, now*2는 방문한 적이 있으면 queue에 넣을 필요 없음
        # 어차피 똑같은 루트를 반복할 거니까
        # 그렇다고 해당 값들을 방문 처리하면 안됨
        # popleft 할때 visited 처리 되도록
        if 0<=now-1<=100000 and not visited[now-1]:
            queue.append((now-1,cnt+1))
        if 0<=now+1<=100000 and not visited[now+1]:
            queue.append((now+1,cnt+1))
        if 0<=now*2<=100000 and not visited[now*2]:
            queue.append((now*2,cnt+1))
    print(min_time)
    print(visited_cnt)

n,k = map(int, input().split())
solution(n,k)
