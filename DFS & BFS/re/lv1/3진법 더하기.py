def solution(n):
    answer = ''
    final_answer = 0
    while n > 0:
        n,d = divmod(n,3)
        answer += str(d)
    temp = 1
    for a in answer[::-1]:
        final_answer += temp * int(a)
        temp *= 3
    return final_answer
#   return int(answer, 3)
