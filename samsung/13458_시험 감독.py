import math
def solution(n,a,b,c):
    answer = 0
    for i in range(n):
        now = a[i] - b # 정감독관
        answer += 1 # 정감독관
        if now > 0: # 아직 감독할 학생 남아 있는 경우
            answer += math.ceil(now/c)
    print(answer)

n = int(input())
a = list(map(int, input().split()))
b,c = map(int, input().split())
solution(n,a,b,c)
