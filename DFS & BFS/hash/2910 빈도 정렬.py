from collections import defaultdict
def solution(n,c,code):
    cnt = defaultdict(int)
    for i in code:
        cnt[i] += 1
    temp = sorted(cnt.items(), key=lambda x:x[1], reverse=True)
    for i in temp:
        for j in range(i[1]):
            print(i[0], end = ' ')

n,c = map(int, input().split())
code = list(map(int, input().split()))
solution(n,c,code)
