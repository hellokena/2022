def solution(array):
    for a in sorted(array):
        print(a)

array = []
n = int(input())
for _ in range(n):
    array.append(int(input()))
solution(array)
