from collections import deque
def solution(a,b):
    queue = deque()
    queue.append((a,0))
    while queue:
        num, cnt = queue.popleft()
        if num == b: return cnt+1 # 최솟값에 +1을 더한 값을 출력
        if num*2 <= b: # 작은것만 계속해서 append # 연산들이 다 큰값만 생성 # / 연산 있을 경우 하면 안될듯
            queue.append((num*2, cnt+1))
        if int(str(num)+'1') <= b:
            queue.append((int(str(num)+'1'), cnt+1))
    else: return -1

a,b = map(int, input().split())
print(solution(a,b))
