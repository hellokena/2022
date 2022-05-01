from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((numbers[0],0))
    queue.append((-numbers[0],0))
    while queue:
        num, idx = queue.popleft()
        if idx == len(numbers)-1:
            if num == target:
                answer += 1
        else:
            queue.append((num+numbers[idx+1],idx+1))
            queue.append((num-numbers[idx+1],idx+1))
    return answer
