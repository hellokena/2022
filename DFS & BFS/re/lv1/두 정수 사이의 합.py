def solution(a, b):
    answer = 0
    for i in range(min(a,b),max(a,b)+1):
        answer += i
    return answer
    
# sum안에 range를 바로 사용 가능하다...! # 게다가 시간도 빠름...

def solution(a, b):
    #answer = 0
    #for i in range(min(a,b),max(a,b)+1):
    #    answer += i
    return sum(range(min(a,b),max(a,b)+1))
