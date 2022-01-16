#bfs
from collections import deque

def bfs(s, c, numbers, target):
    answer = 0
    queue = deque()
    queue.append((numbers[0],0)) # (첫번째수, idx)
    queue.append((-numbers[0],0)) # (-첫번째수, idx)
    while queue:
        num, idx = queue.popleft()
        # 두 if문을 합치면 안됨
        # 합해버리면 길이가 끝까지 돌았는데도, 합이 3이 안될 경우 계속해서 돔
        # 합해버리면 길이가 끝까지 안돌았는데도,합이 3이 되었을 경우 계속해서 돔
        # 1. 우선 idx가 끝까지 돌았는지 확인
        if idx == len(numbers)-1: # 2. idx가 끝까지 돌았다면
            if num == target: # 3. 합이 target과 같은지 확인
                answer += 1 
        else: # 4. idx가 끝까지 안돌았다면 계속해서 append
            queue.append((num+numbers[idx+1],idx+1))
            queue.append((num-numbers[idx+1],idx+1))
    return answer
        
def solution(numbers, target):
    answer = bfs(0, 0, numbers, target)
    print(answer)
    return answer
    
