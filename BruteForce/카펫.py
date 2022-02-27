def solution(brown, yellow):
    num = brown + yellow # 총 격자 수
    # b가 a보다 값이 더 작으니까 b로 시작
    for b in range(1, num):
        if (num/b) % 1 == 0: # 딱 나누어 지는 경우
            a = num // b
        if a>=b and (a-2)*(b-2) == yellow and (2*a)+(2*b)-4 == brown:
            return [a,b]
