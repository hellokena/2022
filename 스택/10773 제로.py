def solution(k, array):
    stack = []
    for a in array:
        if a == 0: stack.pop()
        else: stack.append(a)
    print(sum(stack))

k = int(input()) # 숫자수
array = []
for _ in range(k):
    array.append(int(input()))
solution(k, array)
