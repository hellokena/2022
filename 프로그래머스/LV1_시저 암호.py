def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            temp = ord(i)+n
            if temp > ord('Z'):
                temp -= 26
            answer += chr(temp)
        elif i.islower():
            temp = ord(i)+n
            if temp > ord('z'):
                temp -= 26
            answer += chr(temp)
        elif i == ' ': answer += ' '
    return answer
        
