def solution(n,s,g,p,d,mvp):
    answer = 0
    prev = 0 # 전 달 # ** 첫달을 계산하는 코드를 따로 빼기보다는 0으로 초기화
    for i in range(n):

        if mvp[i] == 'B': # 브론즈
            answer += s-1 - prev
            prev = s-1 - prev # 대치

        elif mvp[i] == 'S': # 실버
            answer += g-1 - prev
            prev = g-1 - prev

        elif mvp[i] == 'G': # 골드
            answer += p-1 - prev
            prev = p-1 - prev

        elif mvp[i] == 'P': # 플래티넘
            answer += d-1 - prev
            prev = d-1 - prev

        else: # ** 다이아는 더 이상의 등급이 없기 때문에 최대과금액을 계속 더해주면 최댓값 
            answer += d
            prev = d

    print(answer)

n = int(input()) # 개월수
s,g,p,d = map(int, input().split())
mvp = list(input())

solution(n,s,g,p,d,mvp)
# --------------------------------------------------

def solution(n,s,g,p,d,mvp):

    # 첫달계산
    if mvp[0] == 'B': answer = s-1
    elif mvp[0] == 'S': answer = g-1
    elif mvp[0] == 'G': answer = p-1
    elif mvp[0] == 'P': answer = d-1
    else: answer = d

    fmonth = answer # 첫달 temp값

    for i in range(1,n):
        if mvp[i] == 'B': smonth = s-1
        elif mvp[i] == 'S': smonth = g-1
        elif mvp[i] == 'G': smonth = p-1
        elif mvp[i] == 'P': smonth = d-1
        else:
            smonth = d # 최대 과금액 # 다이아몬드 이상으로 올라갈곳 없음
            answer += d
            continue
        answer += smonth - fmonth
        fmonth = smonth - fmonth

    print(answer)

n = int(input()) # 개월수
s,g,p,d = map(int, input().split())
mvp = list(input())

solution(n,s,g,p,d,mvp)
