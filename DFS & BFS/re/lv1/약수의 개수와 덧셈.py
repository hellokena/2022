# 제곱수는 약수가 홀수개
import math
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if math.sqrt(i) == int(math.sqrt(i)):
            answer -= i
        else: answer += i
    return answer
