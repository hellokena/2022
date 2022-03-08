def solution(citations):
    for i in range(max(citations),0,-1):
        tmp = list(filter(lambda x:x>=i, citations))
        cnt = len(tmp)
        # i: n번이상, cnt:인용된 논문의 갯수
        if i<=cnt:
            return i
    else: return 0
