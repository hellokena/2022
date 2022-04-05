# 우선순위큐, 최소힙 -> 일반적(오름차순 정렬)
import heapq
import sys
input = sys.stdin.readline

def solution(n,lists):
    heap = [] # heapq 모듈에서 리스트를 사용
    for x in lists:
        if x == 0: # 삭제
            if len(heap) == 0: print(0)
            else: print(heapq.heappop(heap))
        else: heapq.heappush(heap, x) # 삽입

n = int(input())
lists = []
for _ in range(n):
    lists.append(int(input()))
solution(n,lists)
