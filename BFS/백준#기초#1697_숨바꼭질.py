from collections import deque
import sys
sys.setrecursionlimit(10**5)

def solution(n,k):
    move = [0]*100001
    q = deque()
    q.append(n) # 1. 시작 append
    while q:
        v = q.popleft()
        if v == k: # 위치 도달
            print(move[v])
            break
        for np in [v-1, v+1, v*2]:
            if 0<=np<=100000 and move[np]==0:
                move[np] = move[v]+1
                q.append(np)

n,k = map(int, input().split())
solution(n,k)
