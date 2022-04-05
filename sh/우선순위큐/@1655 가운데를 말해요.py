# 계속해서 정렬이 필요한 문제 -> 우선순위 큐로 접근
# heapq는 오름차순/내림차순으로 정렬해주지 않음
# 중간값을 구해야하기 때문에 번갈아서 넣어줌
import heapq
import sys
input = sys.stdin.readline

def solution(n, nums):
    answer = []
    left_heap = [] # 최대힙 # left_heap의 첫원소가 중간값
    right_heap = [] # 최소힙
    for n in nums:
        # 번갈아서 넣어주기
        # 백준이가 외친 수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야한다
        # 중간값은 left_heap에 존재
        if len(left_heap) == len(right_heap):
            heapq.heappush(left_heap, (-n, n))
        else:
            heapq.heappush(right_heap, (n, n))
        # left_heap의 루트가 right_heap의 루트보다 크면 루트 변경
        if right_heap and left_heap[0][1] > right_heap[0][0]:
            miin = heapq.heappop(right_heap)[1]
            maax = heapq.heappop(left_heap)[1]
            heapq.heappush(left_heap, (-miin, miin))
            heapq.heappush(right_heap, (maax, maax))
        answer.append(left_heap[0][1])
    for a in answer:
        print(a)

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
solution(n, nums)
