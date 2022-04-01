#문자열 재정렬
def solution(n):
    answer = ''
    num = 0
    n = list(n)
    n.sort()
    for i in n:
        if i.isdigit(): num += int(i)
        else: answer += i
    if num != 0: print(answer+str(num)) # 숫자가 하나도 없는 경우 처리
    else: print(answer)

n = input()
solution(n)
