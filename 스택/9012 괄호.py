def solution(ps):
    stack = 0
    for p in ps:
        if p == ')': stack -= 1
        else: stack += 1
        # 양수는 될 수 있어도 음수는 안됨
        if stack < 0:
            print('NO')
            break
            #return 'NO'
    else: # for-else 문
        if stack == 0: print('YES')
        else: print('NO')

t = int(input())
array = []
for _ in range(t):
    ps = input()
    solution(ps)
