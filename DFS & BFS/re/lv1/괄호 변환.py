def divide(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(': cnt += 1
        elif p[i] == ')': cnt -= 1
        if cnt == 0: return p[:i+1], p[i+1:]

def check(u):
    cnt = 0
    for i in range(len(u)):
        if u[i] == '(': cnt += 1
        elif u[i] == ')': cnt -= 1
        if cnt < 0: return False
    if cnt == 0: return True

def solution(p):
    # 1단계
    if p == '': return p
    # 2단계
    u,v = divide(p)
    if check(u): return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]    
        for i in u:
            if i == '(': answer += ')'
            elif i == ')': answer += '('
    return answer  
