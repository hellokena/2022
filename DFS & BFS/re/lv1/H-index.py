def solution(citations):
    for i in range(0,max(citations)+1):
        cnt = 0
        for citation in citations:
            if citation >= i: cnt += 1
        if cnt >= i: answer = i
    return answer
