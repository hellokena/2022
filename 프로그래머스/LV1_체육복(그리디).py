def solution(n, lost, reserve):
    newreserve = list(set(reserve) - set(lost))
    newlost = list(set(lost) - set(reserve))
    answer = n - len(newlost) # 지금 수업 들을 수 있는 애
    for i in newlost:
        if i-1 in newreserve:
            answer += 1
            newreserve.remove(i-1)
        elif i+1 in newreserve:
            answer += 1
            newreserve.remove(i+1)
    return answer
