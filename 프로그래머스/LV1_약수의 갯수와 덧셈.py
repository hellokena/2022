def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        temp = 0
        for i in range(1, n+1):
            if n%i == 0:
                temp += 1 # 약수의 갯수
        if temp%2 == 0: answer += i
        else: answer -= i
    return answer
    
    def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        if n**0.5 == int(n**0.5):
            answer -= n
        else: answer += n
    return answer
    
    import math
def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        if math.sqrt(n) == int(math.sqrt(n)):
            answer -= n
        else: answer += n
    return answer
