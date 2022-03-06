def solution(n, array):
    array.sort(reverse=True)
    for i in array:
        print(i, end = ' ')

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
solution(n, array)
