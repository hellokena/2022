import sys
from collections import Counter
def solution(n,array):
    array.sort()
    print(round(sum(array)/n)) #산술평균
    print(array[round(n//2)]) #중앙값

    if n == 1: print(array[0]) # 최빈값
    else:
        temp = Counter(array).most_common() ###
        if temp[0][1] == temp[1][1]: print(temp[1][0])
        else: print(temp[0][0])

    print(max(array)-min(array)) # 범위 : 최댓값 - 최솟값


array = []
n = int(input())
for _ in range(n):
    array.append(int(sys.stdin.readline()))
solution(n,array)
