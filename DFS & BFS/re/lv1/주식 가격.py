def solution(prices):
    answer = []
    for i in range(len(prices)): # 마지막 원소는 두번째 for문이 안돌아서 항상 0
        time = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]: # 증가
                time += 1 # 증가 시간 기록
            else: 
                time += 1 # 현재 시간
                break
        answer.append(time)
    return answer
