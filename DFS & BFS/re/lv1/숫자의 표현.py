def solution(n): # 완탐
    answer = 0
    # 니가 생각하는 단순 포문 맞음!! 슬라이딩 윈도우 비슷! 어렵게 생각하지 말자
    for i in range(1,n+1): # 각 숫자(1,2,3,4,5...)
        sum = 0
        for j in range(i,n+1):
            sum += j
            if sum == n: 
                answer += 1
                break
            elif sum >= n: break # 커지면 의미가 없다 # 효율성 관련
    return answer
