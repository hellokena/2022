def solution(n, lost, reserve):
    # 여분 옷이 있는 애들이 도난당한 경우
    now_lost = list(set(lost) - set(reserve))
    now_reserve = list(set(reserve) - set(lost))
    for l in now_lost:
        if l-1 in now_reserve: 
            now_reserve.remove(l-1)
        elif l+1 in now_reserve: 
            now_reserve.remove(l+1)
        else: n-= 1
    return n
    
    
