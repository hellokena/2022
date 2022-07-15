def solution(n):
    ans = 0
    # 계속해서 2로 나누고 남은 나머지를 더한다.
    # d가 0인 경우는 순간이동(*2,건전지X)
    # d가 1인 경우는 점프(+1,건전지O)
    while n > 0:
        n,d = divmod(n,2)
        ans += d # 딱 나눠떨어져서 나머지가 0이면 더해지지 않음
    return ans
