def solution(n, m, nonhear, nonwatch):
    nonhear = set(nonhear)
    nonwatch = set(nonwatch)
    answer = list(nonhear & nonwatch)
    answer.sort()
    print(len(answer))
    for a in answer:
        print(a)

n, m = map(int, input().split())
nonhear = []
nonwatch = []
for _ in range(n):
    nonhear.append(input())
for _ in range(m):
    nonwatch.append(input())
solution(n, m, nonhear, nonwatch)
