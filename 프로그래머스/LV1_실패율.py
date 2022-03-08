def solution(N, stages):
    answer = []
    temp = []
    num = len(stages) # 플레이어수
    temp = [stages.count(i) for i in range(1, N+1)]
    cur = 0
    for i in temp:
        if num-cur != 0:
            answer.append(i/(num-cur))
        else: answer.append(0)
        cur += i
    test = []
    for i,s in enumerate(answer):
        test.append([i+1,s])
    test.sort(key = lambda x:-x[1])
    result = [i[0] for i in test]
    return result
