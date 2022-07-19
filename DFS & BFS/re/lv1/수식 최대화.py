# 스택은 후위 연산자로만 계산가능.......
# pop() 마지막, pop(0) 처음
from itertools import permutations
def calculate(expression,prior):
    # split된 문자열을 계속 조작하기 때문에 계산할때마다 갱신
    array = ['']
    for exp in expression:
        if exp.isdigit(): 
            array[-1] += str(exp)
        else: 
            array.append(exp)
            array.append('')
    for p in prior: 
        stack = [] 
        while array: # stack을 사용했지만 계속해서 앞부터 확인해준다
            tmp = array.pop(0) # 순서대로 하나씩
            if tmp == p: # 만약 현재 우선 순위
                # 현재 우선순위에 맞는 연산자를 만나면
                # 계산된 것 중 마지막(첫번째 피연산자)와 현재 연산자 그리고 array에 남아있는 첫 연산자(두번째 피연산자)를 계산한다. pop해줌
                stack.append(eval(str(stack.pop()) + tmp + str(array.pop(0))))
            else: stack.append(tmp) ##
        array = stack # 다음 연산자들도 차차 계산해줘야 하기 때문에 array를 stack으로 대치해준다
    return abs(int(array[0]))
        
def solution(expression):   
    answer = 0    
    priority = list(permutations(['+','*','-'],3)) # 각 조합
    for prior in priority: # 각 조합을 대상으로 식을 계산 -> 총 6번 for문
        answer = max(answer, (calculate(expression,prior)))
    return answer
        
        
    
     
    
