from collections import deque
def solution(n,k):
    parent = [0]*200000
    visited = set()
    queue = deque()
    queue.append((n,0))
    visited.add(n)
    while queue:
        now, cnt = queue.popleft()
        if now == k:
            print(cnt)
            answer = []
            while now != n:
                answer.append(now)
                now = parent[now]
            answer.append(n) # 얘는 시작점이라서 parent 없으니까
            answer.reverse()
            print(' '.join(map(str, answer)))
            break

        for i in [now-1, now+1, now*2]:
            if 0<=i<=100000 and i not in visited:
                queue.append((i,cnt+1))
                visited.add(i)
                parent[i] = now

n,k = map(int, input().split())
solution(n,k)
