def solution(lists):
    lists = list(set(lists))
    lists.sort()
    lists.sort(key=lambda x: len(x))
    for l in lists:
        print(l)

n = int(input())
lists = []
for _ in range(n):
    lists.append(input())
solution(lists)
