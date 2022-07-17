def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for num1,num2 in zip(A,B): # 짧은 거 기준으로 돌아간다
        answer += num1 * num2
    return answer
