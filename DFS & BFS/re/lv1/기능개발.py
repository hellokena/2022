import math
def solution(progresses, speeds):
    answer = []
    progresses = [100-progresses[i] for i in range(len(progresses))] # 남은 퍼센테이지
    for i in range(len(progresses)):
        progresses[i] = math.ceil(progresses[i]/speeds[i]) # 2.1이 나오면 일이 걸리는 거지
    now = 0
    for day in progresses:
        if now < day:
            answer.append(1)
            now = day # 기준 변경
        else: 
            answer[-1] += 1
    return answer
