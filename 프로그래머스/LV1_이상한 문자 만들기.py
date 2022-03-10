def solution(s):
    answer = ''
    temp = s.split(" ")
    for t in temp:
        for i in range(len(t)):
            if i%2==0:
                answer += t[i].upper()
            else:
                answer += t[i].lower()
        answer += ' '
    return answer[:-1]
