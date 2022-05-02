def comp(a,b):
    diff = 0
    for i,j in zip(a,b):
        if i!=j: diff += 1
    if diff == 1: return True
    return False

from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = set()
    queue = deque()
    queue.append((begin,0))
    visited.add(begin)
    while queue:
        nextword, cnt = queue.popleft()
        if nextword == target: return cnt
        for word in words:
            if comp(nextword,word) and word not in visited:
                queue.append((word,cnt+1))
                visited.add(word)
    return answer
