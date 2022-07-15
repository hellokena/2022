def solution(number, k):
    temp = 0
    stack = []
    for num in number:
        num = int(num)
        if len(stack) == 0: 
            stack.append(num)
        else:
            while k > 0 and len(stack) > 0 and stack[-1] < num: 
                stack.pop()
                k -= 1
            stack.append(num)
    if k > 0: # 아직 지울 수 있는 k 남음
        stack = stack[:-k]
    stack = map(str,stack)
    return ''.join(stack)

def solution(number, k):
    temp = 0
    stack = []
    for num in number:
        num = int(num)
        while k > 0 and len(stack) > 0 and stack[-1] < num: 
            stack.pop()
            k -= 1
        stack.append(num)
    if k > 0: # 아직 지울 수 있는 k 남음
        stack = stack[:-k]
    stack = map(str,stack)
    return ''.join(stack)
