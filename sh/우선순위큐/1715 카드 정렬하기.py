# 계속적인 재정렬이 필요함
# 소팅을 계속하면 시간초과가 뜰수있음
# 우선순위 큐로 해결
import heapq
def solution(n, cards):
    answer = 0
    heapq.heapify(cards) # 우선순위 큐로 구현
    while len(cards) != 1: # 1개 남을때까지
        num1 = heapq.heappop(cards)
        num2 = heapq.heappop(cards)
        temp = num1 + num2
        answer += temp
        heapq.heappush(cards, temp) # cards에 temp를 추가
    print(answer)

n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))
solution(n, cards)
