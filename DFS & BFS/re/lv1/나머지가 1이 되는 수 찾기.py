def solution(n):
    for i in range(1,n+1): # 0으로 나눌 수 없음
        if n%i == 1: return i
