def solution(n,k,temp):
    temp.sort()
    print(temp[k-1])
n,k = map(int, input().split())
temp = list(map(int, input().split()))
solution(n,k,temp)
