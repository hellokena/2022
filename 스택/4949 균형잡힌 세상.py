while True:
    sen = input()
    if sen == '.': break
    stack = []
    for s in sen:
        if s == '(': stack.append('(')
        elif s == '[': stack.append('[')
        # stack에는 닫는 괄호가 들어갈 수 없다
        elif s == ')':
            if len(stack) == 0: # 닫는 괄호가 있는데 길이가 0일 수 없음
                print('no')
                break
            if stack[-1] == '(':
                stack.pop()
                continue
            elif stack[-1] == '[':
                print('no')
                break
        elif s == ']':
            if len(stack) == 0: # 닫는 괄호가 있는데 길이가 0일 수 없음
                print('no')
                break
            if stack[-1] == '[':
                stack.pop()
                continue
            elif stack[-1] == '(':
                print('no')
                break
    else:
        if len(stack) == 0: print('yes')
        else: print('no')
