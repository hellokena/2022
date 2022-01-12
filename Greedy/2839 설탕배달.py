def solution(n):
    answer = 0
    while n>0:
        if n%5==0:
            answer += n//5
            #n -= 5*(n//5)
            print(answer)
            break
        else:
            answer += 1
            n -= 3
    #if n: print(-1) # 설탕이 남았다면
    #else: print(answer) # 남은 설탕이 0
    else: print(-1) # while-else문

n = int(input())
solution(n)
