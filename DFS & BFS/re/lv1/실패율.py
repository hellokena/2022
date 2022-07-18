def solution(N, stages):
    answer = {}
    for level in range(1,N+1):
        solve_user = 0
        non_play_yet = 0
        for user in stages:
            if user > level: # 해결한 유저
                solve_user += 1
            elif user == level: # 도달 했으나 아직 클리어 못함
                non_play_yet += 1
        if solve_user + non_play_yet == 0: answer[level] = 0
        else: 
            answer[level] = non_play_yet / (solve_user + non_play_yet)
    answer = sorted(answer.items(),reverse=True,key = lambda x:x[1])
    temp = []
    for key,value in answer:
        temp.append(key)
    return temp
