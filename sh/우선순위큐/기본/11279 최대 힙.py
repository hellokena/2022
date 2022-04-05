# 우선순위큐, 최대힙(- 사용)
import heapq
import sys
input = sys.stdin.readline

def solution(n,lists):
    heap = [] # heapq 모듈에서 리스트를 사용
    for x in lists:
        if x == 0: # 삭제
            if len(heap) == 0: print(0)
            else: print(heapq.heappop(heap)[1]) # 첫번째 값은 정렬을 위한 쓰레기 값이므로 무시
        else: heapq.heappush(heap, (-x, x)) # 삽입 # -x를 인덱스로 활용

n = int(input())
lists = []
for _ in range(n):
    lists.append(int(input()))
solution(n,lists)
