def solution(priorities, location):
    answer = 0
    while True:
        # 현재 가장 높은 우선 순위
        max_prior = max(priorities)
        # 모든 우선 순위 탐색 # 가장 높은 우선 순위를 가진 것을 찾아 떠난다
        for i in range(len(priorities)):
            # 만약 탐색하고 있는 현재 값이 최대 우선 순위라면
            if max_prior == priorities[i]:
                answer += 1 # 프린트하기
                priorities[i] = 0 # 프린트하기
                max_prior = max(priorities) # 다시 최대 우선순위 갱신 # 찾았으면 다음 우선순위로 바꿔볼까 # 다시 처음으로 가지 않기 위해서
                # 어차피 for문을 돌고있더라도 location에 도착하면 break 되기 때문에 상관없음
                # 만약 탐색하고 있는현재 값이 알고자 하는위치라면
                if i == location:
                    return answer
                    
# queue
# enumerate, any
def solution(priorities, location):
    printer = [(i,p) for i,p in enumerate(priorities)]
    turn = 0
    while printer:
        job = printer.pop(0)
        # 더 높은 우선 순위가 있는지 확인한다
        # 더 높은 우선 순위가 있으면 True
        # 더 높은 우선 순위가 없다면 False
        # 이 경우는더 높은 우선 순위가 없는 경우
        if any(job[1] < other_job[1] for other_job in printer): ##
            printer.append(job)
        # 내가 제일 우선 순위가 높다    
        else:
            turn += 1
            if job[0] == location:
                return turn
            
                                
    
