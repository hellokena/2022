def solution(dartResult):
    answer = 0
    prev_score = 0
    now_score = 0
    ten_flag = False
    for i in range(len(dartResult)):
        if ten_flag: 
            ten_flag = False
            continue
        if dartResult[i].isdigit():
            print(dartResult[i])
            answer += prev_score
            prev_score = now_score
            star_flag = False
            if dartResult[i] == '1' and dartResult[i+1] == '0':
                now_score = 10
                print(now_score)
                ten_flag = True
            else: now_score = int(dartResult[i])
        elif dartResult[i] == 'S': 
            now_score **= 1
        elif dartResult[i] == 'D': 
            now_score **= 2
        elif dartResult[i] == 'T': 
            now_score **= 3
        elif dartResult[i] == '*': # 스타상
            prev_score *= 2 # 두배
            now_score *= 2 # 두배
            star_flag = True
        elif dartResult[i] == '#': # 아차상
            if star_flag == True: now_score *= -2 # 스타상과 중첩 -2배
            else: now_score = -now_score # 마이너스
    answer += prev_score
    answer += now_score  
    return answer
  
  def solution(dartResult):
    answer = 0
    prev_score = 0
    now_score = 0
    dartResult = dartResult.replace('10','k')
    for dart in dartResult:
        if dart.isdigit() or dart == 'k':
            star_flag = False
            answer += prev_score
            prev_score = now_score
            if dart == 'k': now_score = 10
            else: now_score = int(dart)
        elif dart == 'S': 
            now_score **= 1
        elif dart == 'D': 
            now_score **= 2
        elif dart == 'T': 
            now_score **= 3
        elif dart == '*': # 스타상
            prev_score *= 2 # 두배
            now_score *= 2 # 두배
            star_flag = True
        elif dart == '#': # 아차상
            if star_flag == True: now_score *= -2 # 스타상과 중첩 -2배
            else: now_score = -now_score # 마이너스
    answer += prev_score
    answer += now_score  
    return answer

def solution(dartResult):
    score = []
    now_score = ''
    for dart in dartResult:
        if dart.isdigit():
            now_score += dart
        if dart == 'S':
            now_score = int(now_score)**1
            score.append(now_score)
            now_score = ''
        elif dart == 'D':
            now_score = int(now_score)**2
            score.append(now_score)
            now_score = ''
        elif dart == 'T':
            now_score = int(now_score)**3
            score.append(now_score)
            now_score = ''
        elif dart == '*':
            if len(score) > 1:
                score[-2] *= 2
            score[-1] *= 2
        elif dart == '#':
            score[-1] = -score[-1] 
    return sum(score)
