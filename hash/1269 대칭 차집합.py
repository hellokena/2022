def solution(na,nb,a,b):
    a = set(a)
    b = set(b)
    temp1 = a-b
    temp2 = b-a
    print(len(temp1)+len(temp2))

na, nb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
solution(na,nb,a,b)
