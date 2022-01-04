from collections import deque # 가장 짧은, 가장 빠른 BFS
import sys
sys.setrecursionlimit(10**5)

def solution(n,k): # BFS
    move = [0]*100001
    parent = [0]*100001 # 전의 위치
    q = deque() # 큐 선언
    q.append(n) # 언니의 위치 삽입
    while q:
        next = q.popleft()
        if next == k: # 언니와 동생의 위치가 동일
            print(move[next])
            # 위치
            answer = []
            while next != n: # 시작점까지 거슬러 올라감
                answer.append(next)
                next = parent[next]
            answer.append(n) # 시작점까지 추가
            answer.reverse()
            print(' '.join(map(str, answer))) # 숫자 전체를 str 형태로 형 변환 후 join
            break
        for i in [next-1, next+1, next*2]:
            if 0<=i<=100000 and not move[i]: # 범위안에 있고 아직 방문을 안했더라면
                move[i] = move[next]+1 # 1초 추가
                parent[i] = next # 전의 위치 추가
                q.append(i) # 새로운 위치 추가

n,k = map(int, input().split())
solution(n,k)
