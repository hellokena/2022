def solution(n,p):
    answer = 0
    tmp = 0
    for i in sorted(p):
        tmp += i ##
        answer += tmp ##
        #answer += i*n
        #n -= 1
    print(answer)

n = int(input())
p = list(map(int, input().split()))
solution(n,p)
