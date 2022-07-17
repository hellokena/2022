# 재귀로 짜면 시간초과...
def solution(n):
    answer = []
    for i in range(0,n+1):
        if i<2: answer.append(i)
        else: answer.append(answer[i-2]+answer[i-1])
    return answer[n]%1234567
    
