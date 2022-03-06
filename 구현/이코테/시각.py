def solution(n):
    cnt = 0
    for h in range(n+1): # 주의
        for m in range(60):
            for s in range(60):
                time = str(h)+str(m)+str(s)
                if time.count('3') > 0: cnt += 1
    print(cnt)

n = int(input())
solution(n)
