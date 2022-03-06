def solution(n, info):
    info.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
    for i in info:
        print(i[0])

n = int(input())
info = []
for _ in range(n):
    name, kor, eng, math = input().split()
    info.append([name, int(kor),int(eng),int(math)])
solution(n, info)
