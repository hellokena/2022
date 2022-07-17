def solution(s):
    answer = ''
    idx = 0
    for i in s:
        if i == ' ':
            idx,temp = -1, ' ' # 인덱스 초기화
        else:
            if idx == 0: temp = i.upper()
            else: temp = i.lower()
        answer += temp
        idx += 1
    return answer
    
    def solution(s):
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    return ' '.join(s)
