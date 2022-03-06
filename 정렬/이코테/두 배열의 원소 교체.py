def solution(n,k,a,b):
    a.sort()
    b.sort(reverse=True)

    for i in range(k):
        if a[i] < b[i]: ##### 무작정 바꾸면 안됨! b수가 월등히 크면 어쩌려고??
            a[i], b[i] = b[i], a[i]
        else: # b가 더 크거나 작을 경우 어차피 뒤에것도 a보다 다 작을것
            break # 반복 줄여줌

    print(sum(a))

n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
solution(n,k,a,b)
