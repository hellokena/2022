# combinations 사용
# 로또
from itertools import combinations
while True:
    s = list(map(int, input().split()))
    if s[0] == 0: break # 종료 조건
    tmp = list(combinations(s[1:],6))
    for i in tmp:
        print(' '.join(map(str, list(i))))
    print()

# ----------------------------------------

