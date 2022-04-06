def solution(n,m,strings,findstrs):
    answer = 0
    for findstr in findstrs:
        if findstr in strings: answer += 1
    print(answer)

n,m = map(int, input().split())
strings = []
for _ in range(n):
    strings.append(input())
findstrs = []
for _ in range(m):
    findstrs.append(input())
solution(n,m,strings,findstrs)
