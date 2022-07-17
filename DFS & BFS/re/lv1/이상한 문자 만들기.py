def solution(s):
    answer = ''
    idx = 0
    for i in s:
        if i == ' ': # 공백일 경우 reset
            idx, temp = -1,' '
        if idx%2==0: # 짝수
            temp = i.upper()
        elif idx%2!=0: # 홀수
            temp = i.lower()
        answer += temp
        idx += 1
    return answer
