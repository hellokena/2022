while True:
    sentences = input()
    stack = []
    if sentences == '.': break # 종료 조건
    for s in sentences:
        if s == '(' or s == '[': # 열린 괄호의 경우 stack에 추가
            stack.append(s)
        elif s == ')': # 작은 닫는 괄호
            if stack:
                if stack[-1] == '(': stack.pop() # 괄호 종류를 체크해야 하므로 if문이 필요한 것
                else:
                    print('no')
                    break
            else:
                print('no')
                break
        elif s == ']': # 큰 닫는 괄호
            if stack:
                if stack[-1] == '[': stack.pop() # 괄호 종류를 체크해야 하므로 if문이 필요한 것
                else:
                    print('no')
                    break
            else:
                print('no')
                break
    else: # for-else문
        if not stack: print('yes')
        else: print('no')
