def solution(x, n):
    answer = []
    i=x
    while len(answer) < n:
        answer.append(i)
        i += x
    return answer
    
def solution(x, n):
    answer = []
    # 우선 n개의 숫자니까 n번 돌림
    for i in range(n):
        answer.append(x*(i+1)) # 1부터 시작하도록
    return answer
