from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0,-1)) # answer, idx번까지 넣었다
    while queue:    
        now_sum, now_idx = queue.popleft()
        if now_idx == len(numbers)-1:
            if now_sum == target:
                answer += 1 
        else:
            queue.append((now_sum + numbers[now_idx+1], now_idx+1))
            queue.append((now_sum - numbers[now_idx+1], now_idx+1))
    return answer
