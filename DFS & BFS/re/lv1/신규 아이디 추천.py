def solution(new_id):
    # 1단계 : 소문자 치환
    new_id = new_id.lower()
    # 2단계 : 소문자, 숫자, -_.만 포함
    answer = ''
    for i in new_id: #2
        if i.islower() or i.isdigit() or i in ['-','_','.']: answer += i
    # 3단계 : 연속된 .. 제거
    while '..' in answer:
        answer = answer.replace('..','.')
    # 4단계 : 앞뒤 . 제거
    answer = answer.strip('.')
    # 5단계 : 공백이면 a
    if len(answer) == 0: answer = 'a'
    #6 6단계 : 길이 16이상이면 줄이기 + 마지막 . 제거
    if len(answer) >= 16: 
        answer = answer[:15]
        answer = answer.rstrip('.')
    # 7단계 : 길이 2 이하라면 마지막 숫자 3 될때까지 반복
    while len(answer) <= 2:
        answer += answer[-1]
    return answer
