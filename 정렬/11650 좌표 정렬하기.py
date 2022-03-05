def solution(n, array):
    array.sort()
    for x,y in array:
        print(x,y)

n = int(input())
array = []
for _ in range(n):
    x,y = map(int, input().split())
    array.append([x,y])
solution(n,array)
