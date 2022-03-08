import heapq
def solution(n, cards):
    heapq.heapify(cards) # 우선순위 큐로 heapify
    answer = 0
    while len(cards) != 1: # 1개가 남을 때까지
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        temp = a + b
        answer += temp
        heapq.heappush(cards, temp)
    print(answer)

n = int(input()) # 카드 묶음 갯수
cards = []
for _ in range(n):
    cards.append(int(input()))
solution(n, cards)
