def solution(arr, divisor):
    answer = []
    for a in arr:
        if a%divisor == 0:
            answer.append(a)
    answer.sort()
    if answer: return answer
    else: return [-1]
