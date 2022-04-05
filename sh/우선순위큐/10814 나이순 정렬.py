# 우선순위큐는 커스텀 소팅으로 가능하지만
# 계속해서 변경해주어야 하는 경우 우선순위 큐 쓰는게 더 유리할듯? heap?
def solution(n, lists):
    lists.sort(key = lambda x:x[0])
    for age, name in lists:
        print(age, name)

n = int(input())
lists = []
for _ in range(n):
    age, name = input().split()
    lists.append([int(age), name])
solution(n, lists)
