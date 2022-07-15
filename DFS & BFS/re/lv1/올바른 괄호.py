def solution(s):
    #while '()' in s:
        #s = s.replace('()','')
    #if len(s) == 0: return True
    #else: return False
    stack = []
    for i in s:
        if i == '(': stack.append(i)
        elif i == ')': # ')'
            ## 닫힌 괄호가 나왔는데 열린 현재 스택에 아무것도 없다면 오류
            if not stack: return False 
            elif stack and stack[-1] == '(': stack.pop()
    if not stack: return True
    return False
