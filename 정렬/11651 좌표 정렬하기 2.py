def solution(n, array):
    array.sort(key=lambda x:(x[1],x[0]))
    for x,y in array:
        print(x,y)

n = int(input())
array = []
for _ in range(n):
    x,y = map(int, input().split())
    array.append([x,y])
solution(n,array)
