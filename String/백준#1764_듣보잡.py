# 듣보잡
def solution(hear,watch):
    names = sorted(list(set.intersection(set(hear), set(watch)))) # 교집합
    print(len(names))
    for name in names:
        print(name)

n,m = map(int, input().split())
# hear = [input() for i in range(n)]
# watch = [input() for i in range(m)]
hear =[] # 듣도 못한 사람의 명단
watch = [] # 보도 못한 사람의 명단
for i in range(n):
    hear.append(input())
for j in range(m):
    watch.append(input())
solution(hear,watch)
