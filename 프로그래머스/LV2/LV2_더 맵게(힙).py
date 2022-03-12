import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # 원소 0, 1, 2 나눔
    while scoville: # 원소가 0개면 -1리턴
        if scoville[0] >= K: return answer # 첫원소가 그 이상일경우
        if len(scoville) >= 2: # 원소 길이가 2이상
            min1 = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1+min2*2)
            answer += 1
        else: return -1 # 원소 길이가 1개
    return -1
