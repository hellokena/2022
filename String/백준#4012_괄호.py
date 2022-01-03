# stack
def solution(lists):
    for l in lists:
        stack = [] # 스택
        for i in l:
            if i == '(': stack.append(i)
            else: # )
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else: # 길이가 0이거나 마지막 괄호가 닫는 괄호일 경우
                    stack.append(')')
        if len(stack) == 0: print('YES')
        else: print('NO')


t = int(input())
lists = []
for _ in range(t):
    lists.append(input())
solution(lists)

# -----------------------------

# stack
def solution(lists):
    for l in lists:
        stack = [] # 스택
        for i in l:
            if i == '(': stack.append(i)
            else: # )
                if stack: # not empty
                    stack.pop()
                else: # empty
                    print('NO') # )이 있다는 것은 무조건 앞에 (이 있어야 되는데 그걸 만족하지 못한 것
                    break
        else: # for - else
            if stack: print('NO')
            else: print('YES') # empty

t = int(input())
lists = []
for _ in range(t):
    lists.append(input())
solution(lists)

# -----------------------------

def solution(lists):
    for l in lists:
        sum = 0
        for i in l:
            if i == '(': sum += 1
            else: sum -= 1
            # 계산시 무조건 sum의 값이 0이거나 1이여야 함
            # ()이 pair로 맞아서 0이 되거나
            # (이 먼저 나와서 1이 됨
            # 즉, )이 ( 보다 먼저 나와서 -1이 될 수는 없음
            if sum == -1:
                print('NO')
                break
        else: # for - else
            if sum == 0: print('YES')
            else: print('NO') # empty

t = int(input())
lists = []
for _ in range(t):
    lists.append(input())
solution(lists)
