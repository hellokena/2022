# bfs
from collections import deque

def comp(word1,word2): # 두 단어 비교
    dif = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2: dif += 1 
    if dif == 1: return True # 다른 알파벳이 1개면 True
    else: return False
    
def bfs(v, target, words):
    queue = deque()
    queue.append((v,0)) # (단어, 변경 횟수)
    while queue:
        nv,cnt = queue.popleft()
        if nv == target: return cnt # target 발견
        for i in words:
            if comp(nv,i): 
                queue.append((i, cnt+1))
    #else: print(0)
            
def solution(begin, target, words):
    answer = 0
    if target not in words: return 0 # 예외처리
    answer = bfs(begin, target, words)
    return answer
