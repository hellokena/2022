import heapq # 계속해서 정렬필요함
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # 제일 작은게 k 이상이면 된다
    while scoville[0] < K and len(scoville) >= 2:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        made = first + second * 2
        heapq.heappush(scoville,made)
        answer += 1
    if scoville[0] < K: return -1
    return answer
    
